#ALL FILES UPLOADED - CREDITS 🌟 - @Sunrises_24
import re
from os import environ
import os

id_pattern = re.compile(r'^.\d+$')


API_ID = os.environ.get("API_ID", "13992749")
API_HASH = os.environ.get("API_HASH", "c8b1a7c3ce9aa1d1eec2fee774d48399")
BOT_TOKEN = os.environ.get("BOT_TOKEN", "7327637614:AAHBgQ7USiVKjJx5vtgL3VB9V9Jb3IP1lic")
ADMIN = int(os.environ.get("ADMIN", '5466885993'))
FSUB_UPDATES = os.environ.get("FSUB_CHANNEL", "")
FSUB_GROUP = os.environ.get("FSUB_GROUP", "")
DATABASE_URI = os.environ.get("DATABASE_URI", "mongodb+srv://KR:KR@cluster0.gsa64.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
DATABASE_NAME = os.environ.get("DATABASE_NAME", "ravikumar1cn")
CAPTION = os.environ.get("CAPTION", "")
group = environ.get('GROUP', '-1002169459595')
GROUP = int(group) if group and id_pattern.search(group) else None
#ALL FILES UPLOADED - CREDITS 🌟 - @Sunrises_24
SUNRISES_PIC= "https://graph.org/file/bd91761f6e938e2e6d23a.jpg"  # Replace with your Telegraph link
AUTH_USERS = int(os.environ.get("AUTH_USERS", '5466885993'))
WEBHOOK = bool(os.environ.get("WEBHOOK", True))
PORT = int(os.environ.get("PORT", "8080"))
LOG_CHANNEL_ID = os.environ.get("LOG_CHANNEL_ID", -1001913629397)
