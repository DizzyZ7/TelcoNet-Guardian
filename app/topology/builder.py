class TopologyBuilder:
    def build_edges(self, devices):
        edges = []
        for device in devices:
            for peer in device.get("peers", []):
                edges.append((device["name"], peer))
        return edges
