from telegram.ext import (
    Application,
    CommandHandler,
    MessageHandler,
    filters,
)
from handlers import start, message_handler
from admin import (
    admin_panel,
    total_users,
    add_number,
    broadcast,
    statistics,
)
from config import BOT_TOKEN


app = Application.builder().token(BOT_TOKEN).build()

# Commands
app.add_handler(CommandHandler("start", start))
app.add_handler(CommandHandler("admin", admin_panel))

# Admin Buttons
app.add_handler(MessageHandler(filters.Regex("^👥 Total Users$"), total_users))
app.add_handler(MessageHandler(filters.Regex("^📥 Add Number$"), add_number))
app.add_handler(MessageHandler(filters.Regex("^📢 Broadcast$"), broadcast))
app.add_handler(MessageHandler(filters.Regex("^📊 Statistics$"), statistics))

# All Messages
app.add_handler(
    MessageHandler(filters.TEXT & ~filters.COMMAND, message_handler)
)

print("✅ Bot Started")

app.run_polling()
