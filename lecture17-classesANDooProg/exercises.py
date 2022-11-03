#!/usr/bin/env python3



###############################################################################
#       Remeber in PYTHON we have PASS BY VALUE for function parameters.      #
###############################################################################


###############################################################################
#                                    self.
#
# This operator indicates that we are referring to the current object,
# or class instance. Thus fnname(self, optional_args), self is always
# required.
###############################################################################


class Inventory:
    item = ""
    barcode = 0
    quantity = 0
    price = 0.00
    sales = 0.00
    def __init__(self, product, bar, pr):
        ########################################################################
        #
        #       This is the default CONSTRUCTOR called on object cbject
        #       creation and instantiation.
        #
        ########################################################################
        self.item = product
        self.barcode = bar
        self.price = pr

    def changeprice(self, newprice):
        self.price = newprice

    def sell(self, n):
        self.quantity -= n
        self.sales += self.price*n

    def restock(self, n):
        self.quantity += n

    def printObjectDetails(self, product):
        print("Printing all inventory data for a particular instance or object.")
        print("item: ", product.item)
        print(" barcode: ", product.barcode)
        print(" price: ", product.price)
        print(" quantity: ", product.quantity)
        print(" sales: ", product.sales)

        #######################################################################
        #                 HOWTO use self., very good example.                 #
        #######################################################################
    def printObjectDetailsAnswers(self):
        print("Printing all inventory data for a particular instance or object.\n"
              "Using the method in the Answers: section.")
        print(self.item+"   barcode: "+str(self.barcode))
        print("Price:",self.price)
        print("Current Inventory:", self.quantity)
        print("Sold so far:", self.sales)


        

        
        




# main.py
        
print("ex:1")

# item=widget, barcode=1112223334, price=10.0
widget = Inventory("widget", 1112223334, 10.00)

widget.restock(30) # quantity=30

# quantity=30-10=20
# sales=0+(10*10)=100
widget.sell(10)
print(widget.quantity) # 20
print(widget.sales) # 100

widget.changeprice(20.0) #price=20.0
widget.sell(10) #quantity=20-10=10, sales= 100 + 20*10 = 300
print(widget.quantity) # #10
print(widget.sales) #300
#print(widget)


print("\nex2:")

# shoes obj/instance: item=shoe, barecode=1234512345, price=30
shoes = Inventory("shoe", 12345123245, 30.00)
shoes.restock(100) # quantity=100

# shirts obj/instance: item=9876598765, price=25 
shirts = Inventory("shirt", 9876598765, 25.00)



shirts.restock(80) # shirts obj, quantity=80
shirts.sell(30) # shirts obj: quantity=50, sales=s=30*25=750
shoes.sell(10) # shoes obj: quantity=90, sales=30*10=300
shoes.sell(50) # shoes obj: quantity=40, sales=300 + (50*30=1500) = 1800
print(shoes.quantity) # 40
print(shoes.sales) # 1800
print(shirts.quantity) #50
print(shirts.sales) #750



print("\nex3: my METHOD:  \n"
      "Printing object details for widget, shoes and shirts objects:")
widget.printObjectDetails(widget)
shoes.printObjectDetails(shoes)
shirts.printObjectDetails(shirts)

print("\nex3: answers METHOD: (probably better way to do it)\n"
      "Printing object details for widget, shoes and shirts objects:")

###############################################################################
# NOTE:
# IMPORTANT:
# I think this uses the fact that self refers to the current object,
# this is the power self.(/this. in c++) reference I guess.
###############################################################################

# so this would mean call printObjectDetailsAnswers("with this object,
# widget, as the instance")
widget.printObjectDetailsAnswers()
shoes.printObjectDetailsAnswers()
shirts.printObjectDetailsAnswers()



print("\nex4:\n"
      "Create movies class with members and give default values of\n"
      "name, genre, rating(0-10, -ve number exits.)")

class Movie:
    name = ""
    genre = ""
    rating = 0

    def __init__(self, movie_name, movie_genre, movie_rating):
        "The __init__(self, args), args are optional, \n"
        "is called the init fn or costructor."
        self.name = movie_name
        self.genre = movie_genre
        self.rating = movie_rating



# TESTING part of algorithim:
# movie0 =  Movie("", "", 0)
# name = input("Enter movie name: ")
# genre =  input("Enter movie genre: ")
# rating = input("Enter your rating for the movie: ")
# movie0 = (name, genre, rating)
# print("Details for movies enterd is: ", movie0)


# Could I make the input function using RECURSION???
rating = 0 # while loop terminator
movies = [] # List of movies the user will enter, initialise to empty
while (rating >= 0):
    name = input("Enter movie name: ")
    genre =  input("Enter movie genre: ")
    # converts string to integer, all command line input is treated as
    # a string remember
    rating = int(input("Enter your rating for the movie: "))
    a_movie = (name, genre, rating)
    if rating >=0 :
        # only add valid movies, not end of program/loop/entries
        movies.append(a_movie)

print("Details for movies enterd is: ", movies)
print("Movie list printed VERTICALLY, my preference:")
for i in range(len(movies)):
    # iterates the global movies list
    print(movies[i])
