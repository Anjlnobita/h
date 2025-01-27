from RishuMusic.core.bot import SACHIN
from RishuMusic.core.dir import dirr
from RishuMusic.core.git import git
#from RishuMusic.core.userbot import Userbot
from RishuMusic.misc import dbb, heroku

from SafoneAPI import SafoneAPI
from .logging import LOGGER

dirr()
git()
dbb()
heroku()

app = SACHIN()
api = SafoneAPI()
#userbot = Userbot()


from .platforms import *

Apple = AppleAPI()
Carbon = CarbonAPI()
SoundCloud = SoundAPI()
Spotify = SpotifyAPI()
Resso = RessoAPI()
Telegram = TeleAPI()
YouTube = YouTubeAPI()
