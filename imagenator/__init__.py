from fastapi import FastAPI

from .app import App
from .bot import Bot
from .detector import Detector
from .image import Image
from .settings import BOT_TOKEN

imagenator: App = App(bot=Bot(token=BOT_TOKEN), image=Image(), detector=Detector())
api: FastAPI = FastAPI()
