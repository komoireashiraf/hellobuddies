##
##coins = 100
####add = coins + 500

##print(f'the coins are {add}')

class piggyBank:
    def __init__(self, coins):
        self._coins = coins
        self.put_in(coins)

    def put_in(self, amount):
        if amount <= 0:
            raise ValueError("Add some money!")
        self._coins += amount
    
    def take_out(self, amount):
        if amount <= 0:
            raise ValueError("Enter actual amount!")
        if amount >= self._coins:
            raise ValueError("Money is coming!")
        self._coins -= amount
    
    def how_much(self):
        return self._coins
    
gabby = piggyBank(1000000)

print("Gabby has: ", gabby.how_much()) 
