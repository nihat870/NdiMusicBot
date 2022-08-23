from config import LOG_GROUP_ID
from Yukki.Core.Clients.cli import LOG_CLIENT
from Yukki.Database import is_on_off


def logging(mystic):
    async def wrapper(_, message):
        if await is_on_off(5):
            if message.chat.username:
                chatusername = f"@{message.chat.username}"
            else:
                chatusername = "şəxsi qrup"
            try:
                query = message.text.split(None, 1)[1]
                what = "Sorğu Qəbul Edildi"
            except:
                try:
                    if not message.reply_to_message:
                        what = "Yalnız əmr verilir"
                    else:
                        what = "İstənilən fayla cavab verilir."
                except:
                    what = "Command"
            logger_text = f"""
__**Yeni {what}**__

**Qrup:** {message.chat.title}
**İstifadəçi:** {message.from_user.mention}
**İstifadəçi adı:** @{message.from_user.username}
**İstifadəçi İdi:** `{message.from_user.id}`
**Qrup Linkləri:** {chatusername}
**Sorğu:** {message.text}"""
            if LOG_CLIENT != "None":
                await LOG_CLIENT.send_message(
                    LOG_GROUP_ID,
                    f"{logger_text}",
                    disable_web_page_preview=True,
                )
        return await mystic(_, message)

    return wrapper
