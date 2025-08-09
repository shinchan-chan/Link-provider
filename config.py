# +++ Modified By Yato [telegram username: @i_killed_my_clan & @ProYato] +++ # aNDI BANDI SANDI JISNE BHI CREDIT HATAYA USKI BANDI RAndi 
import os
from os import environ
import logging
from logging.handlers import RotatingFileHandler

# Recommended
TG_BOT_TOKEN = os.environ.get("TG_BOT_TOKEN", "")
APP_ID = int(os.environ.get("APP_ID", "22706444"))
API_HASH = os.environ.get("API_HASH", "6e835a092d3431effe2c909873db1dab")

# Main
OWNER_ID = int(os.environ.get("OWNER_ID", "1683225887"))
PORT = os.environ.get("PORT", "8080")

# Database
DB_URI = os.environ.get("DB_URI", "mongodb+srv://adamopytbusiness1:uSswEjo4ZHMGDU8Z@cluster0.gqgmk.mongodb.net/?retryWrites=true&w=majority&appName=LinkProvidersBot")
DB_NAME = os.environ.get("DB_NAME", "Chnl-Link-Bot")

#Auto approve 
CHAT_ID = [int(app_chat_id) if id_pattern.search(app_chat_id) else app_chat_id for app_chat_id in environ.get('CHAT_ID', '').split()] # dont change anything 
TEXT = environ.get("APPROVED_WELCOME_TEXT", "<b>{mention},\n\nʏᴏᴜʀ ʀᴇǫᴜᴇsᴛ ᴛᴏ ᴊᴏɪɴ {title} ɪs ᴀᴘᴘʀᴏᴠᴇᴅ.\n\‣ ᴘᴏᴡᴇʀᴇᴅ ʙʏ @Codeflix_Bots</b>")
APPROVED = environ.get("APPROVED_WELCOME", "on").lower()

# Default
TG_BOT_WORKERS = int(os.environ.get("TG_BOT_WORKERS", "40"))
#--- ---- ---- --- --- --- - -- -  - - - - - - - - - - - --  - -

# Start pic
START_PIC_FILE_ID = "https://telegra.ph/file/f3d3aff9ec422158feb05-d2180e3665e0ac4d32.jpg"
START_IMG = "https://telegra.ph/file/f3d3aff9ec422158feb05-d2180e3665e0ac4d32.jpg"
# Messages
START_MSG = """<b>›› ʜᴇʏ!!, {mention} ~\n\n<blockquote expandable>ʟᴏᴠᴇ ᴛᴏ ᴡᴀᴛᴄʜ ᴀɴɪᴍᴇ sᴇʀɪᴇs ᴀɴᴅ ᴍᴏᴠɪᴇs? ɪ ᴀᴍ ᴍᴀᴅᴇ ᴛᴏ ʜᴇʟᴘ ʏᴏᴜ ᴛᴏ ғɪɴᴅ ᴡʜᴀᴛ ʏᴏᴜ'ʀᴇ ʟᴏᴏᴋɪɴɢ ꜰᴏʀ.</blockquote></b>"""
HELP = os.environ.get("HELP_MESSAGE", "<b><blockquote expandable>» Creator: <a href=https://t.me/DoraShin_hlo>Gojo</a>\n» Our Community: <a href=https://t.me/HellFire_Network>HellFire Network</a>\n» Anime Channel: <a href=https://t.me/HellFire_Academy>HellFire_Academy</a>\n» Ongoing Anime: <a href=https://t.me/Ongoing_HellFire_Academy>Ongoing HellFire</a>\n» Adult: <a href=https://t.me/Adult_Flux>Adult Flux</a></b>")
ABOUT = os.environ.get("ABOUT_MESSAGE", "<b><blockquote expandable>This bot is developed for to securely share Telegram channel links with temporary invite links, protecting your channels from copyright issues.</b>")

