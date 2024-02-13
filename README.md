# Movie-Info-Bot
Movie Info Bot is a Telegram bot that allows you to search for movies using the [OMDb API](https://www.omdbapi.com/apikey.aspx). You can send a movie title or a phrase to the bot and get a list of related movies. You can also select a movie from the list and get more details about it, such as the IMDB rating, the plot, the genre, the actors, and the poster.

## Installation

To install and run Movie Info Bot, you need:

- Python 3.6 or higher

- The [python-telegram-bot==13.1] library

- An [OMDb API key]

- A [Telegram bot token]

> [!IMPORTANT]
> You can install the requirements using pip:
> 
> `pip install -r requirements.txt`

You can get an OMDb API key from [OMDb API](https://www.omdbapi.com/apikey.aspx). You need to register with your email. Then, you will receive a key in your inbox.

You can get a Telegram bot token from [Bot Father](https://t.me/BotFather). It would help if you created a new bot.  Then you will receive a token.

Alternatively, you can edit the `api_key` and `token variables` in the code and assign them your keys directly.

## Usage
To start the bot, run the following command:

`python movie_info_bot.py`

Then, you can open Telegram and search for your bot by its username. You can start a conversation with the bot by sending the `/start `command. The bot will greet you and ask you to send a movie title or a phrase. For example, you can send "Star Wars" or "romantic comedy". The bot will reply with a list of movies related to your query and their titles, years, and numbers. You can then enter the number of the movie you want to get more details about. The bot will reply with the movie’s IMDB rating, plot, genre, director, writer, actors, language, country, awards, and poster.

## Contributing
If you want to contribute to this project, you can:

Report bugs or suggest features by opening an issue on GitHub.
Fork the repository and make your changes. You can then submit a pull request for review.
Share your feedback or ideas on how to improve the bot.

## License
This project is licensed under the MIT License. Please take a look at the [LICENSE](https://github.com/4prince8/Movie-Info-Bot/blob/main/LICENSE) file for more details.
