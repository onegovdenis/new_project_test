names = ['Denis', 'Alex', 'Kate', 'Tima']
inkognito = ['Dima', 'Oleg', 'Marina']
user_input = input('What is your name? ')
if user_input in names:
    print('Hello', user_input)

elif user_input in inkognito:
    print("Sorry, we don't know you")
else:
    print('Bye')
