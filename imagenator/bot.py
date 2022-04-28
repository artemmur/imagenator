import json
import typing

import requests


def encode(message: str) -> str:
    """Encode special characters"""
    return message.replace(r"-", r"\-").replace(r"_", r"\_").replace(r"*", r"\*")


class Bot:
    """VK Teams api wrapper"""

    def send(self, to, message):
        """Send message to VK teams chat"""
        params = {
            "token": self.token,
            "chatId": to,
            "text": message,
            "parseMode": "MarkdownV2",
        }
        r: requests.Response = requests.get(self.send_text_url, params=params)
        if r.status_code != 200:
            print(f"failed response code from vk teams api: {r.status_code}")

        resp: typing.Any = r.json()
        if not resp.get("ok", False):
            print(f"cannot send message {message} to chat {to}" f"{json.dumps(resp)}")
