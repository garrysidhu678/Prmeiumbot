# premium_emoji.py

class PremiumEmoji:
    # Emojis
    CROWN = "👑"
    FIRE = "🔥"
    STAR = "⭐"
    DIAMOND = "💎"
    ROCKET = "🚀"
    LOCK = "🔐"
    CHECK = "✅"
    CROSS = "❌"
    WARNING = "⚠️"

    # Lines
    LINE = "━━━━━━━━━━━━━━━"
    SMALL_LINE = "───────────────"

    # Labels
    PREMIUM = f"{CROWN} <b>Premium</b>"
    FREE = f"{CROSS} <b>Free User</b>"
    APPROVED = f"{CHECK} <b>Approved</b>"
    DECLINED = f"{CROSS} <b>Declined</b>"
    LOCKED = f"{LOCK} <b>Locked</b>"

    # Badge
    BADGE = f"{DIAMOND} <b>Premium User</b>"

    @staticmethod
    def premium_required():
        return (
            f"{PremiumEmoji.LOCK} <b>Access Denied</b>\n"
            f"{Premium
