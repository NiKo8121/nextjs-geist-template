import os
import logging
import requests
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes, MessageHandler, filters

# Enable logging
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)
logger = logging.getLogger(__name__)

# Movie API configuration
TMDB_API_KEY = os.getenv('TMDB_API_KEY')
TMDB_SEARCH_URL = "https://api.themoviedb.org/3/search/movie"
TMDB_IMAGE_BASE_URL = "https://image.tmdb.org/t/p/w500"

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text(
        "Hi! Send me the name of a movie, and I'll find it for you."
    )

async def search_movie(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    query = update.message.text
    if not query:
        await update.message.reply_text("Please send a movie name to search.")
        return

    params = {
        "api_key": TMDB_API_KEY,
        "query": query,
        "language": "en-US",
        "page": 1,
        "include_adult": False,
    }
    response = requests.get(TMDB_SEARCH_URL, params=params)
    if response.status_code != 200:
        await update.message.reply_text("Sorry, I couldn't reach the movie database.")
        return

    data = response.json()
    results = data.get("results", [])
    if not results:
        await update.message.reply_text("No movies found with that name.")
        return

    # Show top 3 results
    movies = results[:3]
    for movie in movies:
        title = movie.get("title")
        overview = movie.get("overview", "No description available.")
        release_date = movie.get("release_date", "Unknown")
        poster_path = movie.get("poster_path")
        poster_url = TMDB_IMAGE_BASE_URL + poster_path if poster_path else None

        message = f"*{title}* ({release_date})\n\n{overview}"
        if poster_url:
            await update.message.reply_photo(photo=poster_url, caption=message, parse_mode='Markdown')
        else:
            await update.message.reply_text(message, parse_mode='Markdown')

async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text("Send me a movie name to search for movies.")

def main() -> None:
    token = os.getenv("8021991641:AAEHV5nETZ-VCuDkHNP3ATv7jsNkbzdLF3A")
    if not token:
        logger.error("8021991641:AAEHV5nETZ-VCuDkHNP3ATv7jsNkbzdLF3A")
        return
    if not TMDB_API_KEY:
        logger.error("http://www.omdbapi.com/?i=tt3896198&apikey=8b6e8a8b")
        return

    application = ApplicationBuilder().token(token).build()

    application.add_handler(CommandHandler("start", start))
    application.add_handler(CommandHandler("help", help_command))
    application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, search_movie))

    logger.info("Bot started")
    application.run_polling()

if __name__ == "__main__":
    main()
