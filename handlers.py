from telegram import Update
from telegram.ext import ContextTypes

from config import ADMIN_ID
from database import add_user
from keyboards import user_keyboard, admin_keyboard


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user = update.effective_user

    add_user(user.id)

    if user.id == ADMIN_ID:
        await update.message.reply_text(
            "👑 Welcome Admin!\n\nAdmin Panel চালু হয়েছে।",
            reply_markup=admin_keyboard()
        )
    else:
        await update.message.reply_text(
            "👋 Welcome to zANTI OTP BOT!\n\nনিচের মেনু থেকে একটি অপশন নির্বাচন করুন।",
            reply_markup=user_keyboard()
        )


async def message_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = update.message.text

    await update.message.reply_text(
        f"আপনি নির্বাচন করেছেন:\n\n{text}\n\nএই ফিচারটি পরবর্তী ধাপে যুক্ত করা হবে।"
    )
