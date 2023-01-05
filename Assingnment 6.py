import random

def main():
    country = {'USA' : 'Washington DC', 'England' : 'London',
    'France' : 'Paris', 'Germany' : 'Munich', 'Panoma' : 'Panoma City', 'Afghanistan' : 'Kabul',
    'Albania' : 'Tirana', 'Algeria' : 'Algiers', 'Andorra' : 'Andorra la Vella', 'Angola' : 'Luanda',
    'Antigua and Barbuda' : 'Saint Johns', 'Bahamas' : 'Nassau', 'Bahrain' : 'Manama', 'Peru' : 'Lima',
    'Philippines' : 'Manila', 'Saint Kitts and Nevis' : 'Basseterre', 'Singapore' : 'Singapore', 'Ecuador' : 'Quito',
    'Egypt' : 'Cairo', 'Estonia' : 'Asmara', 'Iceland' : 'Reykjavik', 'India' : 'New Delhi',
    'Indonesia' : 'Jakarta', 'Iran' : 'Tehran', 'Iraq' : 'Baghdad', 'Ireland' : 'Dublin',
    'Israel' : 'Jerusalem', 'Italy' : 'Rome', 'Jamaica' : 'Kingston', 'Japan' : 'Tokyo',
    'Jordan' : 'Amman', 'Kazakhstan' : 'Nur-Sultan'}

    choice = input('take a quiz on the countries or capitals? (y/n) ')

    if choice == 'countries':
        countryquiz(country)
    else:
        capitalquiz(country)

def capitalquiz(country):

    flag = 'y'
    correct = 0
    incorrect = 0

    while flag == 'y':
        random_country = random.choice(list(country))
        print(random_country)

        capital_user = input('enter the name of the capital for this country ')
    
        if country[random_country] == capital_user:
            print ('correct')
            correct = correct + 1
        else:
            print('incorrect')
            incorrect = incorrect + 1

        flag = input('do you want to continue (y/n)? ')
        if flag == 'n':
            print('number correct :', correct, '\nnumber incorrect:', incorrect)
# ask user if he wants to continue, if not switch the flag

def countryquiz(country):

    
    flag = 'y'
    correct = 0
    incorrect = 0

    while flag == 'y':
        random_capital = random.choice(list(country.values()))
        country_user = input(f'enter the name of the country with this capital: {random_capital} ')

        if country_user in country:
            
            if random_capital == country[country_user]: #
                print('correct')
                correct = correct + 1
            else:
                 print('incorrect')
                 incorrect = incorrect + 1
        else:
           print('country not on the list')
           incorrect = incorrect + 1 
        
            

        flag = input('do you want to continue(y/n)? ')
        if flag == 'n':
            print('number correct : ', correct, '\nnumber incorrect: ', incorrect)
        
        
        
main()
