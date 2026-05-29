from typing import Protocol

class PaymentMethod(Protocol):
    def authorize_Payment(self,amount:float)->bool:
        pass
    def process_Payment(self,amount:float):
        pass

class CreditCardPayment:
    def authorize_Payment(self,amount:float):
        print(f"Authorize payment {amount}")
        return True
       

    def process_Payment(self,amount:float):
        print(f"Process Payment {amount}")
        
        

class PayPalPayment:
    def authorize_Payment(self,amount:float):
        print(f"Authorize payment {amount}")
        return True

    def process_Payment(self,amount:float):
        print(f"Process Payment {amount}")
        

def process_order(payment:PaymentMethod,amount:float):
    if(payment.authorize_Payment(amount)):
        payment.process_Payment(amount)
        print("Payment successful")
    else:
        print("Payment authorization failed")


c = CreditCardPayment()
p = PayPalPayment()

process_order(p,1000.0)
process_order(p,10000.0)
