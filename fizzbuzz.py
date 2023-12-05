def fizz_buzz(max_num):
    for num in range(1, max_num):
        if num % 3 == 0 and num % 5 == 0:
            print('{} is fizzbuzz'.format(num))
        elif num % 3 == 0:
            print(f'{num} is fizz')
        elif num % 5 == 0:
            print(f'{num} is buzz')
        else:
            print(num)

num = input('enter number: ')

while (int(num) > 10):
    fizz_buzz(int(num))
    num = input('new number: ')
