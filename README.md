# Discord Self-Bot Spambot

> **Warning:** Self-bots are against Discord's Terms of Service. Using this bot can result in account termination. This project is for educational purposes only.

## Features
- Runs MULTIPLE Discord accounts as self-bots
- Sends random spam messages to a specified channel
- Minimal debugging to show when and why accounts stop

## Requirements
- Python 3.8+
- `discord.py-self` (see [requirements.txt](requirements.txt))

## Setup
1. **Clone the repository:**
   ```sh
   git clone https://github.com/yourusername/Discord-Spambot-main.git
   cd Discord-Spambot-main
   ```
2. **Install dependencies:**
   ```sh
   pip install -r requirements.txt
   ```
3. **Configure accounts:**
   - Open `config.py` and add your Discord account tokens and channel IDs:
     ```python
     accounts = [
         {
             'token': 'YOUR_DISCORD_TOKEN',
             'OwnerId': 'YOUR_USER_ID',
             'GuildId': 'YOUR_GUILD_ID',
             'SpamId': 'CHANNEL_ID_TO_SPAM',
             'sleep': False
         },
         # Add more accounts as needed
     ]
     ```

## Usage
Run the bot with:
```sh
python main.py
```

- The bot will log in with each account and start spamming the specified channel.
- Console output will show when accounts disconnect or encounter errors.

## Debugging
- The bot prints simple messages with timestamps when accounts stop or encounter errors (e.g., invalid token, permission denied, channel not found).

## Disclaimer
- **This code is for educational purposes only.**
- Using self-bots on Discord is strictly prohibited and can result in permanent account bans.
- The author is not responsible for any misuse or account bans resulting from this code.
