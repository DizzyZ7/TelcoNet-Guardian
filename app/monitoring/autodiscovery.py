import asyncio
from app.monitoring.snmp import snmp_get

SYS_NAME_OID = "1.3.6.1.2.1.1.5.0"

async def discover_device(host, community):
    name = await snmp_get(host, community, SYS_NAME_OID)
    if name:
        return {"host": host, "name": name}
    return None
