import locale

amountEarned = float(input("Please enter the amount of money you make: "))
status = (input("Enter marital status (single/married): "))
totalTax = float

if amountEarned <=0:
    print("'error")

else:
    if status == "single":
        if amountEarned < 8000:
            totalTax = amountEarned * .10
        else:
            if amountEarned > 8000 or amountEarned < 32000:
                totalTax = ((amountEarned - 8000) * .15) + 800
            else:
                totalTax = ((amountEarned - 32000) * .25) + 4400
    


    else:
        if status == 'married':
            if amountEarned  <16000:
                totalTax = amountEarned * .10
            else:
                if amountEarned >16000 or amountEarned <64000:
                    totalTax = ((amountEarned - 16000) * .15) + 1600
                else:
                    if amountEarned > 64000:
                        totalTax = ((amountEarned - 364000) * .25) + 8800

locale.setlocale(locale.LC_ALL, '')
print("Your total tax is: ", locale.currency(totalTax))

