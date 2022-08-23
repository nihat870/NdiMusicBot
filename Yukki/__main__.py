import asyncio
import importlib
import os
import re

from pyrogram import filters
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from pytgcalls import idle
from rich.console import Console
from rich.table import Table
from youtubesearchpython import VideosSearch

from config import (LOG_GROUP_ID, LOG_SESSION, STRING1, STRING2, STRING3,
                    STRING4, STRING5)
from Yukki import (ASS_CLI_1, ASS_CLI_2, ASS_CLI_3, ASS_CLI_4, ASS_CLI_5,
                   ASSID1, ASSID2, ASSID3, ASSID4, ASSID5, ASSNAME1, ASSNAME2,
                   ASSNAME3, ASSNAME4, ASSNAME5, BOT_ID, BOT_NAME, LOG_CLIENT,
                   OWNER_ID, SUDOERS, app, random_assistant)
from Yukki.Core.Clients.cli import LOG_CLIENT
from Yukki.Core.PyTgCalls.Yukki import (pytgcalls1, pytgcalls2, pytgcalls3,
                                        pytgcalls4, pytgcalls5)
from Yukki.Database import (get_active_chats, get_active_video_chats,
                            get_sudoers, is_on_off, remove_active_chat,
                            remove_active_video_chat)
from Yukki.Inline import private_panel
from Yukki.Plugins import ALL_MODULES
from Yukki.Utilities.inline import paginate_modules

try:
    from config import START_IMG_URL
except:
    START_IMG_URL = None


loop = asyncio.get_event_loop()
console = Console()
HELPABLE = {}


