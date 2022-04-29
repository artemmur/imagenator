import asyncio
import os

import uvicorn

from . import api, app, imagenator


async def server() -> None:
    """Initialize server tasks for running on event loop"""
    tasks: list[asyncio.Task] = [
        asyncio.create_task(
            app.run(
                app=imagenator,
                filename=os.environ.get("APP_CONF", "config.json"),
                mins=float(os.environ.get("APP_DURATION", 60)),
            )
        ),
        asyncio.create_task(
            uvicorn.run(
                api,
                host=os.environ.get("APP_HOST", "0.0.0.0"),
                port=os.environ.get("APP_PORT", 80),
            )
        ),
    ]
    await asyncio.wait(tasks)


def main():
    loop: asyncio.AbstractEventLoop = asyncio.get_event_loop()
    loop.run_until_complete(server())
    loop.close()
