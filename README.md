# reddit-assistant

Monitors Reddit subreddits for posts matching keywords related to TRT and peptide use. 
When a match is found, it summarises the post and sends it to Telegram so you can 
manually read it, write your own reply, and post it yourself.

The script never writes replies, never posts to Reddit, and never acts automatically.

## How it works

1. Scans `subreddits.txt` for new posts every 10 minutes
2. Matches post titles/bodies against `keywords.txt`
3. Summarises the post — core question, key details, what the person needs
4. Sends the summary to Telegram so you can decide whether to respond manually

## Setup

```powershell
& "C:\Program Files\Python39\python.exe" -m pip install -r requirements.txt
copy .env.example .env   # then fill in real keys
& "C:\Program Files\Python39\python.exe" main.py
```

## Keys required

| Key | Where to get it |
|-----|----------------|
| `REDDIT_CLIENT_ID` + `REDDIT_CLIENT_SECRET` | reddit.com/prefs/apps → Create App → Script |
| `ANTHROPIC_API_KEY` | console.anthropic.com |
| `TELEGRAM_BOT_TOKEN` | Message @BotFather → /newbot |
| `TELEGRAM_CHAT_ID` | Message your bot, then `https://api.telegram.org/bot<TOKEN>/getUpdates` |

## Files you edit regularly

| File | Why |
|------|-----|
| `keywords.txt` | Add new triggers as you find better ones |
| `subreddits.txt` | Add/remove subs |

## Optional: run as a Windows service (NSSM)

```powershell
nssm install RedditAssistant "C:\Program Files\Python39\python.exe" "C:\Users\PFrew\Projects\reddit-assistant\main.py"
nssm set RedditAssistant AppDirectory "C:\Users\PFrew\Projects\reddit-assistant"
nssm start RedditAssistant
```
