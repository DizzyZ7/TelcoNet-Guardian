class SLATracker:
    def __init__(self):
        self.total = 0
        self.failures = 0

    def record(self, success: bool):
        self.total += 1
        if not success:
            self.failures += 1
