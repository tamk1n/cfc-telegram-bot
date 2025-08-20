#!/usr/bin/env python3
"""
Script to download and cache player photos locally for faster loading
"""
import os
import asyncio
import aiohttp
import settings

async def download_player_photos():
    """Download all player photos and save them locally"""
    static_folder = os.path.join(os.path.dirname(__file__), 'static', 'players')
    os.makedirs(static_folder, exist_ok=True)
    
    async with aiohttp.ClientSession() as session:
        for player in settings.PLAYERS:
            player_id = player['id']
            player_name = player['full_name']
            
            # Check if photo already exists
            photo_path = os.path.join(static_folder, f"{player_id}.jpg")
            if os.path.exists(photo_path):
                print(f"✅ {player_name} - Photo already exists")
                continue
            
            try:
                # Try to get player stats to find photo URL
                url = f"{settings.PLAYER_STATS_API_URL}/{player_id}/stats"
                async with session.get(url) as response:
                    if response.status == 200:
                        data = await response.json()
                        
                        # Try to find photo URL in different sections
                        photo_url = None
                        for section in ['goalKeeping', 'goals', 'passSuccess']:
                            if (section in data and 
                                'playerAvatar' in data[section] and
                                'image' in data[section]['playerAvatar'] and
                                'file' in data[section]['playerAvatar']['image'] and
                                'url' in data[section]['playerAvatar']['image']['file']):
                                photo_url = data[section]['playerAvatar']['image']['file']['url']
                                break
                        
                        if photo_url:
                            # Convert to HTTPS and WebP if needed
                            if photo_url.startswith('http://'):
                                photo_url = photo_url.replace('http://', 'https://')
                                photo_url = photo_url.replace('png', 'webp')
                                
                            # Download the photo
                            async with session.get(photo_url) as img_response:
                                if img_response.status == 200 and img_response.content_type.startswith('image/'):
                                    image_data = await img_response.read()
                                    
                                    # Save the photo
                                    with open(photo_path, 'wb') as f:
                                        f.write(image_data)
                                    
                                    print(f"✅ {player_name} - Downloaded successfully")
                                else:
                                    
                                    print(f"❌ {player_name} - Could not download photo (HTTP {img_response.status})")
                        else:
                            print(f"⚠️ {player_name} - No photo URL found in API response")
                    else:
                        print(f"❌ {player_name} - API request failed (HTTP {response.status})")
                        
            except Exception as e:
                print(f"❌ {player_name} - Error: {e}")
            
            # Small delay to be nice to the API
            await asyncio.sleep(0.5)

if __name__ == "__main__":
    print("🔄 Starting player photo download...")
    asyncio.run(download_player_photos())
    print("✅ Photo download complete!")
