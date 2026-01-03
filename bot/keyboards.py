from telegram import InlineKeyboardButton, InlineKeyboardMarkup, WebAppInfo

def main_menu_keyboard():
    keyboard = [
        [
            InlineKeyboardButton("🔒 Shutdown", callback_data='shutdown'),
            InlineKeyboardButton("🔄 Restart", callback_data='restart')
        ],
        [
            InlineKeyboardButton("🖥️ Turn Off Display", callback_data='display_off')
        ],
        [
            InlineKeyboardButton("▶️ Scenarios", callback_data='scenarios_menu')
        ]
    ]
    return InlineKeyboardMarkup(keyboard)

def scenarios_keyboard(scenario_names):
    keyboard = []
    # Create a button for each scenario
    for name in scenario_names:
        keyboard.append([InlineKeyboardButton(f"📜 {name}", callback_data=f'run_scenario_{name}')])
    
    keyboard.append([InlineKeyboardButton("🔙 Back", callback_data='main_menu')])
    return InlineKeyboardMarkup(keyboard)

def confirm_shutdown_keyboard():
    keyboard = [
        [
            InlineKeyboardButton("✅ Yes, Shutdown", callback_data='confirm_shutdown'),
            InlineKeyboardButton("❌ Cancel", callback_data='main_menu')
        ]
    ]
    return InlineKeyboardMarkup(keyboard)

def confirm_restart_keyboard():
    keyboard = [
        [
            InlineKeyboardButton("✅ Yes, Restart", callback_data='confirm_restart'),
            InlineKeyboardButton("❌ Cancel", callback_data='main_menu')
        ]
    ]
    return InlineKeyboardMarkup(keyboard)
