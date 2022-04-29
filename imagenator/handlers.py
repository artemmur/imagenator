from fastapi import status
from pydantic.dataclasses import dataclass

from . import api, imagenator


@dataclass
class Image:
    url: str


@api.post("/jobs", status_code=status.HTTP_201_CREATED)
async def scan(image: Image):
    """Webhook for scan OCI image"""
    imagenator.send(f"Start scanning image {image.url}")
    try:
        imagenator.scan(image.url)
    except:
        print("error while scanning image request: {image.url}")


@api.get("/ping", status_code=status.HTTP_200_OK)
def healthcheck():
    return
