from Yukki import BOT_USERNAME, LOG_GROUP_ID, app
from Yukki.Database import blacklisted_chats, is_gbanned_user, is_on_off


def checker(mystic):
    async def wrapper(_, message):
        if message.sender_chat:
            return await message.reply_text(
                "Sən__Admin Anonim__Di Bu Qrup Çatı!\nAdmin Hüquqlarından İstifadəçi Hesabına Qayıdın."
            )
        blacklisted_chats_list = await blacklisted_chats()
        if message.chat.id in blacklisted_chats_list:
            await message.reply_text(
                f"**Qara Siyahıya Söhbət**\n\nSöhbətiniz Sudo İstifadəçisi tərəfindən qara siyahıya salınıb. __SUDO USER__ adlı istifadəçidən Ağ Siyahıya daxil olun.\nSudo İstifadəçi siyahısını yoxlayın. [Disini](https://t.me/{BOT_USERNAME}?start=sudolist)"
            )
            return await app.leave_chat(message.chat.id)
        if await is_on_off(1):
            if int(message.chat.id) != int(LOG_GROUP_ID):
                return await message.reply_text(
                    f"Bot baxım altındadır.  Narahatçılığa görə üzr istəyirik 🙏!"
                )
        if await is_gbanned_user(message.from_user.id):
            return await message.reply_text(
                f"**GBan İstifadəçisi**\n\nSizə Ungban üçün Bot.Ask __SUDO USER__ istifadə etmək qadağandır.\nSudo İstifadəçi Siyahısını yoxlayın [Disini](https://t.me/{BOT_USERNAME}?start=sudolist)"
            )
        return await mystic(_, message)

    return wrapper


def checkerCB(mystic):
    async def wrapper(_, CallbackQuery):
        blacklisted_chats_list = await blacklisted_chats()
        if CallbackQuery.message.chat.id in blacklisted_chats_list:
            return await CallbackQuery.answer(
                "Çat Qara Siyahı", show_alert=True
            )
        if await is_on_off(1):
            if int(CallbackQuery.message.chat.id) != int(LOG_GROUP_ID):
                return await CallbackQuery.answer(
                    "Bot baxım altındadır.  Narahatçılığa görə üzr istəyirik 🙏!",
                    show_alert=True,
                )
        if await is_gbanned_user(CallbackQuery.from_user.id):
            return await CallbackQuery.answer(
                "Siz Gbandasınız", show_alert=True
            )
        return await mystic(_, CallbackQuery)

    return wrapper
