from telegram import ReplyKeyboardMarkup

def user_keyboard():
    keyboard = [
        ["📞 Get Number", "🛡 Checker Set"],
        ["📊 My Stats", "🚦 Live Traffic"],
        ["✉️ 2FA Set"]
    ]

    return ReplyKeyboardMarkup(
        keyboard,
        resize_keyboard=True
    )


def admin_keyboard():
    keyboard = [
        ["➕ Add Number", "➖ Remove Number"],
        ["🛠 Add Service", "❌ Delete Service"],
        ["📢 Broadcast", "👥 User List"],
        ["📊 Statistics", "🚫 Block User"],
        ["✅ Unblock User", "⚙ Settings"]
    ]

    return ReplyKeyboardMarkup(
        keyboard,
        resize_keyboard=True
    )
