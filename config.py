from os import getenv
from dotenv import load_dotenv

load_dotenv()

class Config:
    def __init__(self):
        self.API_ID = int(getenv("32616094", 0))
        self.API_HASH = getenv("af7f796ad3420c7fe6d17220b0dee0c5")

        self.BOT_TOKEN = getenv("8271417279:AAFUUFysn9UnWwI8m05LyllrtDYAn88Jil4")
        self.MONGO_URL = getenv("mongodb+srv://hal588869_db_user:h1XR9uuemLaTyz60@cluster0.qumwxdg.mongodb.net/?appName=Cluster0")

        self.LOGGER_ID = int(getenv("BQHxrp4Ald6OY8NOAU4uuHYv3O3IAEG-b0YYko_qTFxfi_G0JQ0gtDt90kqC064-hCTTvutMF-UKph5VeMUoopIE46kD3QQPz1HPXAe9UNTHIVPseuz2P11UwS5shD1cNjue39s49-ZzTPtGdPMo2MzTZsvS-XbzxHegam9t_Jrl8a6ZiPobDmseQ42Sny7doVdlRO-Zw680KfbGLCydKYCTaY3rGHIxFHrQ9JpL4OizxsLKAu1Sy11S04VFh48NV5hpaVS3nvPmkkNZTMuLFagzeGQv9PmdYTSId3V2_-EZRD-ORwE9OzXQASBvuZ7IlsJgPlTWSpe4b0McWTIhxgfdg7LUsQAAAAGpPgGJAA", 0))
        self.OWNER_ID = int(getenv("7134380425", 0))

        self.DURATION_LIMIT = int(getenv("DURATION_LIMIT", 60)) * 60
        self.QUEUE_LIMIT = int(getenv("QUEUE_LIMIT", 20))
        self.PLAYLIST_LIMIT = int(getenv("PLAYLIST_LIMIT", 20))

        self.SESSION1 = getenv("SESSION", None)
        self.SESSION2 = getenv("SESSION2", None)
        self.SESSION3 = getenv("SESSION3", None)

        self.SUPPORT_CHANNEL = getenv("SUPPORT_CHANNEL", "https://t.me/FallenAssociation")
        self.SUPPORT_CHAT = getenv("SUPPORT_CHAT", "https://t.me/DevilsHeavenMF")

        self.AUTO_LEAVE: bool = getenv("AUTO_LEAVE", "False").lower() == "true"
        self.AUTO_END: bool = getenv("AUTO_END", "False").lower() == "true"
        self.THUMB_GEN: bool = getenv("THUMB_GEN", "True").lower() == "true"
        self.VIDEO_PLAY: bool = getenv("VIDEO_PLAY", "True").lower() == "true"
        self.COOKIES_URL = [
            url for url in getenv("COOKIES_URL", "").split(" ")
            if url and "batbin.me" in url
        ]
        self.DEFAULT_THUMB = getenv("DEFAULT_THUMB", "https://te.legra.ph/file/3e40a408286d4eda24191.jpg")
        self.PING_IMG = getenv("PING_IMG", "https://files.catbox.moe/haagg2.png")
        self.START_IMG = getenv("START_IMG", "https://files.catbox.moe/zvziwk.jpg")

    def check(self):
        missing = [
            var
            for var in ["API_ID", "API_HASH", "BOT_TOKEN", "MONGO_URL", "LOGGER_ID", "OWNER_ID", "SESSION1"]
            if not getattr(self, var)
        ]
        if missing:
            raise SystemExit(f"Missing required environment variables: {', '.join(missing)}")
