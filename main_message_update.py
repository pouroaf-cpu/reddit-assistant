## Updated message format in main.py
## Replace the `message = (...)` block in process_subreddit() with this:

message = (
    f"📬 *New Reddit Match*\n"
    f"*Sub:* r/{sub_name}\n"
    f"*Post:* {post.title[:100]}\n"
    f"*Link:* {post.url}\n\n"
    f"*Post summary:*\n{draft}\n\n"
    f"👆 Write your own reply and post it manually."
)
