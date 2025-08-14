#!/usr/bin/env python3
"""
Example Usage Scripts for Twitter Auto
Demonstrates different ways to use the Twitter automation features
"""

from twitter_auto import TwitterAuto
from config import *
import time
import random

def example_basic_usage():
    """Basic usage examples"""
    print("=== Basic Usage Examples ===")
    
    # Initialize Twitter Auto
    twitter = TwitterAuto(AUTH_TOKEN, CSRF_TOKEN)
    
    if not twitter.csrf_token:
        print("❌ Failed to initialize Twitter Auto. Check your auth_token.")
        return
    
    print("✅ Twitter Auto initialized successfully!")
    
    # Example 1: Post a simple tweet
    print("\n1. Posting a tweet...")
    result = twitter.post_tweet("Hello Twitter! This is an automated tweet using API v1. 🤖 #Python #Automation")
    if result:
        print(f"✅ Tweet posted successfully! ID: {result.get('id_str')}")
    else:
        print("❌ Failed to post tweet")
    
    # Example 2: Like a specific tweet
    print("\n2. Liking a tweet...")
    # Replace with actual tweet ID
    tweet_id = "1234567890123456789"  # Example tweet ID
    if twitter.like_tweet(tweet_id):
        print(f"✅ Tweet {tweet_id} liked successfully!")
    else:
        print(f"❌ Failed to like tweet {tweet_id}")
    
    # Example 3: Retweet a specific tweet
    print("\n3. Retweeting a tweet...")
    if twitter.retweet(tweet_id):
        print(f"✅ Tweet {tweet_id} retweeted successfully!")
    else:
        print(f"❌ Failed to retweet {tweet_id}")
    
    # Example 4: Reply to a tweet
    print("\n4. Replying to a tweet...")
    reply_result = twitter.reply_to_tweet(tweet_id, "Great post! Thanks for sharing! 👍")
    if reply_result:
        print(f"✅ Reply posted successfully! ID: {reply_result.get('id_str')}")
    else:
        print("❌ Failed to post reply")

def example_auto_like():
    """Example of auto like functionality"""
    print("\n=== Auto Like Example ===")
    
    twitter = TwitterAuto(AUTH_TOKEN, CSRF_TOKEN)
    
    if not twitter.csrf_token:
        print("❌ Failed to initialize Twitter Auto.")
        return
    
    # Auto like tweets with specific keywords
    keywords = ["python", "programming", "coding"]
    print(f"🔍 Searching and liking tweets with keywords: {keywords}")
    
    twitter.auto_like_by_keyword(
        keywords=keywords,
        count=5,  # Like 5 tweets per keyword
        delay_range=(30, 60)  # Wait 30-60 seconds between likes
    )
    
    print("✅ Auto like completed!")

def example_auto_retweet():
    """Example of auto retweet functionality"""
    print("\n=== Auto Retweet Example ===")
    
    twitter = TwitterAuto(AUTH_TOKEN, CSRF_TOKEN)
    
    if not twitter.csrf_token:
        print("❌ Failed to initialize Twitter Auto.")
        return
    
    # Auto retweet tweets with specific keywords
    keywords = ["python", "programming"]
    print(f"🔍 Searching and retweeting tweets with keywords: {keywords}")
    
    twitter.auto_retweet_by_keyword(
        keywords=keywords,
        count=3,  # Retweet 3 tweets per keyword
        delay_range=(60, 120)  # Wait 60-120 seconds between retweets
    )
    
    print("✅ Auto retweet completed!")

def example_auto_reply():
    """Example of auto reply functionality"""
    print("\n=== Auto Reply Example ===")
    
    twitter = TwitterAuto(AUTH_TOKEN, CSRF_TOKEN)
    
    if not twitter.csrf_token:
        print("❌ Failed to initialize Twitter Auto.")
        return
    
    # Auto reply to tweets with specific keywords
    keywords = ["python", "programming"]
    replies = [
        "Great post! 👍",
        "Thanks for sharing! 🙏",
        "Interesting perspective! 🤔",
        "Love this content! ❤️"
    ]
    
    print(f"🔍 Searching and replying to tweets with keywords: {keywords}")
    
    twitter.auto_reply_by_keyword(
        keywords=keywords,
        replies=replies,
        count=2,  # Reply to 2 tweets per keyword
        delay_range=(120, 180)  # Wait 120-180 seconds between replies
    )
    
    print("✅ Auto reply completed!")

