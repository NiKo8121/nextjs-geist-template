# Telegram Movie Bot

This is a Telegram chatbot implemented in Python that allows users to search for movies and get details using The Movie Database (TMDb) API.

## Setup

1. Clone the repository or copy the `telegram-bot-python` directory.

2. Install dependencies:

```bash
pip install -r requirements.txt
```

3. Get a Telegram bot token by creating a bot with [BotFather](https://t.me/BotFather) on Telegram.

4. Get a TMDb API key by creating an account and requesting an API key at [TMDb](https://www.themoviedb.org/documentation/api).

5. Set environment variables:

```bash
export TELEGRAM_BOT_TOKEN="your-telegram-bot-token"
export TMDB_API_KEY="your-tmdb-api-key"
```

6. Run the bot:

```bash
python bot.py
```

## Usage

- Start the bot by sending `/start`.
- Send any movie name to search for movies.
- Use `/help` to get help information.

## Notes

- The bot returns the top 3 matching movies with their poster images and descriptions.
- Make sure your environment variables are set correctly before running the bot.
