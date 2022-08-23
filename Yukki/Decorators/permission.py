from typing import Dict, List, Union

from Yukki import BOT_ID, app


def PermissionCheck(mystic):
    async def wrapper(_, message):
        if message.chat.type == "private":
            return await mystic(_, message)
        a = await app.get_chat_member(message.chat.id, BOT_ID)
        if a.status != "administrator":
            return await message.reply_text(
                "Bəzi icazələri olan admin olmalıyam:\n"
                 + "\n- can_manage_voice_chats: Səsli söhbəti idarə etmək üçün"
                 + "\n- can_delete_messages: Botun Axtarılan Zibil qutusunu silmək üçün"
                 + "\n- can_invite_users: Köməkçini söhbətə dəvət etmək."
             )
        if not a.can_manage_voice_chats:
            await message.reply_text(
                "Bu əməliyyatı yerinə yetirmək üçün lazımi icazələrim yoxdur."
                 + "\nİcazələr: __SƏSLİNİ İDARƏ EDİN__"
             )
            return
        if not a.can_delete_messages:
            await message.reply_text(
                "Bu əməliyyatı yerinə yetirmək üçün lazımi icazələrim yoxdur."
                 + "\nİcazələr: __MESSAGE_ SİL_"
             )
            return
        if not a.can_invite_users:
            await message.reply_text(
                "Bu əməliyyatı yerinə yetirmək üçün lazımi icazələrim yoxdur."
                 + "\nİcazə: LİNKDƏN İSTİFADƏÇİLƏRİ DƏVƏT EDİN"
             )
            return
        return await mystic(_, message)

    return wrapper
