from creditcardpay import CreditCardPayement
from upipay import UPIPay
from context import PaymentContext
if __name__=="__main__":
    creditpay=CreditCardPayement()
    upipay=UPIPay()
    payment_context_credit=PaymentContext(creditpay)
    payment_context_credit.execute(1000)
    payment_context_upi=PaymentContext(upipay)
    payment_context_upi.execute(1500)