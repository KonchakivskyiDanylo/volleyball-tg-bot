import os
from dotenv import load_dotenv

load_dotenv()

ADMIN_IDS = os.getenv("CARD_NUMBER")


def is_authorized(user_id):
    return user_id in ADMIN_IDS
