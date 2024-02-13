import logging
from telegram import Update
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackContext
import requests

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)


def start(update: Update, context: CallbackContext) -> None:
    update.message.reply_text(
        "Hello!😎 I'm your movie info bot. Send me a movie title or a phrase to get a list of related movies.")


def movie_info(update: Update, context: CallbackContext) -> None:
    try:
        query = update.message.text
        api_key = 'YOUR_API_KEY'
        base_url = 'http://www.omdbapi.com/'
        params = {'apikey': api_key, 's': query}
        response = requests.get(base_url, params=params)
        response_data = response.json()
        if response_data['Response'] == 'True':
            movies = response_data['Search']
            movie_list = ""
            movie_ids = {}
            for i, movie in enumerate(movies):
                movie_list += f"🎬 {i + 1}. {movie['Title']} ({movie['Year']})\n"
                movie_ids[i + 1] = movie['imdbID']
            context.user_data['movie_ids'] = movie_ids
            update.message.reply_text(
                f"✅ Here are some movies related to '{query}':\n\n{movie_list}\n🔢 Please enter the number of the movie you want to get more details.")
        else:
            update.message.reply_text(
                f"Sorry!😥 I could not find any movies related to '{query}'. Please try another query.")
    except Exception as e:
        update.message.reply_text(f"An error occurred: {str(e)}")


def movie_details(update: Update, context: CallbackContext) -> None:
    try:
        movie_number = int(update.message.text)
        movie_ids = context.user_data.get('movie_ids')
        if movie_ids and movie_number in movie_ids:
            imdb_id = movie_ids[movie_number]
            api_key = 'YOUR_API_KEY'
            base_url = 'http://www.omdbapi.com/'
            params = {'apikey': api_key, 'i': imdb_id, 'plot': 'full'}
            response = requests.get(base_url, params=params)
            response_data = response.json()
            if response_data['Response'] == 'True':
                movie_data = response_data
                response = f"Title: {movie_data['Title']}\n\n"
                response += f"IMDB rating: {movie_data['imdbRating']}\n\n"
                response += f"Year: {movie_data['Year']}\n\n"
                response += f"Released: {movie_data['Released']}\n\n"
                response += f"Runtime: {movie_data['Runtime']}\n\n"
                response += f"Genre: {movie_data['Genre']}\n\n"
                response += f"Director: {movie_data['Director']}\n\n"
                response += f"Writer: {movie_data['Writer']}\n\n"
                response += f"Actors: {movie_data['Actors']}\n\n"
                response += f"Released: {movie_data['Released']}\n\n"
                response += f"Language: {movie_data['Language']}\n\n"
                response += f"Country: {movie_data['Country']}\n\n"
                response += f"Awards: {movie_data['Awards']}\n\n"
                response += f"Plot: {movie_data['Plot']}\n\n"
                response += f"Poster: {movie_data['Poster']}\n\n"

                update.message.reply_text(response)
            else:
                update.message.reply_text(
                    f"Sorry!😥 I could not find any movie with the imdbID '{imdb_id}'. Please try another imdbID.")
        else:
            update.message.reply_text(
                f"Sorry😥, I could not find any movie with the number '{movie_number}'. Please enter a valid number "
                f"from the list.")
    except Exception as e:
        update.message.reply_text(f"An error occurred: {str(e)}")


def main() -> None:
    updater = Updater("YOUR_BOT_TOKEN")
    dispatcher = updater.dispatcher

    dispatcher.add_handler(CommandHandler("start", start))
    dispatcher.add_handler(MessageHandler(Filters.regex(r'^\d+$') & ~Filters.command, movie_details))
    dispatcher.add_handler(MessageHandler(Filters.text & ~Filters.command, movie_info))

    updater.start_polling()
    updater.idle()


if __name__ == '__main__':
    main()
