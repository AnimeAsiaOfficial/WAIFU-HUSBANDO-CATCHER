class Config(object):
    LOGGER = True

    # Get this value from my.telegram.org/apps
    OWNER_ID = "5954851332"
    sudo_users = "5954851332", "5954851332"
    GROUP_ID = -1001728318730
    TOKEN = "8197381107:AAFelQI9jBe5PMryuQKZrLaU9Uc6pqGY3ZE"
    mongo_url = "mongodb+srv://HaremDBBot:ThisIsPasswordForHaremDB@haremdb.swzjngj.mongodb.net/?retryWrites=true&w=majority"
    PHOTO_URL = ["https://telegra.ph/file/b925c3985f0f325e62e17.jpg", "https://telegra.ph/file/4211fb191383d895dab9d.jpg"]
    SUPPORT_CHAT = "ANIME_ASIA_OFFICIAL_GROUP"
    UPDATE_CHAT = "ANIME_ASIA_OFFICIAL_GROUP"
    BOT_USERNAME = "WAIFU-HUSBANDO-CATCHER_BOT"
    CHARA_CHANNEL_ID = "-1001767364063"
    api_id = 26626068
    api_hash = "bf423698bcbe33cfd58b11c78c42caa2"

    
class Production(Config):
    LOGGER = True


class Development(Config):
    LOGGER = True
