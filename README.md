# 🏐 Volleyball Telegram Bot

**A Telegram bot built to automate volleyball team coordination: training schedules, voting, messaging, and payment
management.**
Designed for simplicity and effectiveness to streamline team operations across both male and female teams.
🤝 **Collaborated with:** [@VeronikaGovorischeva](https://github.com/VeronikaGovorischeva)

---

## 🚀 Features

* ✅ **User registration** with name and team (Male/Female)
* 📅 **Training management**: add, view, and vote for one-time and recurring trainings
* 📤 **Broadcast messages** to specific teams
* 🗳️ **Voting system** with vote limits and reminders
* 💳 **Payment tracking** with dynamic cost splitting and debt handling
* 🔄 **Admin utilities**: unlock training for both teams, manage votes/payments
* 🛠️ **MongoDB** integration for persistent storage

---

## 🛠️ Tech Stack

* **Python 3.10+**
* [python-telegram-bot](https://github.com/python-telegram-bot/python-telegram-bot)
* **MongoDB** for data persistence
* **APScheduler** for periodic tasks
* `.env` file for configuration

---

## 📁 Project Structure

```bash
.
├── main.py                   # Entry point and handler registration
├── registration.py          # User registration logic
├── trainings.py             # Add and view training sessions
├── voting.py                # Voting system logic
├── payments.py              # Payment collection and tracking
├── notifier.py              # Daily job to trigger voting and reminders
├── commands.py              # Admin commands to broadcast messages
├── data.py                  # MongoDB data I/O utilities
├── validation.py            # Role validation and admin check
├── requirements.txt         # Project dependencies
```

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
BOT_TOKEN=your_telegram_bot_token
MONGO_URI=your_mongo_uri
TRAINING_COST=200
CARD_NUMBER=your_card_number
ADMIN_IDS=your_admin_ids
```

> ⚠️ `ADMIN_IDS` should be a space-separated list of Telegram user IDs.

---

## 🧪 Running the Bot

```bash
python main.py
```

The bot uses `APScheduler` to:

* Start voting daily at 15:00
* Send voting reminders at 16:00
* Reset training vote states at 22:00

---

## 🧠 Key Commands

| Command            | Description                          |
|--------------------|--------------------------------------|
| `/start`           | Register user (name + team)          |
| `/add_training`    | Admin-only: Add training             |
| `/next_training`   | Show next training for user’s team   |
| `/week_trainings`  | List all trainings for the week      |
| `/vote_training`   | Vote for upcoming training           |
| `/view_votes`      | View current votes                   |
| `/charge_all`      | Admin-only: Request payments         |
| `/pay_debt`        | Pay outstanding debts                |
| `/send_message`    | Admin-only: Send message to a team   |
| `/unlock_training` | Admin-only: Allow both teams to vote |

---

### 🧊 Future Improvements

* 💳 **Improved Payments** – Use [Telegram Payments](https://core.telegram.org/bots/payments) for secure, user-friendly
  in-app transactions with automatic confirmation.
* 📄 **Logging** – Integrate structured logging for better debugging, auditing, and monitoring.
* 🌐 **Webhook Support** – Switch from polling to webhook deployment (for better scalability & performance).
* 🏐 **Game Management** – Extend current training logic to handle friendly matches and tournaments, including voting,
  reminders, and stats.

---

## 👨‍💻 Contributing

PRs welcome! Please create an issue for any major feature before submitting a pull request.

---

## 📜 License

MIT License. See `LICENSE.md` for details.
