from app.monitoring.ping import ping

class EPCValidator:
    async def validate(self, nodes):
        results = {}
        for node in nodes:
            status = await ping(node.ip)
            results[node.name] = status
        return results
