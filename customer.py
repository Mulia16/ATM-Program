from atm_card import ATMCard

class Customer(ATMCard):
    def __init__(self, id, custPin=1234, custBalance=10_000):
        super().__init__(custPin, custBalance)
        self.id = id
        self.custPin = custPin
        self.custBalance = custBalance

    def getId(self):
        return self.id
    
    def getCustPin(self):
        return self.custPin

    def setCustPin(self, pin, verify):
        if self.custPin == verify:
            self.custPin = pin
            print("Berhasil mengganti pin")
        else :
            print("Error. pin verifikasi salah")

    def getCustBalance(self):
        return self.custBalance

    def withdrawBalance(self, nominal):
        self.custBalance -= nominal
    
    def depositBalance(self, nominal):
        self.custBalance += nominal
