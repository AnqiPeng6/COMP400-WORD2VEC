from TikTokApi import TikTokApi
import asyncio
import os

ms_token = os.environ.get("ms_token", None)  # set your own ms_token

async def get_comments(video_id):
    async with TikTokApi() as api:
        await api.create_sessions(ms_tokens=[ms_token], num_sessions=1, sleep_after=3)
        video = api.video(id=video_id)
        count = 0
        async for comment in video.comments(count=30):
            print(comment)
            
async def get_hashtag_videos():
    async with TikTokApi() as api:
        await api.create_sessions(ms_tokens=[ms_token], num_sessions=1, sleep_after=3)
        tag = api.hashtag(name="funny")
        async for video in tag.videos(count=1):
            return video

def return_comments(video_id):
    return asyncio.run(get_comments(video_id))