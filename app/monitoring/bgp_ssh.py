import asyncio
import asyncssh

class BGPSSHChecker:

    async def check_peer(self, host, username, password):
        async with asyncssh.connect(host, username=username, password=password) as conn:
            result = await conn.run("show ip bgp summary", check=False)

            if "Established" in result.stdout:
                return True
            return False
