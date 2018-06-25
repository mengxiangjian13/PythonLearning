def collatz(number):
    try:
        num = int(number)
        while num != 1:
            if num % 2 == 1:
                num = num * 3 + 1 # 奇数
            else:
                num = num // 2 #偶数
            print(num)
        print('finally, 1!')
    except ValueError:
        print('input text is not a integer')

print('input a integer:')
n = input()
collatz(n)