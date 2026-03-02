from pysnmp.hlapi.asyncio import *
import asyncio

async def snmp_get(host, community, oid):
    iterator = getCmd(
        SnmpEngine(),
        CommunityData(community),
        UdpTransportTarget((host, 161)),
        ContextData(),
        ObjectType(ObjectIdentity(oid))
    )

    errorIndication, errorStatus, errorIndex, varBinds = await iterator

    if errorIndication:
        return None

    for varBind in varBinds:
        return str(varBind[1])
