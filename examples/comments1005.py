from TikTokApi import TikTokApi
import asyncio
import os
from transformers import pipeline

# Initialize sentiment analysis pipeline using BERT
sentiment_analysis = pipeline("sentiment-analysis", model="nlptown/bert-base-multilingual-uncased-sentiment")

ms_token = os.environ.get("ms_token", None)  # set your own ms_token


async def get_hashtag_videos():
    video_ids = []  # To store video IDs
    async with TikTokApi() as api:
        await api.create_sessions(ms_tokens=[ms_token], num_sessions=1, sleep_after=3)
        tag = api.hashtag(name="beauty")
        async for video in tag.videos(count=30):
            print(video)
            print(video.as_dict)
            video_ids.append(video.id)  # Store video ID
    return video_ids  # Return list of video IDs


async def get_comments_and_analyze(video_ids):
    async with TikTokApi() as api:
        await api.create_sessions(ms_tokens=[ms_token], num_sessions=1, sleep_after=3)
        
        for video_id in video_ids:  # Loop through each video ID
            print(f"Fetching comments for video ID: {video_id}")
            video = api.video(id=video_id)
            count = 0
            async for comment in video.comments(count=30):
                comment_text = comment.as_dict.get('text', '')  # Get comment text
                if comment_text:
                    print(f"Comment: {comment_text}")
                    
                    # Use BERT for sentiment analysis
                    result = sentiment_analysis(comment_text)[0]
                    print(f"Sentiment: {result['label']}, Score: {result['score']}")

                count += 1
                if count >= 30:  # Limit to 30 comments per video
                    break


async def main():
    # Step 1: Get video IDs
    video_ids = await get_hashtag_videos()

    # Step 2: Fetch comments and analyze sentiment
    await get_comments_and_analyze(video_ids)


if __name__ == "__main__":
    asyncio.run(main())

