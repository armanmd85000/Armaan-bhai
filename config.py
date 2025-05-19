"""
from os import getenv


API_ID = int(getenv("API_ID", "27006047"))
API_HASH = getenv("API_HASH", "d3bb871aa23eadea02cfb7f462c88a78")
BOT_TOKEN = getenv("BOT_TOKEN", "")
OWNER_ID = int(getenv("OWNER_ID", "1621539522"))
SUDO_USERS = list(map(int, getenv("SUDO_USERS", "1621539522 6839270382").split()))
MONGO_URL = getenv("MONGO_DB", "mongodb+srv://3251celinka:mzCwpCFucgOM0Wp8@cluster0.s1l3cvy.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")

CHANNEL_ID = int(getenv("CHANNEL_ID", "-1002634221784"))
PREMIUM_LOGS = int(getenv("PREMIUM_LOGS", "-1002596449748"))

"""
#




# --------------M----------------------------------

import os
from os import getenv
# ---------------R---------------------------------
API_ID = int(os.environ.get("API_ID"))
# ------------------------------------------------
API_HASH = os.environ.get("API_HASH")
# ----------------D--------------------------------
BOT_TOKEN = os.environ.get("BOT_TOKEN")
# -----------------A-------------------------------
BOT_USERNAME = os.environ.get("BOT_USERNAME")
# ------------------X------------------------------
OWNER_ID = int(os.environ.get("OWNER_ID"))
# ------------------X------------------------------

SUDO_USERS = list(map(int, getenv("SUDO_USERS", "1621539522 6839270382").split()))
# ------------------------------------------------
CHANNEL_ID = int(os.environ.get("CHANNEL_ID"))
# ------------------------------------------------
MONGO_URL = os.environ.get("MONGO_URL")
# -----------------------------------------------
PREMIUM_LOGS = int(os.environ.get("PREMIUM_LOGS"))
