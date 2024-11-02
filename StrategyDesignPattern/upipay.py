from pay import PaymentStrategy
class UPIPay(PaymentStrategy):
    def pay(self, amount):
        print(f"Paying {amount} by UPI.")