from telegram import Update
from telegram.ext import ContextTypes

from config import ADMIN_ID
from database import get_users


def is_admin(user_id: int) -> bool:
    return user_id == ADMIN_ID


async def admin_panel(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if not is_admin(update.effective_user.id):
        await update.message.reply_text("❌ Access Denied")
        return

    await update.message.reply_text(
        """👑 ADMIN PANEL

👥 Total Users
📢 Broadcast
📥 Add Number
📋 View Numbers
🗑 Delete Number
➕ Add Service
✏️ Edit Service
❌ Delete Service
📊 Statistics
⚙️ Settings"""
    )


async def total_users(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if not is_admin(update.effective_user.id):
        return

    users = get_users()

    await update.message.reply_text(
        f"👥 Total Users: {len(users)}"
    )


async def add_number(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if not is_admin(update.effective_user.id):
        return

    await update.message.reply_text(
        "📥 Send a .txt or .csv file to import numbers.\n\n(Feature will be added next.)"
    )


async def broadcast(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if not is_admin(update.effective_user.id):
        return

    await update.message.reply_text(
        "📢 Broadcast feature will be added in the next step."
    )


async def statistics(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if not is_admin(update.effective_user.id):
        return

    users = get_users()

    await update.message.reply_text(
        f"""📊 BOT STATISTICS

👥 Users : {len(users)}
🟢 Bot Status : Online
👑 Admin : Active"""
    )
