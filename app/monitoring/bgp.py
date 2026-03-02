from app.monitoring.tcp import check_tcp

async def check_bgp(host: str):
    return await check_tcp(host, 179)
