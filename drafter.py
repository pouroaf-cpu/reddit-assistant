import anthropic
import os

client = anthropic.Anthropic(api_key=os.getenv("ANTHROPIC_API_KEY"))

def draft_reply(post_title, post_body, voice_profile):
    prompt = f"""Analyse this Reddit post and extract the following:

1. **Core question** — What is the person actually asking? One sentence.
2. **Key details** — Any relevant numbers, compounds, or context they mentioned (e.g. dosage, concentration, compound name).
3. **What they need** — What kind of answer would genuinely help them? One sentence.

Reddit post:
Title: {post_title}
Body: {post_body}

Be concise. No fluff. Just the three points above."""

    message = client.messages.create(
        model="claude-sonnet-4-20250514",
        max_tokens=300,
        messages=[{"role": "user", "content": prompt}]
    )
    return message.content[0].text
