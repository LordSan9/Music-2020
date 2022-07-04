import os

class Config(object):
    API_ID = int(os.environ.get("APP_ID", "19141537"))
    API_HASH = os.environ.get("API_HASH", "c9fcc58ebf42803242c664c5b9c3f8c8")
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "5417336972:AAFdBn-zmbHiZb7GC3jsZdiVvrLgham9ORA")
    STRING_SESSION = os.environ.get("STRING_SESSION", "")
    HEROKU_MODE = os.environ.get("HEROKU_MODE", None)
    BOT_USERNAME = os.environ.get("BOT_USERNAME", "AnDy_MuuSiC_bot")
    SUPPORT = os.environ.get("SUPPORT", "Z888I")
    CHANNEL = os.environ.get("CHANNEL", "X_P13")
    START_IMG = os.environ.get("START_IMG", "https://telegra.ph/file/49b38ffc45115d3b5cb33.jpg")
    CMD_IMG = os.environ.get("CMD_IMG", "https://telegra.ph/file/49b38ffc45115d3b5cb33.jpg")
