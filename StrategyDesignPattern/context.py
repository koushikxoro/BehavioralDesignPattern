from pay import PaymentStrategy
class PaymentContext:
    def __init__(self, strategy:PaymentStrategy):
        self.strategy=strategy
    def set_strategy(self, strategy):
        self.strategy=strategy
    def execute(self,amount):
        self.strategy.pay(amount)