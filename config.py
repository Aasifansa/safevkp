# Safe-repo
# Note if you are trying to deploy on vps then directly fill values in ("")

from os import getenv

API_ID = int(getenv("API_ID", "20901045"))
API_HASH = getenv("API_HASH", "dec03cafafbd892b285499762a896082")
BOT_TOKEN = getenv("BOT_TOKEN", "7750523801:AAEvAdBjuxPnB8bky1cifgFeLuMuvTVANME")
OWNER_ID = int(getenv("OWNER_ID", "6324457826"))
MONGODB_CONNECTION_STRING = getenv("MONGO_DB", "mongodb+srv://Anokha:dbLifeline@cluster0.fvmpg.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
LOG_GROUP = int(getenv("LOG_GROUP", "-1002238401216"))
FORCESUB = getenv("FORCESUB", "funnyzilla")
DEFAULT_SESSION = getenv("DEFAULT_SESSION", "") # fill this only if you dont want to force your subscriber to login by this they can use the old method of invite link and can extract from public without login
