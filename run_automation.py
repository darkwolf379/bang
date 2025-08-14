#!/usr/bin/env python3
"""
Continuous Twitter Automation Script
Menjalankan auto like, retweet, dan reply secara berkelanjutan
"""

from twitter_auto import TwitterAuto
from config import *
import time
import random
import logging
from datetime import datetime, timedelta

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler('automation.log'),
        logging.StreamHandler()
    ]
)
logger = logging.getLogger(__name__)

class TwitterAutomation:
    def __init__(self):
        """Initialize Twitter automation"""
        self.twitter = TwitterAuto(AUTH_TOKEN, CSRF_TOKEN)
        self.action_count = 0
        self.last_reset = datetime.now()
        
        if not self.twitter.csrf_token:
            logger.error("Failed to initialize Twitter Auto. Check your auth_token.")
            raise Exception("Twitter initialization failed")
        
        logger.info("Twitter Automation initialized successfully!")
    
    def check_rate_limit(self):
        """Check if we're within rate limits"""
        now = datetime.now()
        
        # Reset counter every hour
        if now - self.last_reset > timedelta(hours=1):
            self.action_count = 0
            self.last_reset = now
            logger.info("Rate limit counter reset")
        
        # Check if we're over the limit
        if self.action_count >= MAX_ACTIONS_PER_HOUR:
            wait_time = 3600 - (now - self.last_reset).seconds
            logger.warning(f"Rate limit reached. Waiting {wait_time} seconds...")
            time.sleep(wait_time)
            self.action_count = 0
            self.last_reset = datetime.now()
    
    def run_auto_like(self):
        """Run auto like automation"""
        try:
            logger.info("Starting auto like automation...")
            self.check_rate_limit()
            
            self.twitter.auto_like_by_keyword(
                keywords=AUTO_LIKE_KEYWORDS,
                count=AUTO_LIKE_COUNT,
                delay_range=AUTO_LIKE_DELAY
            )
            
            self.action_count += len(AUTO_LIKE_KEYWORDS) * AUTO_LIKE_COUNT
            logger.info("Auto like automation completed!")
            
        except Exception as e:
            logger.error(f"Error in auto like: {e}")
    
    def run_auto_retweet(self):
        """Run auto retweet automation"""
        try:
            logger.info("Starting auto retweet automation...")
            self.check_rate_limit()
            
            self.twitter.auto_retweet_by_keyword(
                keywords=AUTO_RETWEET_KEYWORDS,
                count=AUTO_RETWEET_COUNT,
                delay_range=AUTO_RETWEET_DELAY
            )
            
            self.action_count += len(AUTO_RETWEET_KEYWORDS) * AUTO_RETWEET_COUNT
            logger.info("Auto retweet automation completed!")
            
        except Exception as e:
            logger.error(f"Error in auto retweet: {e}")
    
    def run_auto_reply(self):
        """Run auto reply automation"""
        try:
            logger.info("Starting auto reply automation...")
            self.check_rate_limit()
            
            self.twitter.auto_reply_by_keyword(
                keywords=AUTO_REPLY_KEYWORDS,
                replies=AUTO_REPLY_MESSAGES,
                count=AUTO_REPLY_COUNT,
                delay_range=AUTO_REPLY_DELAY
            )
            
            self.action_count += len(AUTO_REPLY_KEYWORDS) * AUTO_REPLY_COUNT
            logger.info("Auto reply automation completed!")
            
        except Exception as e:
            logger.error(f"Error in auto reply: {e}")
    
    def post_scheduled_tweet(self):
        """Post a scheduled tweet"""
        try:
            logger.info("Posting scheduled tweet...")
            self.check_rate_limit()
            
            # Example scheduled tweets
            scheduled_tweets = [
                "Good morning Twitter! ☀️ Starting my day with some automation. #GoodMorning",
                "Happy coding everyone! 💻 Keep learning and growing. #Programming #Coding",
                "Just finished a great coding session! 🚀 What are you working on today? #DeveloperLife",
                "Automation is the future! 🤖 Making life easier one script at a time. #Automation",
                "Time for a coffee break! ☕️ Perfect time to check Twitter. #CoffeeTime"
            ]
            
            tweet_text = random.choice(scheduled_tweets)
            result = self.twitter.post_tweet(tweet_text)
            
            if result:
                self.action_count += 1
                logger.info(f"Scheduled tweet posted: {tweet_text}")
            else:
                logger.error("Failed to post scheduled tweet")
                
        except Exception as e:
            logger.error(f"Error posting scheduled tweet: {e}")
    
    def run_cycle(self):
        """Run one complete automation cycle"""
        logger.info("=" * 50)
        logger.info("Starting automation cycle...")
        logger.info("=" * 50)
        
        try:
            # Run different automation tasks
            self.run_auto_like()
            time.sleep(random.uniform(300, 600))  # Wait 5-10 minutes
            
            self.run_auto_retweet()
            time.sleep(random.uniform(300, 600))  # Wait 5-10 minutes
            
            self.run_auto_reply()
            time.sleep(random.uniform(300, 600))  # Wait 5-10 minutes
            
            # Post a scheduled tweet occasionally
            if random.random() < 0.3:  # 30% chance
                self.post_scheduled_tweet()
            
            logger.info("Automation cycle completed!")
            logger.info(f"Actions performed this hour: {self.action_count}/{MAX_ACTIONS_PER_HOUR}")
            
        except Exception as e:
            logger.error(f"Error in automation cycle: {e}")
    
    def run_continuous(self, cycle_interval_hours=2):
        """Run automation continuously"""
        logger.info(f"Starting continuous automation (cycle every {cycle_interval_hours} hours)")
        logger.info("Press Ctrl+C to stop")
        
        cycle_count = 0
        
        try:
            while True:
                cycle_count += 1
                logger.info(f"Cycle #{cycle_count}")
                
                self.run_cycle()
                
                # Wait before next cycle
                wait_time = cycle_interval_hours * 3600  # Convert to seconds
                logger.info(f"Waiting {cycle_interval_hours} hours before next cycle...")
                time.sleep(wait_time)
                
        except KeyboardInterrupt:
            logger.info("Automation stopped by user")
        except Exception as e:
            logger.error(f"Automation error: {e}")

