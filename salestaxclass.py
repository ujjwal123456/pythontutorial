#!/usr/bin/python
#import modules
import sys
import re
import math
#get filename as argument
filename = sys.argv[1]
round_factor = 0.05
#function round up
#to round up to round_factor 0.05
def round_up(x, a):
            return math.ceil(x / a) * a
#class declaration			
class sales:
	#class member variables
	domesticTaxPercentage = 10
	additionalImportedTaxPercentage = 5
	taxPercentage = 0
	salesTax = 0
	#class member function
	def calculateTaxPercentage(self,itemtype):  #to calculate taxPercentage function
        	if("book" in itemtype  or "chocolate" in itemtype or "pills" in itemtype):  #condition for eliminating food,medicines,books from tax
                	 self.taxPercentage = 0
	        else:
        	        self.taxPercentage = self.domesticTaxPercentage
	        if("imported" in itemtype):		#if imported keyword present in product then additionalImportedTaxPercentage will be applicable 
        	        self.taxPercentage = float(self.taxPercentage) + self.additionalImportedTaxPercentage # #addition of basic tax + imported tax 
    		return self.taxPercentage	#value return 
	#function for calculating tax	
	def calculateSalesTax(self,cost,taxPercentage):
		self.salesTax = float(cost) * float(taxPercentage)/100
		self.salesTax= round_up(self.salesTax,round_factor)
		return round(self.salesTax,2)
#object creation
obj = sales();
#read input file line by line 
with open(filename) as f:
	mylist = f.read().splitlines() 
items={}
#assign default values   
totalcost = 0
salesTax_total=0
salesTax = 0
taxPercentage = 0
for x in mylist:		#for loop 
	item = re.split(r'\bat\b',x)		 #regular expression split by "at"
	item_name = item[0]
	item_cost = item[1]
	taxPercentage = obj.calculateTaxPercentage(item_name) 	#checking item name in according to tax percentage
	salesTax = obj.calculateSalesTax(item_cost,taxPercentage) #calculation of item cost + tax percentage according to product
	salesTax_total = float(salesTax_total) + float(salesTax)#addition of tax 
	totalcost = float(totalcost) + float(item_cost) + float(salesTax) #total cost of bucket
	print str(item_name)+":"+str(float(item_cost)+float(salesTax)) #printing item_name then item cost then tax
print "Sales Total = "+str(salesTax_total)  #printing total sales tax  value 
print "Total Cost = "+str(totalcost)	 #printing total cost of the product

