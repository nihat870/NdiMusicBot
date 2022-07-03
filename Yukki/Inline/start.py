from pyrogram.types import (CallbackQuery, InlineKeyboardButton,
                            InlineKeyboardMarkup, InputMediaPhoto, Message)

from config import MUSIC_BOT_NAME, SUPPORT_CHANNEL, SUPPORT_GROUP
from Yukki import BOT_USERNAME


def setting_markup2():
    buttons = [
        [
            InlineKeyboardButton(text="🔈 səs keyfiyyəti", callback_data="AQ"),
            InlineKeyboardButton(text="🎚 səs həcmi", callback_data="AV"),
        ],
        [
            InlineKeyboardButton(
                text="👥 Lisenziya", callback_data="AU"
            ),
            InlineKeyboardButton(
                text="💻 idarə paneli", callback_data="Dashboard"
            ),
        ],
        [
            InlineKeyboardButton(text="✖️ Bagla", callback_data="close"),
        ],
    ]
    return f"⚙️  **{MUSIC_BOT_NAME} AYARLAR**", buttons


def start_pannel():
    if not SUPPORT_CHANNEL and not SUPPORT_GROUP:
        buttons = [
            [
                InlineKeyboardButton(
                    text="📋 SİFARİŞ MENUSİ", callback_data="shikhar"
                ),
            ],
            [
                InlineKeyboardButton(
                    text="🔧 AYARLAR", callback_data="settingm"
                )
            ],
        ]
        return f"🎛  **MƏN {MUSIC_BOT_NAME}**", buttons
    if not SUPPORT_CHANNEL and SUPPORT_GROUP:
        buttons = [
            [
                InlineKeyboardButton(
                    text="📋 SİFARİŞ MENUSİ", callback_data="shikhar"
                ),
            ],
            [
                InlineKeyboardButton(
                    text="🔧 AYARLAR", callback_data="settingm"
                )
            ],
            [
                InlineKeyboardButton(
                    text="📨GROUP", url=f"{SUPPORT_GROUP}"
                ),
            ],
            [
                 InlineKeyboardButton(
                    text="🥸 ᴏᴡɴᴇʀ 🥸", 
                url=f"https://t.me/nihat_33",
               )
            ],
        ]
        return f"🎛  **MEN {MUSIC_BOT_NAME}*", buttons
    if SUPPORT_CHANNEL and not SUPPORT_GROUP:
        buttons = [
            [
                InlineKeyboardButton(
                    text="📋 SIFARIS MENUSI", callback_data="shikhar"
                ),
            ],
            [
                InlineKeyboardButton(
                    text="🔧 AYARLAR", callback_data="settingm"
                )
            ],
            [
                InlineKeyboardButton(
                    text="📢KANAL", url=f"{SUPPORT_CHANNEL}"
                ),
            ],
            [
                 InlineKeyboardButton(
                    text="🥸 ᴏᴡɴᴇʀ 🥸", 
                url=f"https://t.me/nihat_33",
               )
            ],
        ]
        return f"🎛  **MEN {MUSIC_BOT_NAME}**", buttons
    if SUPPORT_CHANNEL and SUPPORT_GROUP:
        buttons = [
            [
                InlineKeyboardButton(
                    text="📋 SIFARIS MENUSI", callback_data="shikhar"
                ),
            ],
            [
                InlineKeyboardButton(
                    text="🔧 AYARLAR", callback_data="settingm"
                )
            ],
            [
                InlineKeyboardButton(
                    text="📢KANAL", url=f"{SUPPORT_CHANNEL}"
                ),
                InlineKeyboardButton(
                    text="📨GROUP", url=f"{SUPPORT_GROUP}"
                ),
            ],
            [
                 InlineKeyboardButton(
                    text="🥸 ᴏᴡɴᴇʀ 🥸", 
                url=f"https://t.me/nihat_33",
               )
            ],
        ]
        return f"🎛  **MEN {MUSIC_BOT_NAME}**", buttons


