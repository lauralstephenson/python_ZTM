# Shopping cart for my mythical store
# importing file from this folder
from utility import multiply, divide 
#nesting folder shopping, folder more_shopping, file shopping_cart
#import shopping.more_shopping.shopping_cart
#from shopping.more_shopping.shopping_cart import buy
#OR
#from shopping.more_shopping import shopping_cart
fom utility import *

def buy(item):
    cart.append(item)
    return cart

#if importing it
#print(buy("glass apple"))
#OR
#print(shopping_cart.buy("glass apple")
#print(divide(5,2))
#print(multiply(5, 2))

print(shopping.more_shopping.shopping_cart.buy("glass apple"))
