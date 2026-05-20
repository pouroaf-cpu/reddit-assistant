import praw
import time
import os
from dotenv import load_dotenv
from drafter import draft_reply
from telegram_bot import send_draft

load_dotenv()

reddit = praw.Reddit(
    client_id=os.getenv("REDDIT_CLIENT_ID"),
    client_secret=os.getenv("REDDIT_CLIENT_SECRET"),
    user_agent=os.getenv("REDDIT_USER_AGENT"),
)

with open("subreddits.txt") as f:
    subreddits = [line.strip() for line in f if line.strip()]

with open("keywords.txt") as f:
    keywords = [line.strip().lower() for line in f if line.strip()]

with open("voice.md") as f:
    voice_profile = f.read()

seen_file = "seen_posts.txt"
if not os.path.exists(seen_file):
    open(seen_file, "w").close()

def load_seen():
    with open(seen_file) as f:
        return set(f.read().splitlines())

def mark_seen(post_id):
    with open(seen_file, "a") as f:
        f.write(post_id + "\n")

def matches_keywords(text):
    text = text.lower()
    return any(kw in text for kw in keywords)

def process_subreddit(sub_name, seen):
    sub = reddit.subreddit(sub_name)
    for post in sub.new(limit=25):
        if post.id in seen:
            continue
        full_text = f"{post.title} {post.selftext}"
        if matches_keywords(full_text):
            print(f"Match: {post.title[:60]} (r/{sub_name})")
            draft = draft_reply(post.title, post.selftext, voice_profile)
            message = (
                f"📬 *New Reddit Match*\n"
                f"*Sub:* r/{sub_name}\n"
                f"*Post:* {post.title[:100]}\n"
                f"*Link:* {post.url}\n\n"
                f"*Draft reply:*\n{draft}"
            )
            send_draft(message)
            mark_seen(post.id)
            seen.add(post.id)

def run():
    print("Reddit assistant running...")
    while True:
        seen = load_seen()
        for sub in subreddits:
            try:
                process_subreddit(sub, seen)
            except Exception as e:
                print(f"Error on r/{sub}: {e}")
            time.sleep(2)
        print("Cycle complete. Sleeping 10 minutes...")
        time.sleep(600)

if __name__ == "__main__":
    run()
