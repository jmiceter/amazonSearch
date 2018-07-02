# Module: Processing_data.py
#"D:/Projects/JXM Products, llc/amazon filter/Processing_data.py"

print ("here we will take in the web processing items and evaluate them")



# FUNCTIONS
#
# recieve data from internet scraping.
# organize and calclutate the worthyness of the product.
# check for consistancy over time
#
#

class Product_Entry:
	productName = ""
    isbnNumber = 0
    cheapestLoc = ""
    cheaperLoc = ""
    wholesale = 0
    amazonCost = 0
    salesPerMonth = 0
    profitMargin = 0
	def SendEntry():
		return (productName, isbnNumber, cheapestLoc, cheaperLoc, wholesale,amazonCost,salesPerMonth,profitMargin)
