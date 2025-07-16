# 🏐 Volleyball Telegram Bot

**A comprehensive Telegram bot built to automate volleyball team coordination: training schedules, game management,
voting systems, payment tracking, and detailed statistics.**

🤝 **Collaborated with:** [@VeronikaGovorischeva](https://github.com/VeronikaGovorischeva)

---

## 📑 Table of Contents

- [🚀 Features](#-features)
- [🛠️ Tech Stack](#-tech-stack)
- [🧩 Setup Instructions](#-setup-instructions)
- [🧪 Testing](#-testing)
- [🚀 Running the Bot](#-running-the-bot)
- [🧠 Key Commands](#-key-commands)
- [🔮 Future Roadmap](#-future-roadmap)
- [👨‍💻 Contributing](#-contributing)
- [🔒 Security Considerations](#-security-considerations)

---

## 🚀 Features

### 👥 **User & Team Management**

* User registration with team selection (Male/Female)
* Admin role validation and secure access control
* Personal statistics tracking and performance dashboards

### 📅 **Training & Game Management**

* Create and manage trainings (one-time and recurring)
* Complete game lifecycle: creation → voting → results → payments
* Support for multiple game types (friendly, league competitions)
* Automated scheduling with smart status updates

### 🗳️ **Voting & Communication**

* Training and game voting with automated reminders
* Broadcast messaging to specific teams
* Vote limits and deadline management

### 💳 **Payment & Statistics**

* Dynamic cost splitting based on attendance
* Automated debt tracking with payment confirmations
* Comprehensive statistics: MVP tracking, attendance rates, game results
* Historical performance analysis and team comparisons

---

## 🛠️ Tech Stack

* **Python 3.10+**
* [python-telegram-bot](https://github.com/python-telegram-bot/python-telegram-bot) - Telegram Bot API
* **MongoDB** - Persistent data storage with flexible schema
* **APScheduler** - Automated scheduling for daily tasks
* **pytest** - Comprehensive testing framework

---

## 🧩 Setup Instructions

### 1. Clone the repository

```bash
git clone https://github.com/your-username/volleyball-team-bot.git
cd volleyball-team-bot
```

### 2. Install dependencies

```bash
pip install -r requirements.txt
```

### 3. Configure environment variables

Create a `.env` file:

```env
# Bot Configuration
NEW_TOKEN=your_telegram_bot_token
MONGO_URI=your_mongodb_connection_string

# Admin Configuration (comma-separated Telegram user IDs)
ADMIN_IDS=123456789,987654321
EXCLUDED_IDS=111222333

# Payment Configuration
CARD_NUMBER=your_card_number_for_payments
```

> ⚠️ **Security Note**: Never commit real tokens or IDs to version control. Use the `.env` file for all sensitive data.

---

## 🧪 Testing

### Run all tests

```bash
python run_tests.py
```

### Run with coverage

```bash
python run_tests.py -c
```

### Run specific test file

```bash
python run_tests.py -s test_registration
```

---

## 🚀 Running the Bot

```bash
python main.py
```

The bot uses **APScheduler** to automatically:

* 🗳️ Start daily voting at 15:00 (server timezone)
* 🔔 Send voting reminders at 16:00 (server timezone)
* 🎮 Send game reminders at 16:00 (server timezone)
* 🔄 Reset training statuses at 19:00 (server timezone)

---

## 🧠 Key Commands

### 👤 **Public Commands**

| Command           | Description                                   |
|-------------------|-----------------------------------------------|
| `/start`          | Register with name and team selection         |
| `/next_training`  | Show your next scheduled training             |
| `/week_trainings` | Display all trainings for current week        |
| `/next_game`      | Show your next upcoming game                  |
| `/list_games`     | List all upcoming games                       |
| `/week_games`     | Display all games for current week            |
| `/vote`           | Vote for upcoming training sessions and games |
| `/view_votes`     | View current voting status                    |
| `/pay_debt`       | Confirm payment of outstanding debts          |
| `/mvp_stats`      | View MVP rankings by team                     |
| `/my_stats`       | View personal statistics and MVP history      |
| `/training_stats` | View training participation statistics        |
| `/game_stats`     | View game participation statistics            |
| `/game_results`   | View historical game results and records*     |

### 🔧 **Admin Commands**

| Command            | Description                                 |
|--------------------|---------------------------------------------|
| `/add_training`    | Create new training session                 |
| `/add_game`        | Create new game (friendly/league)           |
| `/delete_game`     | Remove a game from schedule                 |
| `/add_vote`        | Add new voting session                      |
| `/vote_for`        | Vote on behalf of team members              |
| `/close_vote`      | Close voting and finalize results           |
| `/unlock_training` | Allow both teams to vote on training        |
| `/charge_all`      | Request payments from training participants |
| `/send_message`    | Broadcast message to specific teams         |
| `/notify_debtors`  | Send reminder to users with unpaid debts    |
| `/view_payments`   | View all payment statuses                   |
| `/close_game`      | Close game with results and MVP selection*  |
| `/edit_game`       | Modify existing game details                |
| `/vote_notify`     | Send voting notifications                   |

> *Future: Add attendance tracking based on votes and MVP selection

---

## 🔮 Future Roadmap

### 💳 **Advanced Payment Integration**

### 🌐 **Scalability Improvements**

### 🏐 **Advanced Game Features**

---

## 👨‍💻 Contributing

Contributions are welcome! Please:

1. **Fork** the repository
2. **Create** a feature branch
3. **Add tests** for new functionality
4. **Ensure** all tests pass
5. **Submit** a pull request

For major features, please create an issue first to discuss the proposed changes.

---

## 🔒 Security Considerations

* All sensitive data (tokens, IDs) stored in environment variables
* Admin authorization required for sensitive operations
* Input validation for all user data
* Secure MongoDB connection with authentication
* Regular security testing included in test suite

---

## 📜 License

MIT License. See `LICENSE.md` for details.

---

## 🙏 Acknowledgments

Special thanks to [@VeronikaGovorischeva](https://github.com/VeronikaGovorischeva) for collaboration and to the
volleyball community for feature inspiration and testing.