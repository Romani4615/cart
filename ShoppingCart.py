class Cart:
    # init method handles our attributes
    def __init__(self):
        # our attributes get defined here
        self.items = []
    
    # our other methods handle our actions/processes
    
    # process of adding handled here
    # add here is the name of my own defined function/method
    # it is different than the set.add() method
    def add_to_cart(self):
        item = input('What item would you like to buy? ').title()
        self.items.append(item)
        print(f'You add {item} to your cart.')
        self.show()
    
    # process of removing handled here
    def remove(self):
        removal = input(f'Okay, here is your cart: {self.items}\nWhat would you like to remove?\n').title()
        # i need to check if the thing is in my cart before I try to remove it
        # membership check
        if removal in self.items:
            self.items.remove(removal)
            print(f'{removal} has been removed from your cart.')
            self.show()
        else:
            print(f'{removal} is not in your cart. Nothing to remove.')
            self.show()
    
    # process of looking at everything in the cart - handled here
    def show(self):
        input(f'Your cart contains: {self.items}\nPress any key to continue.')
    
    # process for clearing
    def clear(self):
        print('clearing\n')
    
    #process for checkout
    def checkout(self):
        print('checkout\n')

# instantiation of your cart object
mycart = Cart() # blah blah whatever parameters you need
while True:
    #asking for user input
    choice = input('What would you like to do? add/remove/show/clear/checkout - ').lower()
    # if the user says add
    if choice == 'add':
        mycart.add_to_cart()
        
    elif choice == 'remove':
        mycart.remove()
    
    elif choice == 'show':
        mycart.show()
        
    elif choice == 'clear':
        mycart.clear()
    
    elif choice == 'checkout':
        mycart.checkout()
        break
    
    else:
        print('Not a valid input.')