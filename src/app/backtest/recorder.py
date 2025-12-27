class BacktestRecorder:
    def __init__(self):
        self.ticks = 0
        self.executions = []

    def record_tick(self):
        self.ticks += 1

    def record_execution(self, result, ts):
        self.executions.append({'ts': ts, 'status': result.status.value, 'fill_price': result.fill_price, 'reason': result.reason})
