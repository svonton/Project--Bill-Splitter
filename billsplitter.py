# write your code here
import random
amount = int(input('Enter the number of friends joining (including you):\n'))
if amount > 0:
    print('Enter the name of every friend (including you), each on a new line:\n')
    user_input = [str(input()) for x in range(amount)]
    total_bill = int(input('Enter the total bill value:\n'))
    choice = str(input('Do you want to use the "Who is lucky?" feature? Write Yes/No:\n'))
    if choice == 'Yes':
        lucky_guy = user_input[random.randrange(0, len(user_input))]
        print(f'{lucky_guy} is the lucky one!')
        users = {k: round(total_bill / (amount-1), 2) for k in user_input}
        users[lucky_guy] = 0
        print(users)
    else:
        print('No one is going to be lucky')
        users = {k: round(total_bill/amount, 2) for k in user_input}
        print(users)
else:
    print('No one is joining for the party')

