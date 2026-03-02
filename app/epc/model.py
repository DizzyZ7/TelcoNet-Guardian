class EPCNode:
    def __init__(self, name, ip, role):
        self.name = name
        self.ip = ip
        self.role = role  # MME, SGW, PGW, HSS, PCRF
