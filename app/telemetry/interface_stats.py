from pysnmp.hlapi.asyncio import *

IF_OPER_STATUS = "1.3.6.1.2.1.2.2.1.8"

async def get_interface_status(host, community):
    iterator = getCmd(
        SnmpEngine(),
        CommunityData(community),
        UdpTransportTarget((host, 161)),
        ContextData(),
        ObjectType(ObjectIdentity(IF_OPER_STATUS))
    )

    errorIndication, errorStatus, errorIndex, varBinds = await iterator

    if errorIndication:
        return None

    return str(varBinds[0][1])
