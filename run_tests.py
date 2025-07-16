#!/usr/bin/env python3
"""
Comprehensive Test Runner for Volleyball Project

This script runs all tests in the project with detailed reporting,
coverage analysis, and error handling.

Usage:
    python run_tests.py [options]

Options:
    --verbose, -v       : Verbose output
    --coverage, -c      : Run with coverage report
    --html-cov         : Generate HTML coverage report
    --specific, -s     : Run specific test file (e.g., test_registration)
    --failed-only, -f  : Run only previously failed tests
    --parallel, -p     : Run tests in parallel
    --quiet, -q        : Minimal output
    --help, -h         : Show this help message
"""

import os
import sys
import subprocess
import argparse
import time
from pathlib import Path
from typing import List, Dict, Optional


class Colors:
    """ANSI color codes for terminal output"""
    GREEN = '\033[92m'
    RED = '\033[91m'
    YELLOW = '\033[93m'
    BLUE = '\033[94m'
    MAGENTA = '\033[95m'
    CYAN = '\033[96m'
    WHITE = '\033[97m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
    END = '\033[0m'


class TestRunner:
    """Comprehensive test runner for the volleyball project"""

    def __init__(self):
        self.project_root = Path(__file__).parent
        self.tests_dir = self.project_root / "tests"
        self.test_files = []
        self.results = {}

    def discover_test_files(self) -> List[str]:
        """Discover all test files in the tests directory"""
        if not self.tests_dir.exists():
            print(f"{Colors.RED}❌ Tests directory not found: {self.tests_dir}{Colors.END}")
            return []

        test_files = []
        for file in self.tests_dir.glob("test_*.py"):
            test_files.append(file.stem)

        if not test_files:
            print(f"{Colors.YELLOW}⚠️  No test files found in {self.tests_dir}{Colors.END}")

        return sorted(test_files)

    def check_dependencies(self) -> bool:
        """Check if required testing dependencies are installed"""
        required_packages = ['pytest', 'pytest-asyncio', 'pytest-mock', 'pytest-cov']
        missing_packages = []

        for package in required_packages:
            try:
                __import__(package.replace('-', '_'))
            except ImportError:
                missing_packages.append(package)

        if missing_packages:
            print(f"{Colors.RED}❌ Missing required packages:{Colors.END}")
            for pkg in missing_packages:
                print(f"   - {pkg}")
            print(f"\n{Colors.CYAN}💡 Install with: pip install {' '.join(missing_packages)}{Colors.END}")
            return False

        return True

    def run_tests(self,
                  verbose: bool = False,
                  coverage: bool = False,
                  html_coverage: bool = False,
                  specific_test: Optional[str] = None,
                  failed_only: bool = False,
                  parallel: bool = False,
                  quiet: bool = False) -> Dict:
        """Run tests with specified options"""

        if not self.check_dependencies():
            return {"success": False, "error": "Missing dependencies"}

        # Discover test files
        self.test_files = self.discover_test_files()
        if not self.test_files:
            return {"success": False, "error": "No test files found"}

        # Build pytest command
        cmd = ["python", "-m", "pytest"]

        # Add test directory
        if specific_test:
            if specific_test in self.test_files:
                cmd.append(f"tests/{specific_test}.py")
            else:
                print(f"{Colors.RED}❌ Test file '{specific_test}' not found{Colors.END}")
                print(f"Available tests: {', '.join(self.test_files)}")
                return {"success": False, "error": f"Test file '{specific_test}' not found"}
        else:
            cmd.append("tests/")

        # Add options
        if verbose and not quiet:
            cmd.extend(["-v", "--tb=short"])
        elif quiet:
            cmd.append("-q")
        else:
            cmd.append("--tb=line")

        if coverage:
            cmd.extend([
                "--cov=.",
                "--cov-report=term-missing",
                "--cov-exclude=tests/*",
                "--cov-exclude=run_tests.py"
            ])

        if html_coverage:
            cmd.append("--cov-report=html")

        if failed_only:
            cmd.append("--lf")

        if parallel:
            cmd.extend(["-n", "auto"])

        # Add async support
        cmd.append("--asyncio-mode=auto")

        # Add color output
        cmd.append("--color=yes")

        print(f"{Colors.BOLD}{Colors.BLUE}🚀 Running Tests{Colors.END}")
        print(f"{Colors.CYAN}Command: {' '.join(cmd)}{Colors.END}")
        print("=" * 60)

        start_time = time.time()

        try:
            # Run tests
            result = subprocess.run(
                cmd,
                cwd=self.project_root,
                capture_output=False,
                text=True
            )

            end_time = time.time()
            duration = end_time - start_time

            # Analyze results
            success = result.returncode == 0

            print("\n" + "=" * 60)
            if success:
                print(f"{Colors.GREEN}✅ All tests passed! ({duration:.2f}s){Colors.END}")
            else:
                print(f"{Colors.RED}❌ Some tests failed! ({duration:.2f}s){Colors.END}")

            if html_coverage:
                coverage_dir = self.project_root / "htmlcov"
                if coverage_dir.exists():
                    print(f"{Colors.CYAN}📊 Coverage report: {coverage_dir}/index.html{Colors.END}")

            return {
                "success": success,
                "return_code": result.returncode,
                "duration": duration,
                "command": cmd
            }

        except Exception as e:
            print(f"{Colors.RED}❌ Error running tests: {e}{Colors.END}")
            return {"success": False, "error": str(e)}

    def run_specific_test_categories(self) -> Dict:
        """Run tests by category with detailed reporting"""
        categories = {
            "Registration Tests": ["test_registration"],
            "Command Tests": ["test_commands"],
            "Data Tests": ["test_data"],
            "Notifier Tests": ["test_notifier"],
            "Training Tests": ["test_trainings"] if "test_trainings" in self.test_files else []
        }

        results = {}
        total_duration = 0

        print(f"{Colors.BOLD}{Colors.MAGENTA}📋 Running Tests by Category{Colors.END}\n")

        for category, test_files in categories.items():
            if not test_files or not all(tf in self.test_files for tf in test_files):
                print(f"{Colors.YELLOW}⏭️  Skipping {category} - files not found{Colors.END}")
                continue

            print(f"{Colors.BOLD}{Colors.CYAN}🔍 {category}{Colors.END}")

            for test_file in test_files:
                result = self.run_tests(specific_test=test_file, quiet=True)
                results[test_file] = result
                if result.get("duration"):
                    total_duration += result["duration"]

                status = "✅" if result.get("success") else "❌"
                duration = result.get("duration", 0)
                print(f"   {status} {test_file}.py ({duration:.2f}s)")

            print()

        # Summary
        passed = sum(1 for r in results.values() if r.get("success"))
        total = len(results)

        print("=" * 60)
        print(f"{Colors.BOLD}📊 Category Test Summary{Colors.END}")
        print(f"Passed: {Colors.GREEN}{passed}{Colors.END}/{total}")
        print(f"Total Duration: {total_duration:.2f}s")

        if passed == total:
            print(f"{Colors.GREEN}🎉 All test categories passed!{Colors.END}")
        else:
            print(f"{Colors.RED}⚠️  {total - passed} test categories failed{Colors.END}")

        return results

    def lint_and_test(self) -> Dict:
        """Run linting and tests together"""
        print(f"{Colors.BOLD}{Colors.BLUE}🔍 Running Linting + Tests{Colors.END}\n")

        # Try to run flake8 if available
        try:
            lint_result = subprocess.run(
                ["python", "-m", "flake8", ".", "--exclude=tests", "--max-line-length=120"],
                cwd=self.project_root,
                capture_output=True,
                text=True
            )

            if lint_result.returncode == 0:
                print(f"{Colors.GREEN}✅ Linting passed{Colors.END}")
            else:
                print(f"{Colors.YELLOW}⚠️  Linting issues found:{Colors.END}")
                print(lint_result.stdout)

        except FileNotFoundError:
            print(f"{Colors.CYAN}💡 Install flake8 for linting: pip install flake8{Colors.END}")

        # Run tests
        test_result = self.run_tests(coverage=True)

        return {
            "lint_success": lint_result.returncode == 0 if 'lint_result' in locals() else None,
            "test_result": test_result
        }


