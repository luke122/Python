amountPurchased = float(input('Please enter the amount of groceries purchased '))
cardholder = input('Are you a cardholder? Please type yes or no ')

discountPercentage = 0.00

if amountPurchased <25:
    discountPercentage = 0
elif amountPurchased >=25 and amountPurchased < 100:
    discountPercentage = .02
elif amountPurchased >= 100 and amountPurchased <= 250:
    discountPercentage = .03
else: 
    discountPercentage = .05
if cardholder == 'yes':
    discountPercentage += .02
        
discount = amountPurchased * discountPercentage
finalAmountPayable = amountPurchased - discount 

print('Total value of groceries purchased is:', amountPurchased)
print('Discount received: ', discount)
print('The final payable amount is:', finalAmountPayable)


        

    
    
