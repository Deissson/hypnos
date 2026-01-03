# Hypnos - Remote PC Management Bot

Hypnos is a Python-based Telegram bot designed to allow you to remotely control your Windows PC. Whether you need to shut down your system, turn off the display, or run custom scenarios (like opening a set of applications), Hypnos puts control at your fingertips.

## Features

*   **System Control**: Remotely **Shutdown** or **Restart** your computer with confirmation prompts to prevent accidental actions.
*   **Display Control**: Turn off your connected monitors to save power or reduce glare.
*   **Scenario Execution**: Run predefined workflow scenarios defined in JSON. Great for setting up your environment (e.g., launching work apps or starting a game).
*   **Secure Access**: Restrict bot usage to a specific Telegram User ID to prevent unauthorized access.

## Requirements

*   **OS**: Windows (Primary support for system commands like display control).
*   **Python**: 3.8+ recommended.

## Installation

1.  **Clone the repository:**
    ```bash
    git clone https://github.com/yourusername/hypnos.git
    cd hypnos
    ```

2.  **Install dependencies:**
    ```bash
    pip install -r requirements.txt
    ```

## Configuration

Hypnos uses a simple JSON file for configuration.

1.  Navigate to the `config` directory.
2.  Open or create `config.json`.
3.  Fill in your details:

```json
{
    "bot_token": "YOUR_TELEGRAM_BOT_TOKEN",
    "allowed_user_id": 123456789
}
```

*   **bot_token**: Get this from [BotFather](https://t.me/BotFather) on Telegram.
*   **allowed_user_id**: Your unique Telegram User ID. You can find this using bots like `@userinfobot`. Set to `0` or remove the check in code if you want to bypass this (not recommended).

## Scenarios

Scenarios allow you to execute custom shell commands. Files are located in the `scenarios/` directory.

To create a new scenario, add a `.json` file in `scenarios/` with the following format:

```json
{
    "name": "My Custom Workflow",
    "steps": [
        {
            "action": "run",
            "command": "notepad.exe"
        },
        {
            "action": "run",
            "command": "start chrome https://google.com"
        }
    ]
}
```

## Usage

1.  **Start the bot:**
    ```bash
    python main.py
    ```

2.  **Open Telegram:**
    Start a chat with your bot. If your User ID matches the configuration, you will see the main menu.

3.  **Interact:**
    *   Click **Shutdown** / **Restart** for power options.
    *   Click **Display Off** to kill the lights.
    *   Click **Scenarios** to see a list of your JSON scenarios and run them.

## License

[MIT License](LICENSE)
