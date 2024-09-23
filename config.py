# Safe-repo
# Note if you are trying to deploy on vps then directly fill values in ("")

from os import getenv

API_ID = int(getenv("API_ID", "27662412"))
API_HASH = getenv("API_HASH", "4a695060ecd737dffa9e92c540b46ed2")
BOT_TOKEN = getenv("BOT_TOKEN", "7574299453:AAH3V90TNu8Wn1a8xEuiVrto-NdIGWrEBD0")
OWNER_ID = int(getenv("OWNER_ID", "6847319298"))
MONGODB_CONNECTION_STRING = getenv("MONGO_DB", "mongodb+srv://Mrkiller:<dbAlone765592@cluster0.xwi48.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
LOG_GROUP = int(getenv("LOG_GROUP", "-1002220096661"))
FORCESUB = getenv("FORCESUB", "Luckyhub2y637")
DEFAULT_SESSION = getenv("DEFAULT_SESSION", "") # fill this only if you dont want to force your subscriber to login by this they can use the old method of invite link and can extract from public without login
