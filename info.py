# This code has been modified by @Safaridev
# Please do not remove this credit
import re
import os
from os import environ, getenv
from Script import script 

id_pattern = re.compile(r'^.\d+$')

def is_enabled(value, default):
    if value.lower() in ["true", "yes", "1", "enable", "y"]:
        return True
    elif value.lower() in ["false", "no", "0", "disable", "n"]:
        return False
    else:
        return default


# Bot information
SESSION = environ.get('SESSION', 'Media_search')
API_ID = int(environ.get('API_ID', ""))
API_HASH = environ.get('API_HASH', "")
BOT_TOKEN = environ.get('BOT_TOKEN', "7586120356:AAGHkqHZJb_Su2juzXOBbmVBT3AecjhNpbs")
TIMEZONE = environ.get("TIMEZONE", "Asia/Kolkata")

# Bot settings
CACHE_TIME = int(environ.get('CACHE_TIME', 300))
USE_CAPTION_FILTER = is_enabled((environ.get('USE_CAPTION_FILTER', 'True')), True)
PICS = (environ.get('PICS', 'https://telegra.ph/file/0ed351c8605c23e8cae79.jpg https://telegra.ph/file/6524270c008b60f81f30a.jpg https://telegra.ph/file/848ed57090fd5111ce64d.jpg https://telegra.ph/file/5fe959d96fcc33d1b9dc9.jpg https://telegra.ph/file/ec5f5a031b7826e28360c.jpg https://telegra.ph/file/aa4b77441bb41cfce12d7.jpg https://telegra.ph/file/00ed60e2c89d564d850ef.jpg https://telegra.ph/file/a5d518f6020976bc45264.jpg https://telegra.ph/file/650191ad1f813ca8f41cb.jpg https://telegra.ph/file/c6042704a1bc0a2b52996.jpg https://telegra.ph/file/9d68211fa9dcb208200be.jpg')).split()
WELCOME_VID = environ.get("WELCOME_VID", "https://telegra.ph/file/451f038b4e7c2ddd10dc0.mp4")

#premium imag
REFFER_PIC = environ.get('REFFER_PIC', 'https://graph.org/file/f75feb19aece0d4badefd.jpg')
PREMIUM_PIC = environ.get('SUBSCRIPTION', 'https://i.imghippo.com/files/wPdPK1726559453.jpg')
QR_CODE = environ.get('QR_CODE', 'https://envs.sh/GoQ.jpg') # Scanner Code image 
#refer time, or feffer count
REFERAL_TIME = int(environ.get('REFERAL_USER_TIME', "2592000")) # set in seconds | already seted 1 month premium
REFFER_POINT = int(environ.get('USER_POINT', "50")) # Set Referel point Count 
#premium Users Satuts
premium = environ.get('PREMIUM_LOGS', '-1002186335716')
PREMIUM_LOGS = int(premium) if premium and id_pattern.search(premium) else None
# lock file, set file limit 
FILE_LIMITE = int(environ.get('FILE_LIMITE', 3))
SEND_ALL_LIMITE = int(environ.get('SEND_ALL_LIMITE', 3))
LIMIT_MODE = is_enabled((environ.get('LIMIT_MODE', 'True')), False)

# Admins, Channels & Users
ADMINS = [int(admin) if id_pattern.search(admin) else admin for admin in environ.get('ADMINS', '1798348973').split()]
OWNER_USER_NAME = environ.get("OWNER_USER_NAME", "looterekrish") # widout 👉 @
CHANNELS = [int(ch) if id_pattern.search(ch) else ch for ch in environ.get('CHANNELS', '-1002087964739').split()]
# post channel auto post new movie
POST_CHANNELS = list(map(int, (channel.strip() for channel in environ.get('POST_CHANNELS', '-1002148604082').split(','))))
AUTH_CHANNEL = int(environ.get('AUTH_CHANNEL', '-1002023191399'))
AUTH_REQ_CHANNEL = int(environ.get('AUTH_REQ_CHANNEL', '-1002177424257'))
NO_RESULTS_MSG = is_enabled((environ.get("NO_RESULTS_MSG", 'True')), False)

