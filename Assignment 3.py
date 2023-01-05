totalRainfall = 0.00
averageRainfall = 0.00
totalMonths = 0
yearlyRainfall = 0.00

years = int(input("Enter the number of years: "))


if years <=0:
    print("error, you must enter a positive whole number")
    exit()



for i in range (1, years + 1):
    print('Year', i)
    yearlyRainfall = 0.00 
    for j in range(1,13):
        rainfall = float(input("Enter the amount of rainfall for this month in inches: "))
        totalMonths = totalMonths + 1
        totalRainfall = totalRainfall + rainfall
        yearlyRainfall = yearlyRainfall + rainfall
        if totalMonths % 12 ==0:
            print('Year', i, 'total rainfall is: ' + format(yearlyRainfall, '.2f'), 'inches')
            print('Yearly average:', format(yearlyRainfall/12, '.2f'))
            years +=1
            
        
        
averageRainfall = totalRainfall/totalMonths        
print(totalMonths, 'Months', '--','Total rainfall in inches:', format(totalRainfall, '.2f'), '--', 'Average rainfall in inches: ', format(averageRainfall, '.2f'))