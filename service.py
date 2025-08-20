import os
import json
import aiohttp
import asyncio
import logging
import settings

from datetime import datetime, timedelta


logger = logging.getLogger(__name__)

class APICache:
    def __init__(self, cache_dir="cache"):
        self.cache_dir = cache_dir
        self.ensure_cache_dir()
        
    def ensure_cache_dir(self):
        """Create cache directory if it doesn't exist"""
        if not os.path.exists(self.cache_dir):
            os.makedirs(self.cache_dir)
    
    def get_cache_file_path(self, cache_key):
        """Get the full path for a cache file"""
        return os.path.join(self.cache_dir, f"{cache_key}.json")
    
    def save_cache(self, cache_key, data):
        """Save data to cache with timestamp"""
        cache_data = {
            "timestamp": datetime.now().isoformat(),
            "data": data
        }
        
        try:
            cache_file = self.get_cache_file_path(cache_key)
            with open(cache_file, 'w', encoding='utf-8') as f:
                json.dump(cache_data, f, ensure_ascii=False, indent=2)
            logger.info(f"Cached data for {cache_key}")
        except Exception as e:
            logger.error(f"Failed to save cache for {cache_key}: {e}")
    
    def load_cache(self, cache_key):
        """Load data from cache if it exists"""
        try:
            cache_file = self.get_cache_file_path(cache_key)
            if os.path.exists(cache_file):
                with open(cache_file, 'r', encoding='utf-8') as f:
                    cache_data = json.load(f)
                return cache_data
        except Exception as e:
            logger.error(f"Failed to load cache for {cache_key}: {e}")
        return None
    
    def is_cache_fresh(self, cache_key, max_age_hours):
        """Check if cache is still fresh (within max_age_hours)"""
        cache_data = self.load_cache(cache_key)
        if not cache_data:
            return False
        
        try:
            cache_time = datetime.fromisoformat(cache_data["timestamp"])
            age = datetime.now() - cache_time
            return age < timedelta(hours=max_age_hours)
        except Exception:
            return False
    
    def get_cache_age(self, cache_key):
        """Get how old the cache is in hours"""
        cache_data = self.load_cache(cache_key)
        if not cache_data:
            return None
        
        try:
            cache_time = datetime.fromisoformat(cache_data["timestamp"])
            age = datetime.now() - cache_time
            return age.total_seconds() / 3600  # Return hours
        except Exception:
            return None
api_cache = APICache()

async def fetch_with_cache(url, cache_key, max_age_hours):
    """
    Fetch data from URL with intelligent caching:
    1. Check if we have fresh cache data
    2. If cache is fresh, return it immediately
    3. If cache is stale or missing, try API
    4. If API fails, return stale cache as fallback
    """

    if api_cache.is_cache_fresh(cache_key, max_age_hours):
        cache_data = api_cache.load_cache(cache_key)
        logger.info(f"Using fresh cached data for {cache_key}")
        return {
            "success": True,
            "data": cache_data["data"],
            "source": "cache",
            "timestamp": cache_data["timestamp"],
            "cache_age_hours": api_cache.get_cache_age(cache_key)
        }
    
    # First, try to fetch fresh data
    try:
        async with aiohttp.ClientSession() as session:
            async with session.get(url, timeout=aiohttp.ClientTimeout(total=10)) as response:
                if response.status == 200:
                    data = await response.json()
                    # Cache the successful response
                    api_cache.save_cache(cache_key, data)
                    logger.info(f"Fresh data fetched and cached for {cache_key}")
                    return {
                        "success": True,
                        "data": data,
                        "source": "live",
                        "timestamp": datetime.now().isoformat()
                    }
                else:
                    logger.warning(f"API returned status {response.status} for {cache_key}")
                    raise Exception(f"API error: {response.status}")
                    
    except Exception as e:
        logger.error(f"Failed to fetch fresh data for {cache_key}: {e}")
        
        # API failed, try to use cached data
        cache_data = api_cache.load_cache(cache_key)
        if cache_data:
            cache_age = api_cache.get_cache_age(cache_key)
            logger.info(f"Using cached data for {cache_key} (age: {cache_age:.1f} hours)")
            
            return {
                "success": True,
                "data": cache_data["data"],
                "source": "cache",
                "timestamp": cache_data["timestamp"],
                "cache_age_hours": cache_age
            }
        else:
            # No cache available
            logger.error(f"No cached data available for {cache_key}")
            return {
                "success": False,
                "error": str(e),
                "source": "none"
            }

# def format_cache_notice(result):
#     """Format a notice about data freshness for users"""
#     if result["source"] == "live":
#         return ""  # No notice needed for fresh data
#     elif result["source"] == "cache":
#         age_hours = result.get("cache_age_hours", 0)
#         if age_hours < 1:
#             return "📊 (Son məlumat - dəqiqələr əvvəl)"
#         elif age_hours < 24:
#             return f"📊 (Son məlumat - {age_hours:.0f} saat əvvəl)"
#         else:
#             days = age_hours / 24
#             return f"📊 (Son məlumat - {days:.0f} gün əvvəl)"
#     else:
#         return "⚠️ (Məlumatlar müvəqqəti əlçatan deyil)"