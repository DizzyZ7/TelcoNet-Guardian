class VLANValidator:
    def validate(self, vlans):
        return len(vlans) == len(set(vlans))