async def initiate_bot():
    with console.status(
        "[magenta] Yenidən Başlama tamamlanır...",
    ) as status:
        ass_count = len(random_assistant)
        if ass_count == 0:
            console.print(
                f"\n[red] Heç bir köməkçi dəyişəni tapılmadı!.. Prosesdən çıxın"
            )
            return
        try:
            chats = await get_active_video_chats()
            for chat in chats:
                chat_id = int(chat["chat_id"])
                await remove_active_video_chat(chat_id)
        except Exception as e:
            pass
        try:
            chats = await get_active_chats()
            for chat in chats:
                chat_id = int(chat["chat_id"])
                await remove_active_chat(chat_id)
        except Exception as e:
            pass
        status.update(
            status="[bold blue]Skan Pluginləri", spinner="earth"
        )
        console.print("Found {} Plugins".format(len(ALL_MODULES)) + "\n")
        status.update(
            status="[bold red]Plugin idxalı...",
            spinner="bouncingBall",
            spinner_style="yellow",
        )
        for all_module in ALL_MODULES:
            imported_module = importlib.import_module(
                "Yukki.Plugins." + all_module
            )
            if (
                hasattr(imported_module, "__MODULE__")
                and imported_module.__MODULE__
            ):
                imported_module.__MODULE__ = imported_module.__MODULE__
                if (
                    hasattr(imported_module, "__HELP__")
                    and imported_module.__HELP__
                ):
                    HELPABLE[
                        imported_module.__MODULE__.lower()
                    ] = imported_module
            console.print(
                f">> [bold cyan]Uğurla idxal edin: [green]{all_module}.py"
            )
        console.print("")
        status.update(
            status="[bold blue]İdxal tamamlandı!",
        )
    console.print(
        "[bold green]Xoşbəxt!! King Music Botu Uğurla Başladı!\n"
    )
    try:
        await app.send_message(
            LOG_GROUP_ID,
            "<b>Xoşbəxt!! Assistent Hesabı Uğurla Başladı!</b>",
        )
    except Exception as e:
        print(
            "\nBot Qrup jurnalına daxil ola bilmədi.  Botunuzu Qrup jurnalınıza əlavə etdiyinizə və admin kimi yüksəldildiyinizə əmin olun!"
        )
        console.print(f"\n[red]Bot Stop")
        return
    a = await app.get_chat_member(LOG_GROUP_ID, BOT_ID)
    if a.status != "administrator":
        print("Qrup LOG-də Botu Admin kimi təşviq edin")
        console.print(f"\n[red]Bot Stop")
        return
    console.print(f"\n┌[red] Bot Başladı {BOT_NAME}!")
    console.print(f"├[green] ID :- {BOT_ID}!")
    if STRING1 != "None":
        try:
            await ASS_CLI_1.send_message(
                LOG_GROUP_ID,
                "<b>Xoşbəxt!! Assistent Hesabı Uğurla Başladı!</b>",
            )
        except Exception as e:
            print(
                "\nAssistent hesabı Qrup Qeydinə daxil ola bilmədi.  Köməkçi hesabının Günlük Qrupa daxil olduğuna əmin olun və onu admin edin!"
            )
            console.print(f"\n[red]Bot Stop")
            return
        try:
            await ASS_CLI_1.join_chat("gunes_isigi_33")
            await ASS_CLI_1.join_chat("king_sohbet_33")
        except:
            pass
        console.print(f"├[red] Assistent Uğurla Başladı {ASSNAME1}!")
        console.print(f"├[green] ID :- {ASSID1}!")
    if STRING2 != "None":
        try:
            await ASS_CLI_2.send_message(
                LOG_GROUP_ID,
                "<b>Xoşbəxt!!  Assistent Hesabı 2 Uğurla Başladı!</b>",
            )
        except Exception as e:
            print(
                "\nAssistent Hesabı 2 log Kanalına daxil ola bilmədi.  Assistentinizi jurnal kanalınıza əlavə etdiyinizə və admin kimi yüksəldiyinizə əmin olun!"
            )
            console.print(f"\n[red]Botun dayandırılması")
            return
        try:
            await ASS_CLI_2.join_chat("gunes_isigi_33")
            await ASS_CLI_2.join_chat("king_sohbet_33")
        except:
            pass
        console.print(f"├[red] Assistent 2 olaraq başladı {ASSNAME2}!")
        console.print(f"├[green] ID :- {ASSID2}!")
    if STRING3 != "None":
        try:
            await ASS_CLI_3.send_message(
                LOG_GROUP_ID,
                "<b>Təbriklər!!  Assistant Client 3 uğurla başladı!</b>",
            )
        except Exception as e:
            print(
                "\nAssistent Hesabı 3 log Kanalına daxil ola bilmədi.  Assistentinizi jurnal kanalınıza əlavə etdiyinizə və admin kimi yüksəldiyinizə əmin olun!"
            )
            console.print(f"\n[red]Botun dayandırılması")
            return
        try:
            await ASS_CLI_3.join_chat("gunes_isigi_33")
            await ASS_CLI_3.join_chat("king_sohbet_33")
        except:
            pass
        console.print(f"├[red] Köməkçi 3 olaraq başladı {ASSNAME3}!")
        console.print(f"├[green] ID :- {ASSID3}!")
    if STRING4 != "None":
        try:
            await ASS_CLI_4.send_message(
                LOG_GROUP_ID,
                "<b>Təbriklər!!  Assistant Client 4 uğurla başladı!</b>",
            )
        except Exception as e:
            print(
                "\nAssistent Hesabı 4 log Kanalına daxil ola bilmədi.  Assistentinizi jurnal kanalınıza əlavə etdiyinizə və admin kimi yüksəldiyinizə əmin olun!"
            )
            console.print(f"\n[red]Botun dayandırılması")
            return
        try:
            await ASS_CLI_3.join_chat("gunes_isigi_33")
            await ASS_CLI_3.join_chat("king_sohbet_33")
        except:
            pass
        console.print(f"├[red] Köməkçi 4 olaraq başladı {ASSNAME4}!")
        console.print(f"├[green] ID :- {ASSID4}!")
    if STRING5 != "None":
        try:
            await ASS_CLI_5.send_message(
                LOG_GROUP_ID,
                "<b>Təbriklər!!  Assistant Client 5 uğurla başladı!</b>",
            )
        except Exception as e:
            print(
                "\nAssistent Hesabı 5 log Kanalına daxil ola bilmədi.  Assistentinizi log kanalınıza əlavə etdiyinizə və admin kimi yüksəldiyinizə əmin olun!"
            )
            console.print(f"\n[red]Botun dayandırılması")
            return
        try:
            await ASS_CLI_3.join_chat("gunes_isigi_33")
            await ASS_CLI_3.join_chat("king_sohbet_33")
        except:
            pass
        console.print(f"├[red] Köməkçi 5 olaraq başladı {ASSNAME5}!")
        console.print(f"├[green] ID :- {ASSID5}!")
    if LOG_SESSION != "None":
        try:
            await LOG_CLIENT.send_message(
                LOG_GROUP_ID,
                "<b>Xoşbəxt!!  Bot Girişi Uğurla Başladı!</b>",
            )
        except Exception as e:
            print(
                "\nLog Müştərisi Log Groupa daxil ola bilmədi.  Müştəri Girişinin Qeydlər Qrupuna daxil olduğundan əmin olun və onu admin edin!"
            )
            console.print(f"\n[red]Bot Stop")
            return
        try:
            await ASS_CLI_3.join_chat("gunes_isigi_33")
            await ASS_CLI_3.join_chat("king_sohbet_33")
        except:
            pass
    console.print(f"└[red] King Music Bot-u yenidən başladın.")
    if STRING1 != "None":
        await pytgcalls1.start()
    if STRING2 != "None":
        await pytgcalls2.start()
    if STRING3 != "None":
        await pytgcalls3.start()
    if STRING4 != "None":
        await pytgcalls4.start()
    if STRING5 != "None":
        await pytgcalls5.start()
    await idle()
    console.print(f"\n[red]Bot Stop")

