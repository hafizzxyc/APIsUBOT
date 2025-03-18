# Credits: @mrismanaziz
# Copyright (C) 2022 Pyro-ManUserbot
#
# This file is a part of < https://github.com/mrismanaziz/PyroMan-Userbot/ >
# PLease read the GNU Affero General Public License in
# <https://www.github.com/mrismanaziz/PyroMan-Userbot/blob/main/LICENSE/>.
#
# t.me/SharingUserbot & t.me/Lunatic0de

from os import getenv

from dotenv import load_dotenv

load_dotenv("config.env")


API_HASH = getenv("4e16cd70d2e415745d0b272d42f3f792")
API_ID = int(getenv("API_ID", "22624775"))
BLACKLIST_CHAT = getenv("BLACKLIST_CHAT", None)
if not BLACKLIST_CHAT:
    BLACKLIST_CHAT = [-1001473548283]
BLACKLIST_GCAST = {int(x) for x in getenv("BLACKLIST_GCAST", "").split()}
BOTLOG_CHATID = int(getenv("BOTLOG_CHATID") or 0)
BOT_VER = "0.2.0@main"
BRANCH = getenv("BRANCH", "main")
CHANNEL = getenv("CHANNEL", "aapiiiscodes")
CMD_HANDLER = getenv("CMD_HANDLER", ".")
DB_URL = getenv("DATABASE_URL", "")
GIT_TOKEN = getenv("GIT_TOKEN", "")
GROUP = getenv("GROUP", "xbeggars")
HEROKU_API_KEY = getenv("HEROKU_API_KEY", None)
HEROKU_APP_NAME = getenv("HEROKU_APP_NAME", None)
PMPERMIT_PIC = getenv("PMPERMIT_PIC", None)
REPO_URL = getenv("REPO_URL", "Yatom")
STRING_SESSION1 = getenv("STRING_SESSION1", "BQFZOgcAT_LHs_zp0H9062d_03X3KgGjmGeqqJr5ph1rxUC1g7BE0PLieCLq9Bb0CGOGzmQyMyv86GP_1R0j82Krd64GgXPS32y0liHoL-3F1uwRz38ZDQH13BHzoZQnuTL6vLycnD3zUy7DhbmncJIpVdxSaApZdzPzu7UD50N368nu38NZNT_hF8qNR9FCTW4lig8aum3_lXpK-7vRzUihvYJ8p2ZJxHlsBxkcOAec64pqTltnam2U0l4lBecQz57ELLgtmCjVK8aCssUKeiFCO9C16e0IgwD8TwO0V_C03RNwXYx0jW-hRDtZr4gtkBB5aBRpyh0QBOb-6Goai8Go_82X1QAAAAFQ67G8AA")
STRING_SESSION2 = getenv("STRING_SESSION2", "")
STRING_SESSION3 = getenv("STRING_SESSION3", "")
STRING_SESSION4 = getenv("STRING_SESSION4", "")
STRING_SESSION5 = getenv("STRING_SESSION5", "")
SUDO_USERS = list(map(int, getenv("SUDO_USERS", "").split()))