ABOUT_TXT = """<b>🤖 ᴍʏ ɴᴀᴍᴇ: {botname}
<blockquote><b>» ᴄʀᴇᴀᴛᴏʀ: <a href=https://t.me/Urr_Sanjiii>𝐒ᴀɴJɪ 𝐒αᴍᴀ</a>\n» ᴀɴɪᴍᴇ ᴄʜᴀɴɴᴇʟ : <a href=https://t.me/HellFire_Academy>𝐇ᴇʟʟғɪʀᴇ 𝐀ᴄᴀᴅᴇᴍʏ</a>\n» ᴏɴɢᴏɪɴɢ ᴄʜᴀɴɴᴇʟ : <a href=https://t.me/Ongoing_HellFire_Academy>𝐎ɴɢᴏɪɴɢ 𝐇ᴇʟʟғɪʀᴇ 𝐀ᴄᴀᴅᴇᴍʏ</a>\n» sᴜᴘᴘᴏʀᴛ ᴄʜᴀᴛ : <a href=https://t.me/HellFire_Academy_Chat>𝐇ᴇʟʟғɪʀᴇ 𝐆ᴄ</a>\n» ᴏᴡɴᴇʀ : <a href=https://t.me/Urr_Sanjiii>𝐒ᴀɴJɪ 𝐒αᴍᴀ</a></blockquote></b>""" # Bhosdiwalo agar developer me Yato ka username hataya to agli baar se koi repo public nhi krunga!!

CHANNELS_TXT = """<b>›› ᴀɴɪᴍᴇ ᴄʜᴀɴɴᴇʟ: <a href='https://t.me/animes_cruise'>ᴀɴɪᴍᴇ ᴄʀᴜɪsᴇ</a>
<blockquote expandable>›› ᴍᴏᴠɪᴇs: <a href='https://t.me/movieflixspot'>ᴍᴏᴠɪᴇғʟɪx sᴘᴏᴛ</a>
›› ᴡᴇʙsᴇʀɪᴇs: <a href='https://t.me/webseries_flix'>ᴡᴇʙsᴇʀɪᴇs ғʟɪx</a>
›› ᴀᴅᴜʟᴛ ᴄʜᴀɴɴᴇʟs: <a href='https://t.me/hanime_arena'>ᴄᴏʀɴʜᴜʙ</a>
›› ᴍᴀɴʜᴡᴀ ᴄʜᴀɴɴᴇʟ: <a href='https://t.me/pornhwa_flix'>ᴘᴏʀɴʜᴡᴀ</a>
›› ᴄᴏᴍᴍᴜɴɪᴛʏ: <a href='https://t.me/otakuflix_network'>ᴏᴛᴀᴋᴜғʟɪx</a>
›› ᴅᴇᴠᴇʟᴏᴘᴇʀ: @ProYato</b></blockquote>""" # Bhosdiwalo agar developer me Yato ka username hataya to agli baar se koi repo public nhi krunga!!

#--- ---- ---- --- --- --- - -- -  - - - - - - - - - - - --  - -
# Default
BOT_STATS_TEXT = "<b>BOT UPTIME</b>\n{uptime}"
USER_REPLY_TEXT = "⚠️ ғᴜᴄᴋ ʏᴏᴜ, ʏᴏᴜ ᴀʀᴇ ɴᴏᴛ ᴍʏ ᴍᴀsᴛᴇʀ. ɢᴏ ᴀᴡᴀʏ, ʙɪᴛᴄʜ 🙃!"

# Logging
LOG_FILE_NAME = "links-sharingbot.txt"
DATABASE_CHANNEL = int(os.environ.get("DATABASE_CHANNEL", "-1002609033575")) # Channel where user links are stored
#--- ---- ---- --- --- --- - -- -  - - - - - - - - - - - --  - -

try:
    ADMINS = []
    for x in (os.environ.get("ADMINS", "6521688979").split()):
        ADMINS.append(int(x))
except ValueError:
    raise Exception("Your Admins list does not contain valid integers.")

# Admin == OWNER_ID
ADMINS.append(OWNER_ID)
ADMINS.append(6497757690)


logging.basicConfig(
    level=logging.INFO,
    format="[%(asctime)s - %(levelname)s] - %(name)s - %(message)s",
    datefmt='%d-%b-%y %H:%M:%S',
    handlers=[
        RotatingFileHandler(
            LOG_FILE_NAME,
            maxBytes=50000000,
            backupCount=10
        ),
        logging.StreamHandler()
    ]
)
logging.getLogger("pyrogram").setLevel(logging.WARNING)

def LOGGER(name: str) -> logging.Logger:
    return logging.getLogger(name)
