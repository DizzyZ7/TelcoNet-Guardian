import asyncio

async def ping(host: str):
    proc = await asyncio.create_subprocess_exec(
        "ping", "-c", "2", host,
        stdout=asyncio.subprocess.PIPE,
        stderr=asyncio.subprocess.PIPE
    )

    stdout, _ = await proc.communicate()

    if proc.returncode != 0:
        return False

    return True
