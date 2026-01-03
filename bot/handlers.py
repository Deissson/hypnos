import logging
import json
import os
from telegram import Update
from telegram.ext import ContextTypes, ConversationHandler
from bot.keyboards import main_menu_keyboard, scenarios_keyboard, confirm_shutdown_keyboard, confirm_restart_keyboard
from core.system import shutdown, restart, turn_off_display
from core.runner import get_scenarios, execute_scenario

# Load config
CONFIG_PATH = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'config', 'config.json')
with open(CONFIG_PATH, 'r') as f:
    config = json.load(f)

ALLOWED_USER_ID = config.get('allowed_user_id')

logger = logging.getLogger(__name__)

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_id = update.effective_user.id
    if ALLOWED_USER_ID and user_id != ALLOWED_USER_ID:
        await update.message.reply_text("⛔ Unauthorized access.")
        return

    await update.message.reply_text(
        "👋 Welcome to Hypnos Remote Management.\nSelect an action:",
        reply_markup=main_menu_keyboard()
    )

async def button_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()

    user_id = update.effective_user.id
    if ALLOWED_USER_ID and user_id != ALLOWED_USER_ID:
        await query.edit_message_text("⛔ Unauthorized access.")
        return

    data = query.data

    if data == 'main_menu':
        await query.edit_message_text(
            "👋 Main Menu\nSelect an action:",
            reply_markup=main_menu_keyboard()
        )

    elif data == 'shutdown':
        await query.edit_message_text(
            "⚠️ Are you sure you want to SHUTDOWN the computer?",
            reply_markup=confirm_shutdown_keyboard()
        )

    elif data == 'restart':
        await query.edit_message_text(
            "⚠️ Are you sure you want to RESTART the computer?",
            reply_markup=confirm_restart_keyboard()
        )

    elif data == 'confirm_shutdown':
        await query.edit_message_text("🔌 Shutting down...")
        shutdown()

    elif data == 'confirm_restart':
        await query.edit_message_text("🔄 Restarting...")
        restart()

    elif data == 'display_off':
        await query.edit_message_text("🖥️ Turning off display...", reply_markup=main_menu_keyboard())
        turn_off_display()

    elif data == 'scenarios_menu':
        scenarios = get_scenarios()
        if not scenarios:
            await query.edit_message_text("No scenarios found.", reply_markup=main_menu_keyboard())
        else:
            await query.edit_message_text(
                "📂 Select a scenario to run:",
                reply_markup=scenarios_keyboard(scenarios)
            )

    elif data.startswith('run_scenario_'):
        scenario_name = data.replace('run_scenario_', '')
        await query.edit_message_text(f"▶️ Running scenario: {scenario_name}...")
        result = execute_scenario(scenario_name)
        await query.message.reply_text(f"✅ Result:\n{result}")
        await query.message.reply_text("Back to menu:", reply_markup=main_menu_keyboard())