def main():

    profit1 = Profit()
    profit2 = Profit() 


    firstStock = input("Enter the first stock's symbol: ")
    firstStockNumberOfPurchases = int(input("Enter the number of purchases for this stock: "))
    if firstStockNumberOfPurchases <= 0:
        print('You must enter a positve number.')

    firstStockProfitOrLoss = profit1.loop(firstStockNumberOfPurchases)

    
    secondStock = input("Enter the second stock's symbol: ")
    secondStockNumberOfPurchases = int(input("Enter the number of purchases for this stock: "))
    if secondStockNumberOfPurchases <= 0:
        print('You must enter a positve number.')

     
    secondStockProfitOrLoss = profit2.loop(secondStockNumberOfPurchases)
    
        
    if firstStockProfitOrLoss > secondStockProfitOrLoss:
        print(firstStock, 'was more profitable than', secondStock)
    else:
        print(secondStock, 'was more profitable than', firstStock)





    



class Profit:
    def __init__(self):
        self._numberOfPuchases = 0
        self._numberOfShares = 0
        self._pricePerShare = 0.0
        self._counter = 1
        self._totalShares = 0
        self._totalCost = 0
        self._pricePerShare = 0
        self._todaysPrice = 0
        self._todaysCost = 0
        self._netGainOrLoss = 0

    def loop(self, numberOfPuchases):
        while self._counter <= numberOfPuchases:
            print(self._counter, end='')
            self._numberOfShares = int(input(': How many shares? '))
            if self._numberOfShares < 0:
                print('You must enter a positive number.')
                exit() 
            self._totalShares = self._totalShares + self._numberOfShares
            self._pricePerShare = float(input('Price per share? '))
            if self._pricePerShare < 0:
                print('You must enter a positive number.')
                exit()
            self._totalCost = self._totalCost + (self._pricePerShare * self._numberOfShares)
            self._counter = self._counter + 1
        self._todaysPrice = float(input("Today's price per share? "))
        if self._todaysPrice < 0:
            print('You must enter a positive number.')
            exit()
        self._todaysCost = self._todaysPrice * self._totalShares
        self._netGainOrLoss = self._todaysCost - self._totalCost
        print('Net profit/loss: $',(format(self._netGainOrLoss, ',.2f')), sep = '')
        

        return self._netGainOrLoss
            
    
        
        
        
main()
