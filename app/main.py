# app/main.py
import asyncio
import uvicorn

from app.config import load_config
from app.logger import setup_logger
from app.monitoring.ping import ping
from app.monitoring.bgp import check_bgp
from app.integrations.prometheus_exporter import (
    start_exporter,
    update_ping,
    update_bgp
)
from app.integrations.telegram import TelegramNotifier
from app.api.rest import app as api_app

async def monitor_loop():
    config = load_config()
    logger = setup_logger()

    telegram = TelegramNotifier(
        config["telegram"]["token"],
        config["telegram"]["chat_id"]
    )

    while True:
        for device in config["devices"]:
            host = device["ip"]

            ping_status = await ping(host)
            bgp_status = await check_bgp(host)

            update_ping(host, ping_status)
            update_bgp(host, bgp_status)

            if not ping_status:
                await telegram.send(f"❌ {host} is DOWN")

            logger.info(f"{host} | ping={ping_status} | bgp={bgp_status}")

        await asyncio.sleep(10)

async def main():
    start_exporter()
    asyncio.create_task(monitor_loop())
    config = uvicorn.Config(api_app, host="0.0.0.0", port=8000)
    server = uvicorn.Server(config)
    await server.serve()

if __name__ == "__main__":
    asyncio.run(main())
