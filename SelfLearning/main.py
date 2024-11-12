from TikTokApi import TikTokApi
import asyncio
import os
from gensim.models import Word2Vec
from word2vec import update_word2vec_model, update_trending_comments, load_word2vec_model
from get_comments import get_comments, get_comments_for_videos
from get_trending_videos import trending_videos
os.chmod('/Users/anqi/TikTok-Api/word2vec.model', 0o666)  # Grants read/write permissions

async def main():
    await update_trending_comments()

# Main execution
if __name__ == "__main__":
    
        # Run the main coroutine inside asyncio.run
    asyncio.run(main())
    