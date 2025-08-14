#!/usr/bin/env python3
"""
Twitter Auto Script - Using API v1 with Cookie Authentication
Features: Auto Like, Tweet, Reply, Retweet
"""

import requests
import json
import time
import random
import re
from datetime import datetime
from typing import Optional, List, Dict, Any
import logging

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler('twitter_auto.log'),
        logging.StreamHandler()
    ]
)
logger = logging.getLogger(__name__)

class TwitterAuto:
    def __init__(self, auth_token: str, csrf_token: str = None):
        """
        Initialize Twitter Auto with cookie authentication
        
        Args:
            auth_token: Twitter auth_token cookie value
            csrf_token: Twitter csrf token (optional, will be fetched if not provided)
        """
        self.auth_token = auth_token
        self.csrf_token = csrf_token
        self.session = requests.Session()
        self.base_url = "https://api.twitter.com/1.1"
        self.guest_url = "https://api.twitter.com/1.1/guest/activate.json"
        
        # Set up session headers and cookies
        self.session.headers.update({
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36',
            'Accept': 'application/json, text/plain, */*',
            'Accept-Language': 'en-US,en;q=0.9',
            'Accept-Encoding': 'gzip, deflate, br',
            'DNT': '1',
            'Connection': 'keep-alive',
            'Upgrade-Insecure-Requests': '1',
        })
        
        # Set auth cookie
        self.session.cookies.set('auth_token', auth_token, domain='.twitter.com')
        
        # Initialize tokens
        self._initialize_tokens()
    
    def _initialize_tokens(self):
        """Initialize guest token and csrf token"""
        try:
            # Get guest token
            guest_response = self.session.post(self.guest_url)
            if guest_response.status_code == 200:
                guest_data = guest_response.json()
                self.guest_token = guest_data.get('guest_token')
                self.session.headers.update({'x-guest-token': self.guest_token})
                logger.info("Guest token obtained successfully")
            else:
                logger.error(f"Failed to get guest token: {guest_response.status_code}")
                return
            
            # Get csrf token if not provided
            if not self.csrf_token:
                self._get_csrf_token()
            
            logger.info("Tokens initialized successfully")
            
        except Exception as e:
            logger.error(f"Error initializing tokens: {e}")
    
    def _get_csrf_token(self):
        """Get CSRF token from Twitter"""
        try:
            # Visit Twitter home page to get csrf token
            response = self.session.get('https://twitter.com/home')
            if response.status_code == 200:
                # Extract csrf token from HTML
                csrf_match = re.search(r'ct0=([^;]+)', response.text)
                if csrf_match:
                    self.csrf_token = csrf_match.group(1)
                    self.session.headers.update({'x-csrf-token': self.csrf_token})
                    logger.info("CSRF token obtained successfully")
                else:
                    logger.warning("CSRF token not found in response")
            else:
                logger.error(f"Failed to get CSRF token: {response.status_code}")
        except Exception as e:
            logger.error(f"Error getting CSRF token: {e}")
    
    def _make_request(self, method: str, endpoint: str, data: Dict = None, params: Dict = None) -> Optional[Dict]:
        """Make authenticated request to Twitter API"""
        try:
            url = f"{self.base_url}/{endpoint}"
            
            if method.upper() == 'GET':
                response = self.session.get(url, params=params)
            elif method.upper() == 'POST':
                response = self.session.post(url, json=data, params=params)
            else:
                logger.error(f"Unsupported HTTP method: {method}")
                return None
            
            if response.status_code == 200:
                return response.json()
            else:
                logger.error(f"Request failed: {response.status_code} - {response.text}")
                return None
                
        except Exception as e:
            logger.error(f"Request error: {e}")
            return None
    
    def post_tweet(self, text: str, reply_to: str = None) -> Optional[Dict]:
        """
        Post a new tweet
        
        Args:
            text: Tweet content
            reply_to: Tweet ID to reply to (optional)
        
        Returns:
            Tweet data if successful, None otherwise
        """
        try:
            data = {
                'text': text,
                'tweet_mode': 'extended'
            }
            
            if reply_to:
                data['in_reply_to_status_id'] = reply_to
            
            result = self._make_request('POST', 'statuses/update.json', data=data)
            
            if result:
                logger.info(f"Tweet posted successfully: {result.get('id_str')}")
                return result
            else:
                logger.error("Failed to post tweet")
                return None
                
        except Exception as e:
            logger.error(f"Error posting tweet: {e}")
            return None
    
    def like_tweet(self, tweet_id: str) -> bool:
        """
        Like a tweet
        
        Args:
            tweet_id: ID of the tweet to like
        
        Returns:
            True if successful, False otherwise
        """
        try:
            data = {'id': tweet_id}
            result = self._make_request('POST', 'favorites/create.json', data=data)
            
            if result:
                logger.info(f"Tweet {tweet_id} liked successfully")
                return True
            else:
                logger.error(f"Failed to like tweet {tweet_id}")
                return False
                
        except Exception as e:
            logger.error(f"Error liking tweet: {e}")
            return False
    
    def unlike_tweet(self, tweet_id: str) -> bool:
        """
        Unlike a tweet
        
        Args:
            tweet_id: ID of the tweet to unlike
        
        Returns:
            True if successful, False otherwise
        """
        try:
            data = {'id': tweet_id}
            result = self._make_request('POST', 'favorites/destroy.json', data=data)
            
            if result:
                logger.info(f"Tweet {tweet_id} unliked successfully")
                return True
            else:
                logger.error(f"Failed to unlike tweet {tweet_id}")
                return False
                
        except Exception as e:
            logger.error(f"Error unliking tweet: {e}")
            return False
    
    def retweet(self, tweet_id: str) -> bool:
        """
        Retweet a tweet
        
        Args:
            tweet_id: ID of the tweet to retweet
        
        Returns:
            True if successful, False otherwise
        """
        try:
            data = {'id': tweet_id}
            result = self._make_request('POST', 'statuses/retweet.json', data=data)
            
            if result:
                logger.info(f"Tweet {tweet_id} retweeted successfully")
                return True
            else:
                logger.error(f"Failed to retweet {tweet_id}")
                return False
                
        except Exception as e:
            logger.error(f"Error retweeting: {e}")
            return False
    
    def unretweet(self, tweet_id: str) -> bool:
        """
        Unretweet a tweet
        
        Args:
            tweet_id: ID of the tweet to unretweet
        
        Returns:
            True if successful, False otherwise
        """
        try:
            data = {'id': tweet_id}
            result = self._make_request('POST', 'statuses/unretweet.json', data=data)
            
            if result:
                logger.info(f"Tweet {tweet_id} unretweeted successfully")
                return True
            else:
                logger.error(f"Failed to unretweet {tweet_id}")
                return False
                
        except Exception as e:
            logger.error(f"Error unretweeting: {e}")
            return False
    
    def reply_to_tweet(self, tweet_id: str, text: str) -> Optional[Dict]:
        """
        Reply to a tweet
        
        Args:
            tweet_id: ID of the tweet to reply to
            text: Reply content
        
        Returns:
            Tweet data if successful, None otherwise
        """
        return self.post_tweet(text, reply_to=tweet_id)
    
    def search_tweets(self, query: str, count: int = 20, result_type: str = 'recent') -> Optional[List[Dict]]:
        """
        Search for tweets
        
        Args:
            query: Search query
            count: Number of tweets to return (max 100)
            result_type: 'mixed', 'recent', or 'popular'
        
        Returns:
            List of tweets if successful, None otherwise
        """
        try:
            params = {
                'q': query,
                'count': min(count, 100),
                'result_type': result_type,
                'tweet_mode': 'extended'
            }
            
            result = self._make_request('GET', 'search/tweets.json', params=params)
            
            if result and 'statuses' in result:
                logger.info(f"Found {len(result['statuses'])} tweets for query: {query}")
                return result['statuses']
            else:
                logger.error("Failed to search tweets")
                return None
                
        except Exception as e:
            logger.error(f"Error searching tweets: {e}")
            return None
    
    def get_user_timeline(self, screen_name: str = None, count: int = 20) -> Optional[List[Dict]]:
        """
        Get user timeline
        
        Args:
            screen_name: Twitter username (optional, uses authenticated user if None)
            count: Number of tweets to return (max 200)
        
        Returns:
            List of tweets if successful, None otherwise
        """
        try:
            params = {
                'count': min(count, 200),
                'tweet_mode': 'extended'
            }
            
            if screen_name:
                params['screen_name'] = screen_name
            
            result = self._make_request('GET', 'statuses/user_timeline.json', params=params)
            
            if result:
                logger.info(f"Retrieved {len(result)} tweets from timeline")
                return result
            else:
                logger.error("Failed to get user timeline")
                return None
                
        except Exception as e:
            logger.error(f"Error getting user timeline: {e}")
            return None
    
    def auto_like_by_keyword(self, keywords: List[str], count: int = 10, delay_range: tuple = (30, 60)):
        """
        Automatically like tweets containing specific keywords
        
        Args:
            keywords: List of keywords to search for
            count: Number of tweets to like per keyword
            delay_range: Range of seconds to wait between actions (min, max)
        """
        logger.info(f"Starting auto like for keywords: {keywords}")
        
        for keyword in keywords:
            try:
                tweets = self.search_tweets(keyword, count=count)
                if not tweets:
                    continue
                
                for tweet in tweets:
                    tweet_id = tweet['id_str']
                    
                    # Skip if already liked
                    if tweet.get('favorited', False):
                        logger.info(f"Tweet {tweet_id} already liked, skipping")
                        continue
                    
                    # Like the tweet
                    if self.like_tweet(tweet_id):
                        delay = random.uniform(*delay_range)
                        logger.info(f"Liked tweet {tweet_id}, waiting {delay:.1f} seconds")
                        time.sleep(delay)
                    else:
                        logger.warning(f"Failed to like tweet {tweet_id}")
                
                # Wait between keywords
                time.sleep(random.uniform(60, 120))
                
            except Exception as e:
                logger.error(f"Error in auto like for keyword '{keyword}': {e}")
    
    def auto_retweet_by_keyword(self, keywords: List[str], count: int = 5, delay_range: tuple = (60, 120)):
        """
        Automatically retweet tweets containing specific keywords
        
        Args:
            keywords: List of keywords to search for
            count: Number of tweets to retweet per keyword
            delay_range: Range of seconds to wait between actions (min, max)
        """
        logger.info(f"Starting auto retweet for keywords: {keywords}")
        
        for keyword in keywords:
            try:
                tweets = self.search_tweets(keyword, count=count)
                if not tweets:
                    continue
                
                for tweet in tweets:
                    tweet_id = tweet['id_str']
                    
                    # Skip if already retweeted
                    if tweet.get('retweeted', False):
                        logger.info(f"Tweet {tweet_id} already retweeted, skipping")
                        continue
                    
                    # Retweet
                    if self.retweet(tweet_id):
                        delay = random.uniform(*delay_range)
                        logger.info(f"Retweeted {tweet_id}, waiting {delay:.1f} seconds")
                        time.sleep(delay)
                    else:
                        logger.warning(f"Failed to retweet {tweet_id}")
                
                # Wait between keywords
                time.sleep(random.uniform(120, 180))
                
            except Exception as e:
                logger.error(f"Error in auto retweet for keyword '{keyword}': {e}")
    
    def auto_reply_by_keyword(self, keywords: List[str], replies: List[str], count: int = 3, delay_range: tuple = (120, 180)):
        """
        Automatically reply to tweets containing specific keywords
        
        Args:
            keywords: List of keywords to search for
            replies: List of possible reply messages
            count: Number of tweets to reply to per keyword
            delay_range: Range of seconds to wait between actions (min, max)
        """
        logger.info(f"Starting auto reply for keywords: {keywords}")
        
        for keyword in keywords:
            try:
                tweets = self.search_tweets(keyword, count=count)
                if not tweets:
                    continue
                
                for tweet in tweets:
                    tweet_id = tweet['id_str']
                    reply_text = random.choice(replies)
                    
                    # Reply to the tweet
                    if self.reply_to_tweet(tweet_id, reply_text):
                        delay = random.uniform(*delay_range)
                        logger.info(f"Replied to {tweet_id}, waiting {delay:.1f} seconds")
                        time.sleep(delay)
                    else:
                        logger.warning(f"Failed to reply to {tweet_id}")
                
                # Wait between keywords
                time.sleep(random.uniform(180, 300))
                
            except Exception as e:
                logger.error(f"Error in auto reply for keyword '{keyword}': {e}")

