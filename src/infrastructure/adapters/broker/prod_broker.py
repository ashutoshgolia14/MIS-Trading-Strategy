from execution.ports import BrokerPort

class ProdBroker(BrokerPort):
    def place_order(self, order):
        raise NotImplementedError("Production broker not configured")