def private_panel():
    if not SUPPORT_CHANNEL and not SUPPORT_GROUP:
        buttons = [
            [
                InlineKeyboardButton(
                    text="🗂 SİFARİŞ MENUSİ",
                    callback_data="search_helper_mess",
                ),
            ],
            [
                InlineKeyboardButton(
                    "➕ MƏNİ QRUPA ƏLAVƏ EDİN",
                    url=f"https://t.me/{BOT_USERNAME}?startgroup=true",
                )
            ],
        ]
        return f"🎛  **MEN {MUSIC_BOT_NAME}**", buttons
    if not SUPPORT_CHANNEL and SUPPORT_GROUP:
        buttons = [
            [
                InlineKeyboardButton(
                    text="🗂 SIFARIS MENUSI",
                    callback_data="search_helper_mess",
                ),
            ],
            [
                InlineKeyboardButton(
                    "➕ MƏNİ QRUPA ƏLAVƏ EDİN",
                    url=f"https://t.me/{BOT_USERNAME}?startgroup=true",
                )
            ],
            [
                InlineKeyboardButton(
                    text="📨GROUP", url=f"{SUPPORT_GROUP}"
                ),
            ],
            [
                 InlineKeyboardButton(
                    text="🥸 ᴏᴡɴᴇʀ 🥸", 
                url=f"https://t.me/nihat_33",
               )
            ],
        ]
        return f"🎛  **MEN {MUSIC_BOT_NAME}*", buttons
    if SUPPORT_CHANNEL and not SUPPORT_GROUP:
        buttons = [
            [
                InlineKeyboardButton(
                    text="🗂 SIFARIS MENUSI",
                    callback_data="search_helper_mess",
                ),
            ],
            [
                InlineKeyboardButton(
                    "➕ MƏNİ QRUPA ƏLAVƏ EDİN",
                    url=f"https://t.me/{BOT_USERNAME}?startgroup=true",
                )
            ],
            [
                InlineKeyboardButton(
                    text="📢KANAL", url=f"{SUPPORT_CHANNEL}"
                ),
            ],
            [
                 InlineKeyboardButton(
                    text="🥸 ᴏᴡɴᴇʀ 🥸", 
                url=f"https://t.me/nihat_33",
               )
            ],
        ]
        return f"🎛  **MEN {MUSIC_BOT_NAME}**", buttons
    if SUPPORT_CHANNEL and SUPPORT_GROUP:
        buttons = [
            [
                InlineKeyboardButton(
                    text="🗂 SIFARIS MENUSI",
                    callback_data="search_helper_mess",
                ),
            ],
            [
                InlineKeyboardButton(
                    "➕ MƏNİ QRUPA ƏLAVƏ EDİN",
                    url=f"https://t.me/{BOT_USERNAME}?startgroup=true",
                )
            ],
            [
                InlineKeyboardButton(
                    text="📢KANAL", url=f"{SUPPORT_CHANNEL}"
                ),
                InlineKeyboardButton(
                    text="📨GROUP", url=f"{SUPPORT_GROUP}"
                ),
            ],
            [
                 InlineKeyboardButton(
                    text="🥸 ᴏᴡɴᴇʀ 🥸", 
                url=f"https://t.me/nihat_33",
               )
            ],
        ]
        return f"🎛  **MEN {MUSIC_BOT_NAME}**", buttons


def setting_markup():
    buttons = [
        [
            InlineKeyboardButton(text="🔈 SƏS KEYFİYYƏTİ", callback_data="AQ"),
            InlineKeyboardButton(text="🎚 SES HECMI ", callback_data="AV"),
        ],
        [
            InlineKeyboardButton(
                text="👥 LİSENZİYA", callback_data="AU"
            ),
            InlineKeyboardButton(
                text="💻 MENU", callback_data="Dashboard"
            ),
        ],
        [
            InlineKeyboardButton(text="✖️ BAGLA", callback_data="close"),
            InlineKeyboardButton(text="≼ GERI", callback_data="okaybhai"),
        ],
    ]
    return f"🔧  **{MUSIC_BOT_NAME} AYARLAR**", buttons