# MongoDB information
DATABASE_URI = environ.get('DATABASE_URI', "mongodb+srv://Cluster0:q6Jwo214NcB7LCsm@cluster0.jxby6.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
DATABASE_NAME = environ.get('DATABASE_NAME', "Cluster0")
COLLECTION_NAME = environ.get('COLLECTION_NAME', 'Safaribotts')

#stream link shortner
STREAM_SITE = (environ.get('STREAM_SITE', 'sharedisklinks.com'))
STREAM_API = (environ.get('STREAM_API', '587f94f0e0b1813a52aed61290af6ea79d6ee464'))
STREAM_HTO = (environ.get('STREAMHTO', 'https://t.me/Hoe/69'))
STREAM_MODE = is_enabled((environ.get('STREAM_MODE', "False")), False)


#verify site api and url
IS_VERIFY = is_enabled((environ.get('IS_VERIFY', 'False')), False)
VERIFY_IMG = environ.get("VERIFY_IMG", "https://graph.org/file/1669ab9af68eaa62c3ca4.jpg")
VERIFY_URL = environ.get('VERIFY_URL', 'https://shortxlinks.com')
VERIFY_API = (environ.get('VERIFY_API', '99d89644e3049653b4b838934bf78d1b6024472d'))

TWO_VERIFY_GAP = int(environ.get('TWO_VERIFY_GAP', "600"))
VERIFY_URL2 = environ.get('VERIFY_URL2', 'https://shortxlinks.com')
VERIFY_API2 = (environ.get('VERIFY_API2', '99d89644e3049653b4b838934bf78d1b6024472d'))
 
THIRD_VERIFY_GAP = int(environ.get('THIRD_VERIFY_GAP', "600"))
VERIFY_URL3 = environ.get('VERIFY_URL3', 'https://shortxlinks.com')
VERIFY_API3 = (environ.get('VERIFY_API3', '99d89644e3049653b4b838934bf78d1b6024472d'))
 
TUTORIAL = environ.get('TUTORIAL', 'https://t.me/c/2265223323/2')
TUTORIAL2 = environ.get('TUTORIAL2', 'https://t.me/c/2265223323/2')
TUTORIAL3 = environ.get('TUTORIAL3', 'https://t.me/c/2265223323/2')

# auto files delete
AUTO_FILE_DELETE = is_enabled((environ.get('AUTO_FILE_DELETE', "True")), False)

DELETE_CHANNELS = [int(dch) if id_pattern.search(dch) else dch for dch in environ.get('DELETE_CHANNELS', '-1001998895377').split()]
MAX_B_TN = environ.get("MAX_B_TN", "7")
MAX_BTN = is_enabled((environ.get('MAX_BTN', "True")), True)
PORT = environ.get("PORT", "8080")
GRP_LNK = environ.get('GRP_LNK', 'https://t.me/+FJGHmYjZ4vFlNmQ1')
CHNL_LNK = environ.get('CHNL_LNK', 'https://t.me/rkmovieszip')
MSG_ALRT = environ.get('MSG_ALRT', 'Wʜᴀᴛ Aʀᴇ Yᴏᴜ Lᴏᴏᴋɪɴɢ Aᴛ ?')
LOG_CHANNEL = int(environ.get('LOG_CHANNEL', -1002186335716))
GROUP_VERIFY_LOGS = int(environ.get('GROUP_VERIFY_LOGS', -1002186335716)) # Group verify stats 
REQ_CHANNEL = int(environ.get('REQ_CHANNEL', -1002177424257)) # movies request channel, else log channel
SUPPORT_CHAT = environ.get('SUPPORT_CHAT', 'Jhwjwp')
IMDB = is_enabled((environ.get('IMDB', "True")), True)
AUTO_FFILTER = is_enabled((environ.get('AUTO_FFILTER', "True")), True)
AUTO_DELETE = is_enabled((environ.get('AUTO_DELETE', "True")), True)
PM_FILTER = is_enabled((environ.get('PM_FILTER', "True")), False)

SINGLE_BUTTON = is_enabled((environ.get('SINGLE_BUTTON', "True")), True)
CUSTOM_FILE_CAPTION = environ.get("CUSTOM_FILE_CAPTION", f"{script.CAPTION}")
IMDB_TEMPLATE = environ.get("IMDB_TEMPLATE", f"{script.IMDB_TEMPLATE_TXT}")
LONG_IMDB_DESCRIPTION = is_enabled(environ.get("LONG_IMDB_DESCRIPTION", "False"), False)
SPELL_CHECK_REPLY = is_enabled(environ.get("SPELL_CHECK_REPLY", "True"), True)
MAX_LIST_ELM = environ.get("MAX_LIST_ELM", None)
INDEX_REQ_CHANNEL = int(environ.get('INDEX_REQ_CHANNEL', LOG_CHANNEL))
MELCOW_NEW_USERS = is_enabled((environ.get('MELCOW_NEW_USERS', "True")), True)

REACTION = ["🔥", "❤️", "😍", "⚡", "👍", "❤", "🔥", "🥰", "👏", "😁", "🎉", "🤩", "🙏", "👌", "🕊", "❤‍🔥", "⚡", "😇", "🤗", "😘", "🙊", "😎"]

# Streaming
BIN_CHANNEL = int(environ.get("BIN_CHANNEL", "-1002263971223")) 
PORT = int(environ.get('PORT', 8080))
NO_PORT = bool(environ.get('NO_PORT', False))
APP_NAME = None
if 'DYNO' in environ:
    ON_HEROKU = True
    APP_NAME = environ.get('APP_NAME')
else:
    ON_HEROKU = False
BIND_ADRESS = str(getenv('WEB_SERVER_BIND_ADDRESS', '0.0.0.0'))
FQDN = str(getenv('FQDN', BIND_ADRESS)) if not ON_HEROKU or getenv('FQDN') else APP_NAME+'.herokuapp.com'
URL = "https://{}/".format(FQDN) if ON_HEROKU or NO_PORT else \
    "https://{}:{}/".format(FQDN, PORT)
SLEEP_THRESHOLD = int(environ.get('SLEEP_THRESHOLD', '60'))
WORKERS = int(environ.get('WORKERS', '4'))
SESSION_NAME = str(environ.get('SESSION_NAME', 'safaribotts'))
MULTI_CLIENT = False
name = str(environ.get('name', 'safaribotts'))
PING_INTERVAL = int(environ.get("PING_INTERVAL", "1200"))  # 20 minutes
if 'DYNO' in environ:
    ON_HEROKU = True
    APP_NAME = str(getenv('APP_NAME'))

else:
    ON_HEROKU = False
HAS_SSL=bool(getenv('HAS_SSL',False))
if HAS_SSL:
    URL = "https://{}/".format(FQDN)
else:
    URL = "https://{}/".format(FQDN)

LOG_STR = "Current Cusomized Configurations are:-\n"
LOG_STR += ("IMDB Results are enabled, Bot will be showing imdb details for you queries.\n" if IMDB else "IMBD Results are disabled.\n")
LOG_STR += ("SINGLE_BUTTON is Found, filename and files size will be shown in a single button instead of two separate buttons\n" if SINGLE_BUTTON else "SINGLE_BUTTON is disabled , filename and file_sixe will be shown as different buttons\n")
LOG_STR += (f"CUSTOM_FILE_CAPTION enabled with value {CUSTOM_FILE_CAPTION}, your files will be send along with this customized caption.\n" if CUSTOM_FILE_CAPTION else "No CUSTOM_FILE_CAPTION Found, Default captions of file will be used.\n")
LOG_STR += ("Long IMDB storyline enabled." if LONG_IMDB_DESCRIPTION else "LONG_IMDB_DESCRIPTION is disabled , Plot will be shorter.\n")
LOG_STR += ("Spell Check Mode Is Enabled, bot will be suggesting related movies if movie not found\n" if SPELL_CHECK_REPLY else "SPELL_CHECK_REPLY Mode disabled\n")
LOG_STR += (f"MAX_LIST_ELM Found, long list will be shortened to first {MAX_LIST_ELM} elements\n" if MAX_LIST_ELM else "Full List of casts and crew will be shown in imdb template, restrict them by adding a value to MAX_LIST_ELM\n")
LOG_STR += f"Your current IMDB template is {IMDB_TEMPLATE}"

