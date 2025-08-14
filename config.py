# Twitter Auto Configuration
# Replace these values with your actual Twitter credentials

# Twitter Authentication
AUTH_TOKEN = "YOUR_AUTH_TOKEN_HERE"  # Get this from browser cookies
CSRF_TOKEN = "YOUR_CSRF_TOKEN_HERE"  # Optional, will be fetched automatically

# Auto Like Settings
AUTO_LIKE_KEYWORDS = [
    "python",
    "programming", 
    "coding",
    "developer",
    "tech",
    "software"
]

AUTO_LIKE_COUNT = 10  # Number of tweets to like per keyword
AUTO_LIKE_DELAY = (30, 60)  # Delay range in seconds between likes

# Auto Retweet Settings
AUTO_RETWEET_KEYWORDS = [
    "python",
    "programming",
    "coding"
]

AUTO_RETWEET_COUNT = 5  # Number of tweets to retweet per keyword
AUTO_RETWEET_DELAY = (60, 120)  # Delay range in seconds between retweets

# Auto Reply Settings
AUTO_REPLY_KEYWORDS = [
    "python",
    "programming"
]

AUTO_REPLY_MESSAGES = [
    "Great post! 👍",
    "Thanks for sharing! 🙏", 
    "Interesting perspective! 🤔",
    "Love this content! ❤️",
    "Awesome! 🔥",
    "Thanks for the info! 📚",
    "Great insights! 💡",
    "Keep it up! 🚀"
]

AUTO_REPLY_COUNT = 3  # Number of tweets to reply to per keyword
AUTO_REPLY_DELAY = (120, 180)  # Delay range in seconds between replies

# General Settings
ENABLE_LOGGING = True
LOG_LEVEL = "INFO"  # DEBUG, INFO, WARNING, ERROR
LOG_FILE = "twitter_auto.log"

# Safety Settings
MAX_ACTIONS_PER_HOUR = 50  # Maximum actions (like/retweet/reply) per hour
SAFETY_DELAY = True  # Enable random delays between actions
MIN_DELAY = 30  # Minimum delay in seconds
MAX_DELAY = 180  # Maximum delay in seconds

# Search Settings
SEARCH_RESULT_TYPE = "recent"  # recent, popular, mixed
MAX_SEARCH_RESULTS = 100  # Maximum tweets to search per query