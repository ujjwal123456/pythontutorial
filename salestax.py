#importing libraries 
import sys
import re       
import math

#get filename as argument
filename = sys.argv[1]

#assign default values
round_factor = 0.05      
domesticTaxPercentage = 10 
additionalImportedTaxPercentage = 5    
taxPercentage = 0  

#round-up function
def round_up(x, a):     
    return math.ceil(x / a) * a      
#to calculate taxPercentage function
def calculateTaxPercentage(itemtype):      
	if("book" in itemtype  or "chocolate" in itemtype or "pills" in itemtype):		#condition for eliminating food,medicines,books from tax
                 taxPercentage = 0				
        else:
                taxPercentage = domesticTaxPercentage
        if("imported" in itemtype):		#if imported keyword present in product then additionalImportedTaxPercentage will be applicable 
                taxPercentage = float(taxPercentage) + additionalImportedTaxPercentage  #addition of basic tax + imported tax 
        return taxPercentage    #value return 

#function for calculating tax
def calculateSalesTax(cost,taxPercentage):    
        salesTax = float(cost) * float(taxPercentage)/100 
	salesTax= round_up(salesTax,round_factor)
	return round(salesTax,2)
	
#read input file line by line 
with open(filename) as f:  
	mylist = f.read().splitlines()  
	
#assign default values    		
totalcost = 0	 
salesTax_total=0	
salesTax = 0		
taxPercentage = 0  
for x in mylist:						#for loop 	
	item = re.split(r'\bat\b',x)        #regular expression split by "at"
	item_name = item[0]      
	item_cost = item[1]
	taxPercentage = calculateTaxPercentage(item_name)  #checking item name in according to tax percentage
	salesTax = calculateSalesTax(item_cost,taxPercentage)  #calculation of item cost + tax percentage according to product
	salesTax_total = float(salesTax_total) + float(salesTax) # addition of tax 
	totalcost = float(totalcost) + float(item_cost) + float(salesTax) #total cost of bucket
	print str(item_name)+":"+str(float(item_cost)+float(salesTax)) #printing item_name then item cost then tax
print "Sales Total = "+str(salesTax_total) #here we are printing total sales tax  value 
print "Total Cost = "+str(totalcost) #here we are printing total cost of the product 


