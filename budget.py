class Category:
    name = ''
    balance = 0
    
    
    def __init__(self, categ):
        self.name = categ
        self.ledger = list()
    
    
    def deposit(self, amount, description=''):
        self.ledger.append({'amount': amount, 'description': description})
        self.balance += amount
    
    
    def withdraw(self, amount, description=''):
        if self.check_funds(amount):         
            self.ledger.append({'amount': (amount * -1), 'description': description})
            self.balance -= amount
            return True 
        else:
            return False
    
    
    def get_balance(self):
        return self.balance
    
    
    def transfer(self, amount, destination):
        if self.check_funds(amount):
            self.withdraw(amount, f'Transfer to {destination.name}')
            destination.deposit(amount, f'Transfer from {self.name}')
            return True
        else:            
            return False
            
    def check_funds(self, amount):
        if amount > self.balance:
            return False
        else:
            return True
    
    
    def __str__(self):
        chart = f'{self.name:*^30}\n'
        for item in self.ledger:
            chart += f'{item["description"][0:23]:<23}{item["amount"]:>7.2f}\n'
        chart += f'Total: {self.balance}'
        return chart
       
        
def create_spend_chart(categories):
    percentages = dict()
    expenses = dict()
    total = 0
    longestname = None
    for category in categories:
        expense = 0
        if longestname is None or len(category.name) > longestname:
            longestname = len(category.name)        
        for item in category.ledger:
            if item['amount'] < 0:
                expense += item['amount']
        total += expense
        expenses[category.name] = expense
    for category in categories:
        percentages[category.name] = round(expenses[category.name] * 100 / total)
    chart = 'Percentage spent by category\n'
    for p in range(100, -10, -10):
        chart += f'{p:>3}|'
        for category in categories:
            if percentages[category.name] >= p:
                chart += ' o '
            else:
                chart += '   '
        chart += ' \n'
    chart += '    ' + '-' * (len(categories) * 3 + 1) + '\n'
    for letter in range(0, longestname):
        chart += '    '
        for category in categories:
            if len(category.name) > letter:
                chart += f' {category.name[letter]} '
            else:
                chart += '   '
        if letter < longestname - 1:
            chart += ' \n'
        else:
            chart += ' '
    return chart
            

from unicodedata import category
from unittest import main

food = Category('Food')
entertainment = Category('Entertainment')
business = Category('Business')
food.deposit(900, "deposit")
entertainment.deposit(900, "deposit")
business.deposit(900, "deposit")
food.withdraw(105.55)
entertainment.withdraw(33.40)
business.withdraw(10.99)
print(food)
print(entertainment)
print(business)
print(create_spend_chart([business, food, entertainment]))

