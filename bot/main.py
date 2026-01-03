import logging
import json
import os
from telegram.ext import ApplicationBuilder, CommandHandler, CallbackQueryHandler
from bot.handlers import start, button_handler

# Setup logging
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)

def main():
    # Load config
    config_path = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'config', 'config.json')
    try:
        with open(config_path, 'r') as f:
            config = json.load(f)
    except FileNotFoundError:
        print("Config file not found. Please create config/config.json")
        return

    token = config.get('bot_token')
    if not token or token == "YOUR_BOT_TOKEN_HERE":
        print("Error: Bot token not set in config/config.json")
        return

    application = ApplicationBuilder().token(token).build()

    application.add_handler(CommandHandler('start', start))
    application.add_handler(CallbackQueryHandler(button_handler))

    print("Bot is running...")
    application.run_polling()

if __name__ == '__main__':
    main()
