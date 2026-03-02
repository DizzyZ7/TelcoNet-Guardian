class SLACalculator:
    @staticmethod
    def calculate(total, failures):
        if total == 0:
            return 100.0
        return round(((total - failures) / total) * 100, 5)
