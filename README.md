# reddit-assistant

Polls Reddit subreddits for posts matching keywords, drafts a reply using the Anthropic API in a configured voice, and sends the draft to a Telegram chat for manual review. It never auto-posts to Reddit.

## How it works

1. Scans `subreddits.txt` for new posts
2. Matches post titles/bodies against `keywords.txt`
3. Drafts a reply in the voice defined in `voice.md`
4. Sends draft to Telegram — you decide whether to post it

## Setup

```powershell
& "C:\Program Files\Python39\python.exe" -m pip install -r requirements.txt
copy .env.example .env   # then fill in real keys
& "C:\Program Files\Python39\python.exe" main.py
```

> **Known issue:** `main.py` imports `drafter` before calling `load_dotenv()`, so
> the Anthropic client is built before keys are loaded. The project will crash at
> startup until you fix it: move `load_dotenv()` above the `from drafter …` line in
> `main.py`.

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
| `voice.md` | Tune your tone, add example phrases that land well |
| `keywords.txt` | Add new triggers as you find better ones |
| `subreddits.txt` | Add/remove subs |

## Optional: run as a Windows service (NSSM)

```powershell
nssm install RedditAssistant "C:\Program Files\Python39\python.exe" "C:\Users\PFrew\Projects\reddit-assistant\main.py"
nssm set RedditAssistant AppDirectory "C:\Users\PFrew\Projects\reddit-assistant"
nssm start RedditAssistant
```
