# Safe-repo
# Note if you are trying to deploy on vps then directly fill values in ("")

from os import getenv

API_ID = int(getenv("API_ID", "25713846"))
API_HASH = getenv("API_HASH", "ca57c019f37ab7bf0bd9caead4846c88")
BOT_TOKEN = getenv("BOT_TOKEN", "7269627262:AAH6oVfd4ONGBkHr_N1hpYZ0OgMNVfO0mN8")
OWNER_ID = int(getenv("OWNER_ID", "6750546542"))
MONGODB_CONNECTION_STRING = getenv("MONGO_DB", "mongodb+srv://tvvt680:xfiV6ktxfGG4IZk2@cluster0.athjl.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
LOG_GROUP = int(getenv("LOG_GROUP", "-1002458368001"))
FORCESUB = getenv("FORCESUB", "funnyzilla")
DEFAULT_SESSION = getenv("DEFAULT_SESSION", "") # fill this only if you dont want to force your subscriber to login by this they can use the old method of invite link and can extract from public without login