def main():
    """Main function to demonstrate usage"""
    # Configuration
    AUTH_TOKEN = "YOUR_AUTH_TOKEN_HERE"  # Replace with your auth_token
    CSRF_TOKEN = "YOUR_CSRF_TOKEN_HERE"  # Optional, will be fetched automatically
    
    # Initialize Twitter Auto
    twitter = TwitterAuto(AUTH_TOKEN, CSRF_TOKEN)
    
    # Example usage
    if twitter.csrf_token:
        logger.info("Twitter Auto initialized successfully!")
        
        # Example 1: Post a tweet
        # twitter.post_tweet("Hello Twitter! This is an automated tweet. 🤖")
        
        # Example 2: Auto like tweets with specific keywords
        keywords = ["python", "programming", "coding"]
        # twitter.auto_like_by_keyword(keywords, count=5)
        
        # Example 3: Auto retweet tweets with specific keywords
        # twitter.auto_retweet_by_keyword(keywords, count=3)
        
        # Example 4: Auto reply to tweets
        replies = [
            "Great post! 👍",
            "Thanks for sharing! 🙏",
            "Interesting perspective! 🤔",
            "Love this content! ❤️"
        ]
        # twitter.auto_reply_by_keyword(keywords, replies, count=2)
        
    else:
        logger.error("Failed to initialize Twitter Auto. Check your auth_token.")

if __name__ == "__main__":
    main()