def example_search_and_analyze():
    """Example of searching tweets and analyzing them"""
    print("\n=== Search and Analyze Example ===")
    
    twitter = TwitterAuto(AUTH_TOKEN, CSRF_TOKEN)
    
    if not twitter.csrf_token:
        print("❌ Failed to initialize Twitter Auto.")
        return
    
    # Search for tweets
    query = "python programming"
    print(f"🔍 Searching for tweets with query: '{query}'")
    
    tweets = twitter.search_tweets(query, count=10, result_type='recent')
    
    if tweets:
        print(f"📊 Found {len(tweets)} tweets:")
        
        for i, tweet in enumerate(tweets[:5], 1):  # Show first 5 tweets
            user = tweet.get('user', {}).get('screen_name', 'Unknown')
            text = tweet.get('full_text', tweet.get('text', ''))[:100] + "..."
            tweet_id = tweet.get('id_str')
            
            print(f"{i}. @{user}: {text}")
            print(f"   Tweet ID: {tweet_id}")
            print(f"   Likes: {tweet.get('favorite_count', 0)}, Retweets: {tweet.get('retweet_count', 0)}")
            print()
    else:
        print("❌ No tweets found")

def example_user_timeline():
    """Example of getting user timeline"""
    print("\n=== User Timeline Example ===")
    
    twitter = TwitterAuto(AUTH_TOKEN, CSRF_TOKEN)
    
    if not twitter.csrf_token:
        print("❌ Failed to initialize Twitter Auto.")
        return
    
    # Get your own timeline
    print("📱 Getting your timeline...")
    timeline = twitter.get_user_timeline(count=5)
    
    if timeline:
        print(f"📊 Found {len(timeline)} tweets in your timeline:")
        
        for i, tweet in enumerate(timeline, 1):
            text = tweet.get('full_text', tweet.get('text', ''))[:100] + "..."
            tweet_id = tweet.get('id_str')
            created_at = tweet.get('created_at', 'Unknown')
            
            print(f"{i}. {text}")
            print(f"   Tweet ID: {tweet_id}")
            print(f"   Created: {created_at}")
            print()
    else:
        print("❌ Failed to get timeline")

def example_scheduled_actions():
    """Example of running scheduled actions"""
    print("\n=== Scheduled Actions Example ===")
    
    twitter = TwitterAuto(AUTH_TOKEN, CSRF_TOKEN)
    
    if not twitter.csrf_token:
        print("❌ Failed to initialize Twitter Auto.")
        return
    
    # Run different actions with delays
    print("⏰ Running scheduled actions...")
    
    # Action 1: Post a tweet
    print("1. Posting scheduled tweet...")
    twitter.post_tweet("Good morning Twitter! Starting my day with some automation. ☀️ #GoodMorning")
    time.sleep(random.uniform(60, 120))
    
    # Action 2: Auto like some tweets
    print("2. Auto liking tweets...")
    twitter.auto_like_by_keyword(["python", "coding"], count=3, delay_range=(30, 60))
    time.sleep(random.uniform(120, 180))
    
    # Action 3: Auto retweet some tweets
    print("3. Auto retweeting tweets...")
    twitter.auto_retweet_by_keyword(["programming"], count=2, delay_range=(60, 90))
    
    print("✅ Scheduled actions completed!")

def main():
    """Main function to run examples"""
    print("🚀 Twitter Auto Examples")
    print("=" * 50)
    
    # Check if credentials are set
    if AUTH_TOKEN == "YOUR_AUTH_TOKEN_HERE":
        print("❌ Please set your AUTH_TOKEN in config.py first!")
        print("📝 To get your auth_token:")
        print("   1. Go to Twitter.com and log in")
        print("   2. Open Developer Tools (F12)")
        print("   3. Go to Application/Storage > Cookies > twitter.com")
        print("   4. Find 'auth_token' and copy its value")
        print("   5. Paste it in config.py")
        return
    
    # Run examples
    try:
        example_basic_usage()
        time.sleep(2)
        
        example_search_and_analyze()
        time.sleep(2)
        
        example_user_timeline()
        time.sleep(2)
        
        # Uncomment the following lines to run automation examples
        # (Be careful with these as they perform actual actions)
        
        # example_auto_like()
        # time.sleep(2)
        
        # example_auto_retweet()
        # time.sleep(2)
        
        # example_auto_reply()
        # time.sleep(2)
        
        # example_scheduled_actions()
        
    except KeyboardInterrupt:
        print("\n⏹️  Examples interrupted by user")
    except Exception as e:
        print(f"❌ Error running examples: {e}")

if __name__ == "__main__":
    main()