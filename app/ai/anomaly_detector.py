import statistics

class AnomalyDetector:

    def detect(self, values):
        if len(values) < 5:
            return False

        mean = statistics.mean(values)
        stdev = statistics.stdev(values)

        latest = values[-1]

        if latest > mean + 3 * stdev:
            return True

        return False
