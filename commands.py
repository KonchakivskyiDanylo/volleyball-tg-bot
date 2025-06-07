from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import ContextTypes
from data import *

SEND_MESSAGE_STATE = {}

async def send_message_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keyboard = InlineKeyboardMarkup([
        [
            InlineKeyboardButton("Чоловіча команда", callback_data="send_team_Male"),
            InlineKeyboardButton("Жіноча команда", callback_data="send_team_Female"),
        ],
        [InlineKeyboardButton("Обидві команди", callback_data="send_team_Both")]
    ])
    await update.message.reply_text("Оберіть команду, якій хочете надіслати повідомлення:", reply_markup=keyboard)


async def handle_send_message_team_selection(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()

    team = query.data.replace("send_team_", "")
    SEND_MESSAGE_STATE[query.from_user.id] = team

    await query.edit_message_text(f"Ви обрали: {team} команда.\n\nТепер надішліть текст повідомлення у наступному повідомленні.")


async def handle_send_message_input(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_id = update.message.from_user.id
    if user_id not in SEND_MESSAGE_STATE:
        return

    team = SEND_MESSAGE_STATE.pop(user_id)
    message_text = update.message.text
    users = load_data("users")

    count = 0
    for uid, info in users.items():
        if team in [info.get("team"), "Both"]:
            try:
                await context.bot.send_message(chat_id=int(uid), text=message_text)
                count += 1
            except Exception as e:
                print(f"❌ Не вдалося надіслати повідомлення {uid}: {e}")

    await update.message.reply_text(f"✅ Повідомлення надіслано {count} користувачам.")