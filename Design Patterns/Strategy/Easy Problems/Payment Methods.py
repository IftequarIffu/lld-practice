"""
Problem Statement:
------------------

Without using if-else or switch-case conditionals, 
implement multiple different payment methods.

1. Card
2. UPI
3. Crypto

"""



from abc import ABC, abstractmethod

class PaymentStrategy(ABC):

    @abstractmethod
    def pay(self, amount: float):
        pass


class CardPaymentStrategy(PaymentStrategy):

    def __init__(self, card_no: str):
        self.card_no = card_no

    def pay(self, amount: float):
        print(f"Paying ${amount} using card ending with {self.card_no[-4:]}")


class UPIPaymentStrategy(PaymentStrategy):

    def __init__(self, upi_id: str):
        self.upi_id = upi_id

    def pay(self, amount: float):
        print(f"Paying ${amount} using UPI ID: {self.upi_id}")


class CryptoPaymentStrategy(PaymentStrategy):

    def __init__(self, wallet_address: str):
        self.wallet_address = wallet_address

    def pay(self, amount: float):
        print(f"Paying ${amount} using Crypto from wallet address {self.wallet_address}")


class PaymentContext:

    def __init__(self, strategy: PaymentStrategy):
        self.strategy = strategy

    def set_strategy(self, strategy: PaymentStrategy):
        self.strategy = strategy

    def make_payment(self, amount: float):
        self.strategy.pay(amount)


if __name__ == "__main__":

    context = PaymentContext(CardPaymentStrategy("1234 1234 1234 1234"))
    context.make_payment(2500)

    context.set_strategy(CryptoPaymentStrategy("0x12f312f312f312f312f312f312f312f3"))
    context.make_payment(5000)

    context.set_strategy(UPIPaymentStrategy("9124317562@oksbi"))
    context.make_payment(3000)