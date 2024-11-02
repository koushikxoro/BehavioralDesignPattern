from pay import PaymentStrategy
class CreditCardPayement(PaymentStrategy):
    def pay(self, amount):
        print(f"Paying {amount} by credit card.")