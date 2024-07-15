class Order(object):
    def __init__(self, shipper):
        self._shipper = shipper
    
    # against SRP, as order is about who ordering what
    @property
    def shipper(self):
        return self._shipper