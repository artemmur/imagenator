import json

from . import bot, detector, image
from .settings import CHAT_ID


class ScanException(BaseException):
    """Raise when error during scanning image"""


class App:
    def __init__(
        self, bot: bot.Bot, image: image.Image, detector: detector.Detector
    ) -> None:
        self.bot = bot
        self.detector = detector
        self.image = image

    def scan(self, image: str) -> None:
        """Scan image for vulnerabilities and publish result"""
        if not image:
            return

        vulnerabilities: list[detector.Vulnerability] = self.detector.check(
            self.image.decompose(image)
        )
        if len(vulnerabilities) == 0:
            self.bot.send(
                CHAT_ID, f"*Vulnerabilities wasn't detected in image  💮*\n```{image}```"
            )
            return

        message: str = f"{image} is vulnerable ⛔️\n\n"
        for vulnerability in vulnerabilities:
            message += str(vulnerability)
        self.bot.send(CHAT_ID, message)
        return


async def run(app: App, filename: str) -> None:
    """Start shedule job"""
    while True:
        data: dict = dict()
        with open(filename, "r") as f:
            data = json.load(f)

        for image in data.get("images", []):
            try:
                app.scan(image)
            except:
                print(f"error while scanning {image}")
