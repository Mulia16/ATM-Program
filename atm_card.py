class ATMCard:
    def __init__(self, defaultPin, defaultBalance):
        self.defaultPin = defaultPin
        self.defaultBalance = defaultBalance

    def getDefaultPin(self):
        return self.defaultPin

    def getDefaultBalance(self):
        return self.defaultBalance