home_text_pm = f"""✨ **Salam, Xoş gəldiniz!**

🤖{BOT_NAME} **Telegram səsli söhbətində musiqi+videoları oynamaq üçün telegram musiqi botu**!

╭┉┉┅┅┄┄┄┄•◦ೋ•◦❥•◦ೋ
⧱ Musiqi çalın.
⧱ Videoları oynayın.
⧱ Mahnılar yükləyin.
⧱ Videoları yükləyin.
⧱ YOUTUBE Linkində Online ilə axtarın.
 •◦ೋ•◦❥•◦ೋ•┈┄┄┄┄┅┅┉╯


💡Menyuda bütün musiqi bot əmrlərini tapın » Komanda Menyu«!"""


@app.on_message(filters.command("help") & filters.private)
async def help_command(_, message):
    text, keyboard = await help_parser(message.from_user.mention)
    await app.send_message(message.chat.id, text, reply_markup=keyboard)


@app.on_message(filters.command("start") & filters.private)
async def start_command(_, message):
    if len(message.text.split()) > 1:
        name = (message.text.split(None, 1)[1]).lower()
        if name[0] == "s":
            sudoers = await get_sudoers()
            text = "👑 <u> **ᴏᴡɴᴇʀs:**</u>\n"
            sex = 0
            for x in OWNER_ID:
                try:
                    user = await app.get_users(x)
                    user = (
                        user.first_name if not user.mention else user.mention
                    )
                    sex += 1
                except Exception:
                    continue
                text += f"{sex}⌬ {user}\n"
            smex = 0
            for count, user_id in enumerate(sudoers, 1):
                if user_id not in OWNER_ID:
                    try:
                        user = await app.get_users(user_id)
                        user = (
                            user.first_name
                            if not user.mention
                            else user.mention
                        )
                        if smex == 0:
                            smex += 1
                            text += "\n👨‍🚀 <u> **sᴜᴅᴏ ᴜsᴇʀs:**</u>\n"
                        sex += 1
                        text += f"{sex}⌬ {user}\n"
                    except Exception:
                        continue
            if not text:
                await message.reply_text("Sudo İstifadəçisi yoxdur")
            else:
                await message.reply_text(text)
            if await is_on_off(5):
                sender_id = message.from_user.id
                sender_name = message.from_user.first_name
                umention = f"[{sender_name}](tg://user?id={int(sender_id)})"
                return await LOG_CLIENT.send_message(
                    LOG_GROUP_ID,
                    f"{message.from_user.mention} Yalnız yoxlamaq üçün botu işə salın <code>SUDOLIST</code>\n\n**USER ID:** {sender_id}\n**USER NAME:** {sender_name}",
                )
        if name == "help":
            text, keyboard = await help_parser(message.from_user.mention)
            await message.delete()
            return await app.send_text(
                message.chat.id,
                text,
                reply_markup=keyboard,
            )
        if name[0] == "i":
            m = await message.reply_text("🔎 Məlumat axtarılır!")
            query = (str(name)).replace("info_", "", 1)
            query = f"https://www.youtube.com/watch?v={query}"
            results = VideosSearch(query, limit=1)
            for result in results.result()["result"]:
                title = result["title"]
                duration = result["duration"]
                views = result["viewCount"]["short"]
                thumbnail = result["thumbnails"][0]["url"].split("?")[0]
                channellink = result["channel"]["link"]
                channel = channel = result["channel"]["name"]
                link = result["link"]
                published = result["publishedTime"]
            searched_text = f"""
🔍__**Video Track Məlumatı**__

🎸**Başlıq:** {title}

⏳**Müddət:** {duration} Menit
👀**Görüntülənib :** `{views}`
⏰**Çıxış vaxtı:** {published}
🎥**Kanal Adı:** {channel}
📎**Kanal Linki:** [Lihat Disini]({channellink})
🔗**Video Linki:** [Link]({link})

💫__Axtarış Powered by {BOT_NAME}__"""
            key = InlineKeyboardMarkup(
                [
                    [
                        InlineKeyboardButton(
                            text="🎥 YouTube Videolarına baxmaq", url=f"{link}"
                        ),
                        InlineKeyboardButton(
                            text="bagla", callback_data="close"
                        ),
                    ],
                ]
            )
            await m.delete()
            await app.send_photo(
                message.chat.id,
                photo=thumbnail,
                caption=searched_text,
                parse_mode="markdown",
                reply_markup=key,
            )
            if await is_on_off(5):
                sender_id = message.from_user.id
                sender_name = message.from_user.first_name
                umention = f"[{sender_name}](tg://user?id={int(sender_id)})"
                return await LOG_CLIENT.send_message(
                    LOG_GROUP_ID,
                    f"{message.from_user.mention} Yalnız yoxlamaq üçün botu işə salın <code>INFORMASI VIDEO</code>\n\n**USER ID:** {sender_id}\n**USER NAME:** {sender_name}",
                )
            return
    out = private_panel()
    if START_IMG_URL is None:
        await message.reply_text(
            home_text_pm,
            reply_markup=InlineKeyboardMarkup(out[1]),
        )
    else:
        await message.reply_photo(
            photo=START_IMG_URL,
            caption=home_text_pm,
            reply_markup=InlineKeyboardMarkup(out[1]),
        )
    if await is_on_off(5):
        sender_id = message.from_user.id
        sender_name = message.from_user.first_name
        umention = f"[{sender_name}](tg://user?id={int(sender_id)})"
        return await LOG_CLIENT.send_message(
            LOG_GROUP_ID,
            f"{message.from_user.mention} Botlar başladı.\n\n**USER ID:** {sender_id}\n**USER NAME:** {sender_name}",
        )
    return


