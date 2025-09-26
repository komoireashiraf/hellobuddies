##area of a circle
class Circle:
    def __init__(self, radius):
        self.radius = radius
        
    def area_of_circle(self):
        return 3.14 * self.radius * self.radius
    
##creation of objects
c1 = Circle(26)
c2 = Circle(6.9)

print(c1.area_of_circle())


##bank account
class bank_account:
    def __init__(self, balance=0):
        self.balance = balance
    
    def deposit(self, amount):
        self.balance += amount
    
    def withdraw(self, amount):
        self.balance -= amount

account = bank_account(679)
account.deposit(89)
account.withdraw(180)

print(account.balance)

##student
class student:
    def __init__(self, name, age, course):
        self.name = name 
        self.age = age
        self.course = course


class Phone:
    def __init__(self, brand, model, storage):
        self.brand = brand
        self.model = model
        self.stotage = storage

    def call(self, number):
        print(f'Calling {number} from {self.brand} {self.model}!')
    def take_photo(self, photo):
        print(f'Taking photo {photo}!')
    def play_music(self, song):
        print(f'Playing {song}.')


phone = Phone('iPhone','17 Air', '2TB')
phone.call('0123-456-789')
phone.take_photo('selfie')
phone.play_music('Luv By Tory Lanez')





    