# +++ Edited By Gojo [telegram username: @DoraShin_hlo] 
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
TEXT = environ.get("APPROVED_WELCOME_TEXT", "<b>{mention},\n\nʏᴏᴜʀ ʀᴇǫᴜᴇsᴛ ᴛᴏ ᴊᴏɪɴ {title} ɪs ᴀᴘᴘʀᴏᴠᴇᴅ.\n\‣ ᴘᴏᴡᴇʀᴇᴅ ʙʏ @HellFire_Academy</b>")
APPROVED = environ.get("APPROVED_WELCOME", "on").lower()

# Default
TG_BOT_WORKERS = int(os.environ.get("TG_BOT_WORKERS", "40"))
#--- ---- ---- --- --- --- - -- -  - - - - - - - - - - - --  - -

# Start pic
START_PIC_FILE_ID = "https://telegra.ph/file/f3d3aff9ec422158feb05-d2180e3665e0ac4d32.jpg"
START_IMG = "https://telegra.ph/file/f3d3aff9ec422158feb05-d2180e3665e0ac4d32.jpg"
# Messages
START_MSG = os.environ.get("START_MESSAGE", "<b>ᴡᴇʟᴄᴏᴍᴇ ᴛᴏ ᴛʜᴇ ᴀᴅᴠᴀɴᴄᴇᴅ ʟɪɴᴋs sʜᴀʀɪɴɢ ʙᴏᴛ. ᴡɪᴛʜ ᴛʜɪs ʙᴏᴛ, ʏᴏᴜ ᴄᴀɴ sʜᴀʀᴇ ʟɪɴᴋs ᴀɴᴅ ᴋᴇᴇᴘ ʏᴏᴜʀ ᴄʜᴀɴɴᴇʟs sᴀғᴇ ғʀᴏᴍ ᴄᴏᴘʏʀɪɢʜᴛ ɪssᴜᴇs.\n\n<blockquote>‣ ᴘᴏᴡᴇʀᴇᴅ ʙʏ : <a href='https://t.me/HellFire_Academy'>𝐇ᴇʟʟғɪʀᴇ 𝐀ᴄᴀᴅᴇᴍʏ</a></blockquote></b>")
HELP = os.environ.get("HELP_MESSAGE", "<b><blockquote expandable>» Owner: <a href=https://t.me/DoraShin_hlo>Gojo</a>\n» Our Community: <a href=https://t.me/HellFire_Academy>HellFire Academy</a>\n» Ongoing Anime Channel: <a href=https://t.me/Ongoing_HellFire_Academy>Ongoing HellFire Academy</a></b>")
ABOUT = os.environ.get("ABOUT_MESSAGE", "<b><blockquote expandable>This bot is developed for link provide to securely share Telegram channel links with temporary invite links, protecting your channels from copyright issues.</b>")

ABOUT_TXT = """<b>›› ᴄᴏᴍᴍᴜɴɪᴛʏ: <a href='https://t.me/HellFire_Academy'>𝐇ᴇʟʟғɪʀᴇ 𝐀ᴄᴀᴅᴇᴍʏ</a>
<blockquote expandable>›› ᴜᴘᴅᴀᴛᴇs ᴄʜᴀɴɴᴇʟ: <a href='https://t.me/Adult_Flux'>Cʟɪᴄᴋ ʜᴇʀᴇ</a>
›› ᴏᴡɴᴇʀ: <a href='https://t.me/DoraShin_hlo'>Gojo</a>
›› Main Channel: <a href='https://t.me/HellFire_Academy>Click Here</a>
›› Adult: <a href='https://t.me/Adult_Flux>Adult_Flux</a>"""

CHANNELS_TXT = "\u203A\u203A ᴀɴɪᴍᴇ ᴄʜᴀɴɴᴇʟ: <a href='https://t.me/HellFire_Academy'>𝐇ᴇʟʟғɪʀᴇ 𝐀ᴄᴀᴅᴇᴍʏ</a>"
<blockquote expandable>›› ᴍᴏᴠɪᴇs: <a href='https://t.me/Hellfire_Movies'>ᴍᴏᴠɪᴇ sᴘᴏᴛ</a>
›› ᴡᴇʙsᴇʀɪᴇs: <a href='https://t.me/HellFire_Movies'>ᴡᴇʙsᴇʀɪᴇs</a>
›› ᴀᴅᴜʟᴛ ᴄʜᴀɴɴᴇʟs: <a href='https://t.me/Adult_Flux'>ᴄᴏʀɴʜᴜʙ</a>
›› ᴍᴀɴʜᴡᴀ ᴄʜᴀɴɴᴇʟ: <a href='https://t.me/Adult_Flux'>ᴘᴏʀɴʜᴡᴀ</a>
›› ᴄᴏᴍᴍᴜɴɪᴛʏ: <a href='https://t.me/HellFire_Network'>HellFire Network</a>

#--- ---- ---- --- --- --- - -- -  - - - - - - - - - - - --  - -
# Default
BOT_STATS_TEXT = "<b>BOT UPTIME</b>\n{uptime}"
USER_REPLY_TEXT = "⚠️ ғᴜᴄᴋ ʏᴏᴜ, ʏᴏᴜ ᴀʀᴇ ɴᴏᴛ ᴍʏ ᴍᴀsᴛᴇʀ. ɢᴏ ᴀᴡᴀʏ, 🙃!"

# Logging
LOG_FILE_NAME = "links-sharingbot.txt"
DATABASE_CHANNEL = int(os.environ.get("DATABASE_CHANNEL", "")) # Channel where user links are stored
#--- ---- ---- --- --- --- - -- -  - - - - - - - - - - - --  - -

try:
    ADMINS = []
    for x in (os.environ.get("ADMINS", "6497757690").split()):
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
