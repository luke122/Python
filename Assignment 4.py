def main():

      income = getHouseholdIncome()
      if income != 99999:
            numberOfKids = getNumKids()
            financialAssistance = financialCalc(income,numberOfKids)
            print('Your total financial assistance is $', format(financialAssistance ,',.2f'))

    
def getHouseholdIncome():
       householdIncome = float(input('Enter your household income, or enter -1 to quit: '))
       if householdIncome >0:
          return  householdIncome  
       else:
             print('Income has to be positive -- enter income or -1 to quit')
             householdIncome = float(input('Enter your household income, or enter -1 to quit: '))
             if householdIncome == -1:
                   return 99999
             else: return householdIncome
        
         
   
def getNumKids():
       numKids = int(input('Enter the number of kids that you have: '))
       if numKids >= 0:
          return numKids
       else:
          print('Number of kids has to be greater than or equal to 0')
          return 0
          
    
def financialCalc(householdIncome, numKids):
        if householdIncome >= 30000 and householdIncome <= 40000 and numKids >= 3:
            return 1000
        elif householdIncome >=20000 and householdIncome < 30000 and numKids >= 2:
            return 1500
        elif householdIncome < 20000:
            return 2000
        else:
            return 0
    

main()