def volmarkup():
    buttons = [
        [
            InlineKeyboardButton(
                text="🔄 ᴀᴛᴜʀ ᴜʟᴀɴɢ ᴠᴏʟᴜᴍᴇ 🔄", callback_data="HV"
            )
        ],
        [
            InlineKeyboardButton(text="🔈 ᴠᴏʟ ʀᴇɴᴅᴀʜ", callback_data="LV"),
            InlineKeyboardButton(text="🔉 ᴠᴏʟ sᴇᴅᴀɴɢ", callback_data="MV"),
        ],
        [
            InlineKeyboardButton(text="🔊 ᴠᴏʟ ᴛɪɴɢɢɪ", callback_data="HV"),
            InlineKeyboardButton(text="🔈 ᴠᴏʟ sᴇɪᴍʙᴀɴɢ", callback_data="VAM"),
        ],
        [
            InlineKeyboardButton(
                text="🔽 ᴠᴏʟᴜᴍᴇ ᴋᴜsᴛᴏᴍ 🔽", callback_data="Custommarkup"
            )
        ],
        [InlineKeyboardButton(text="≼ GERI", callback_data="settingm")],
    ]
    return f"🔧  **{MUSIC_BOT_NAME} AYARLAR**", buttons


def custommarkup():
    buttons = [
        [
            InlineKeyboardButton(text="+10", callback_data="PTEN"),
            InlineKeyboardButton(text="-10", callback_data="MTEN"),
        ],
        [
            InlineKeyboardButton(text="+25", callback_data="PTF"),
            InlineKeyboardButton(text="-25", callback_data="MTF"),
        ],
        [
            InlineKeyboardButton(text="+50", callback_data="PFZ"),
            InlineKeyboardButton(text="-50", callback_data="MFZ"),
        ],
        [InlineKeyboardButton(text="🔼 ᴠᴏʟᴜᴍᴇ ᴋᴜsᴛᴏᴍ 🔼", callback_data="AV")],
    ]
    return f"🔧  **{MUSIC_BOT_NAME} ᴘᴇɴɢᴀᴛᴜʀᴀɴ**", buttons


def usermarkup():
    buttons = [
        [
            InlineKeyboardButton(text="👥 sᴇᴍᴜᴀ", callback_data="EVE"),
            InlineKeyboardButton(text="🤴 ᴀᴅᴍɪɴ", callback_data="AMS"),
        ],
        [
            InlineKeyboardButton(
                text="📖 ᴅᴀғᴛᴀʀ ᴘᴇʀɪᴊɪɴᴀɴ", callback_data="USERLIST"
            )
        ],
        [InlineKeyboardButton(text="≼ ᴋᴇᴍʙᴀʟɪ", callback_data="settingm")],
    ]
    return f"🔧  **{MUSIC_BOT_NAME} ᴘᴇɴɢᴀᴛᴜʀᴀɴ**", buttons


def dashmarkup():
    buttons = [
        [
            InlineKeyboardButton(text="✔️ CALISMA VAXTI", callback_data="UPT"),
            InlineKeyboardButton(text="💾 Ram", callback_data="RAT"),
        ],
        [
            InlineKeyboardButton(text="💻 Cpu", callback_data="CPT"),
            InlineKeyboardButton(text="💽 Disk", callback_data="DIT"),
        ],
        [InlineKeyboardButton(text="≼ ᴋᴇᴍʙᴀʟɪ", callback_data="settingm")],
    ]
    return f"🔧  **{MUSIC_BOT_NAME} AYARLAR**", buttons
