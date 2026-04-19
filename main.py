import json
import time
import os
from pyrogram import Client, filters
from premium_emoji import PremiumEmoji

API_ID = int(os.getenv("API_ID"))
API_HASH = os.getenv("API_HASH")
BOT_TOKEN = os.getenv("BOT_TOKEN")

app = Client("premium_bot", api_id=API_ID, api_hash=API_HASH, bot_token=BOT_TOKEN)

DB_FILE = "premium.json"


# ---------------- DB ----------------
def load_db():
    try:
        with open(DB_FILE, "r") as f:
            return json.load(f)
    except:
        return {}


def save_db(data):
    with open(DB_FILE, "w") as f:
        json.dump(data, f, indent=4)


def is_premium(user_id):
    data = load_db()
    if str(user_id) in data:
        return data[str(user_id)] > time.time()
    return False


def add_premium(user_id, days):
    data = load_db()
    expiry = time.time() + (days * 86400)
    data[str(user_id)] = expiry
    save_db(data)


# ---------------- COMMANDS ----------------

@app.on_message(filters.command("start"))
async def start(client, message):
    status = is_premium(message.from_user.id)

    await message.reply(
        f"""
{PremiumEmoji.LINE}
👋 <b>Welcome {message.from_user.first_name}</b>
{PremiumEmoji.LINE}

Status: {PremiumEmoji.user_status(status)}

Use /premium to open panel
""",
        parse_mode="html"
    )


@app.on_message(filters.command("premium"))
async def premium_panel(client, message):
    await message.reply(
        PremiumEmoji.premium_menu(message.from_user.first_name),
        parse_mode="html"
    )


@app.on_message(filters.command("addprem"))
async def add_prem(client, message):
    OWNER_ID = 1718738592

    if message.from_user.id != OWNER_ID:
        return await message.reply("Not allowed")

    try:
        user_id = int(message.command[1])
        days = int(message.command[2])
    except:
        return await message.reply("Usage: /addprem user_id days")

    add_premium(user_id, days)

    await message.reply(
        PremiumEmoji.premium_success(days),
        parse_mode="html"
    )


@app.on_message(filters.command("chk"))
async def chk(client, message):
    if not is_premium(message.from_user.id):
        return await message.reply(
            PremiumEmoji.premium_required(),
            parse_mode="html"
        )

    await message.reply(
        f"{PremiumEmoji.APPROVED}\nPremium command executed 🔥",
        parse_mode="html"
    )


# ---------------- RUN ----------------
app.run()
