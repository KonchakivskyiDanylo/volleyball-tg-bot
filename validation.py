import os
from dotenv import load_dotenv

load_dotenv()

ADMIN_IDS = os.getenv("ADMIN_IDS", "").split(",")
EXCLUDED_IDS = os.getenv("EXCLUDED_IDS", "").split(",")


def is_authorized(user_id):
    return str(user_id) in ADMIN_IDS


def is_excluded_from_stats(user_id):
    return str(user_id) in EXCLUDED_IDS
