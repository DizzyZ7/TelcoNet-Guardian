import asyncio
import uvicorn

from app.config import load_config
from app.logger import setup_logger
from app.monitoring.ping import ping
from app.monitoring.snmp import snmp_get
from app.sla.tracker import SLATracker
from app.sla.calculator import SLACalculator
from app.integrations.prometheus import start, update_ping, update_sla
from app.api.rest import app as api_app

tracker = SLATracker()

async def monitor():
    config = load_config()
    logger = setup_logger()

    while True:
        for device in config["devices"]:
            host = device["ip"]

            status = await ping(host)
            tracker.record(status)
            update_ping(host, status)

            logger.info(f"{host} status={status}")

        sla_value = SLACalculator.calculate(tracker.total, tracker.failures)
        update_sla("core_network", sla_value)

        await asyncio.sleep(15)

async def main():
    start()
    asyncio.create_task(monitor())

    server = uvicorn.Server(
        uvicorn.Config(api_app, host="0.0.0.0", port=8000)
    )
    await server.serve()

if __name__ == "__main__":
    asyncio.run(main())