def main():
    """Main function"""
    print("🤖 Twitter Continuous Automation")
    print("=" * 40)
    
    # Check if credentials are set
    if AUTH_TOKEN == "YOUR_AUTH_TOKEN_HERE":
        print("❌ Please set your AUTH_TOKEN in config.py first!")
        print("💡 Run: python get_auth_token.py for help")
        return
    
    try:
        # Initialize automation
        automation = TwitterAutomation()
        
        # Ask user for cycle interval
        print("\n⏰ Automation Settings:")
        print("1. Run once")
        print("2. Run continuously (every 2 hours)")
        print("3. Run continuously (custom interval)")
        
        choice = input("\nPilih opsi (1-3): ").strip()
        
        if choice == "1":
            print("\n🚀 Running single cycle...")
            automation.run_cycle()
            print("✅ Single cycle completed!")
            
        elif choice == "2":
            print("\n🔄 Starting continuous automation (2-hour cycles)...")
            automation.run_continuous(cycle_interval_hours=2)
            
        elif choice == "3":
            try:
                hours = float(input("Masukkan interval dalam jam: "))
                print(f"\n🔄 Starting continuous automation ({hours}-hour cycles)...")
                automation.run_continuous(cycle_interval_hours=hours)
            except ValueError:
                print("❌ Invalid input. Using 2-hour default.")
                automation.run_continuous(cycle_interval_hours=2)
        
        else:
            print("❌ Invalid choice. Exiting.")
            
    except Exception as e:
        print(f"❌ Error: {e}")
        logger.error(f"Main error: {e}")

if __name__ == "__main__":
    main()