async def help_parser(name, keyboard=None):
    if not keyboard:
        keyboard = InlineKeyboardMarkup(paginate_modules(0, HELPABLE, "help"))
    return (
        """Salam {first_name},

Ətraflı məlumat üçün aşağıdakı düyməni basın.

Bütün Əmrlər üçün istifadə edin: /
""".format(
            first_name=name
        ),
        keyboard,
    )


@app.on_callback_query(filters.regex("shikhar"))
async def shikhar(_, CallbackQuery):
    text, keyboard = await help_parser(CallbackQuery.from_user.mention)
    await CallbackQuery.message.edit(text, reply_markup=keyboard)


@app.on_callback_query(filters.regex("search_helper_mess"))
async def search_helper_mess(_, CallbackQuery):
    await CallbackQuery.message.delete()
    text, keyboard = await help_parser(CallbackQuery.from_user.mention)
    await app.send_message(
        CallbackQuery.message.chat.id, text, reply_markup=keyboard
    )


@app.on_callback_query(filters.regex(r"help_(.*?)"))
async def help_button(client, query):
    home_match = re.match(r"help_home\((.+?)\)", query.data)
    mod_match = re.match(r"help_module\((.+?)\)", query.data)
    prev_match = re.match(r"help_prev\((.+?)\)", query.data)
    next_match = re.match(r"help_next\((.+?)\)", query.data)
    back_match = re.match(r"help_back", query.data)
    create_match = re.match(r"help_create", query.data)
    top_text = f"""Salam {query.from_user.first_name},

Ətraflı məlumat üçün aşağıdakı düyməni basın.

Bütün Əmrlər üçün istifadə edin: /
 """
    if mod_match:
        module = mod_match.group(1)
        if str(module) == "sudousers":
            userid = query.from_user.id
            if userid in SUDOERS:
                pass
            else:
                return await query.answer(
                    "Bu düyməyə yalnız SUDO İSTİFADƏÇİLƏRİ daxil ola bilər",
                    show_alert=True,
                )
        text = (
            "{} **{}**:\n".format(
                "Yardım üçün burada", HELPABLE[module].__MODULE__
            )
            + HELPABLE[module].__HELP__
        )
        key = InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        text="↪️ Kembali", callback_data="help_back"
                    ),
                    InlineKeyboardButton(
                        text="✖️ Tutup", callback_data="close"
                    ),
                ],
            ]
        )

        await query.message.edit(
            text=text,
            reply_markup=key,
            disable_web_page_preview=True,
        )
    elif home_match:
        out = private_panel()
        await app.send_message(
            query.from_user.id,
            text=home_text_pm,
            reply_markup=InlineKeyboardMarkup(out[1]),
        )
        await query.message.delete()
    elif prev_match:
        curr_page = int(prev_match.group(1))
        await query.message.edit(
            text=top_text,
            reply_markup=InlineKeyboardMarkup(
                paginate_modules(curr_page - 1, HELPABLE, "help")
            ),
            disable_web_page_preview=True,
        )

    elif next_match:
        next_page = int(next_match.group(1))
        await query.message.edit(
            text=top_text,
            reply_markup=InlineKeyboardMarkup(
                paginate_modules(next_page + 1, HELPABLE, "help")
            ),
            disable_web_page_preview=True,
        )

    elif back_match:
        await query.message.edit(
            text=top_text,
            reply_markup=InlineKeyboardMarkup(
                paginate_modules(0, HELPABLE, "help")
            ),
            disable_web_page_preview=True,
        )

    elif create_match:
        text, keyboard = await help_parser(query)
        await query.message.edit(
            text=text,
            reply_markup=keyboard,
            disable_web_page_preview=True,
        )

    return await client.answer_callback_query(query.id)


if __name__ == "__main__":
    loop.run_until_complete(initiate_bot())
