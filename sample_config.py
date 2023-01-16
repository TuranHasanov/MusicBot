import os


class Config(object):
    TG_BOT_TOKEN = os.environ.get("TG_BOT_TOKEN", "5970347980:AAEsHZjkymj2IYJG36TfO6P8hhyb8gL3MsY")

    APP_ID = int(os.environ.get("APP_ID", 6473933))

    API_HASH = os.environ.get("API_HASH", "999a64e43ef2d4dc98af4ef69ccd7ade")
