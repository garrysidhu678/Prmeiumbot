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
            f"{PremiumEmoji.SMALL_LINE}\n"
            f"Only {PremiumEmoji.PREMIUM} users can use this command.\n"
            f"Upgrade now {PremiumEmoji.ROCKET}"
        )

    @staticmethod
    def premium_success(days):
        return (
            f"{PremiumEmoji.CHECK} <b>Premium Activated</b>\n"
            f"{PremiumEmoji.SMALL_LINE}\n"
            f"Duration: <b>{days} Days</b>\n"
            f"Enjoy {PremiumEmoji.FIRE}"
        )

    @staticmethod
    def premium_expired():
        return (
            f"{PremiumEmoji.WARNING} <b>Premium Expired</b>\n"
            f"{PremiumEmoji.SMALL_LINE}\n"
            f"Renew now {PremiumEmoji.ROCKET}"
        )

    @staticmethod
    def user_status(is_premium):
        return PremiumEmoji.BADGE if is_premium else PremiumEmoji.FREE

    @staticmethod
    def premium_menu(username):
        return (
            f"{PremiumEmoji.LINE}\n"
            f"{PremiumEmoji.CROWN} <b>Premium Panel</b>\n"
            f"{PremiumEmoji.LINE}\n\n"
            f"User: <b>{username}</b>\n"
            f"Status: {PremiumEmoji.BADGE}\n\n"
            f"{PremiumEmoji.ROCKET} Enjoy unlocked features!"
        )
