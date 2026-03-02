import asyncio

async def check_tcp(host: str, port: int):
    try:
        reader, writer = await asyncio.open_connection(host, port)
        writer.close()
        await writer.wait_closed()
        return True
    except:
        return False
