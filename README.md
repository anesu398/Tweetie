# Twitter Bot

This project is a Python-based Twitter bot that provides basic automation functionalities such as posting tweets, liking tweets, and performing sentiment analysis on tweets.

## Features

- **Post Tweets**: Post tweets automatically using the provided text.
- **Like Tweets**: Like tweets containing a specific keyword.
- **Sentiment Analysis**: Analyze the sentiment of a tweet using TextBlob.

## Installation

1. Clone the repository:

    ```bash
    git clone https://github.com/your_username/twitter-bot.git
    ```

2. Install dependencies:

    ```bash
    cd twitter-bot
    pip install -r requirements.txt
    ```

3. Set up Twitter API credentials in `config.py`:

    ```python
    consumer_key = 'YOUR_CONSUMER_KEY'
    consumer_secret = 'YOUR_CONSUMER_SECRET'
    access_token = 'YOUR_ACCESS_TOKEN'
    access_token_secret = 'YOUR_ACCESS_TOKEN_SECRET'
    ```

## Usage

1. Post a tweet:

    ```bash
    python bot.py post "Your tweet text here."
    ```

2. Like tweets containing a keyword:

    ```bash
    python bot.py like "keyword"
    ```

3. Perform sentiment analysis on a tweet:

    ```bash
    python bot.py analyze "Tweet text here."
    ```

## Contributing

Contributions are welcome! If you have any suggestions or find any issues, please open an issue or submit a pull request.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