def main():
    """Main function with argument parsing"""
    parser = argparse.ArgumentParser(
        description="Comprehensive test runner for volleyball project",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
    python run_tests.py                    # Run all tests
    python run_tests.py -v -c             # Verbose with coverage
    python run_tests.py -s test_registration  # Run specific test
    python run_tests.py --html-cov        # Generate HTML coverage
    python run_tests.py --categories      # Run by categories
    python run_tests.py --lint-and-test   # Lint + test
        """
    )

    parser.add_argument("-v", "--verbose", action="store_true",
                        help="Verbose output")
    parser.add_argument("-c", "--coverage", action="store_true",
                        help="Run with coverage report")
    parser.add_argument("--html-cov", action="store_true",
                        help="Generate HTML coverage report")
    parser.add_argument("-s", "--specific", type=str,
                        help="Run specific test file (without .py extension)")
    parser.add_argument("-f", "--failed-only", action="store_true",
                        help="Run only previously failed tests")
    parser.add_argument("-p", "--parallel", action="store_true",
                        help="Run tests in parallel")
    parser.add_argument("-q", "--quiet", action="store_true",
                        help="Minimal output")
    parser.add_argument("--categories", action="store_true",
                        help="Run tests by category")
    parser.add_argument("--lint-and-test", action="store_true",
                        help="Run linting and tests")

    args = parser.parse_args()

    runner = TestRunner()

    try:
        if args.categories:
            result = runner.run_specific_test_categories()
        elif args.lint_and_test:
            result = runner.lint_and_test()
        else:
            result = runner.run_tests(
                verbose=args.verbose,
                coverage=args.coverage,
                html_coverage=args.html_cov,
                specific_test=args.specific,
                failed_only=args.failed_only,
                parallel=args.parallel,
                quiet=args.quiet
            )

        # Exit with appropriate code
        if isinstance(result, dict) and result.get("success") is False:
            sys.exit(1)
        elif isinstance(result, dict) and "test_result" in result:
            sys.exit(0 if result["test_result"].get("success") else 1)
        else:
            sys.exit(0)

    except KeyboardInterrupt:
        print(f"\n{Colors.YELLOW}⏹️  Tests interrupted by user{Colors.END}")
        sys.exit(130)
    except Exception as e:
        print(f"{Colors.RED}❌ Unexpected error: {e}{Colors.END}")
        sys.exit(1)


if __name__ == "__main__":
    main()