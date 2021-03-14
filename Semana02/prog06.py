
nums = [1, 2, 3, 4, 5, 6, 7]

for num in nums:
    if num == 3:
        print('Found!')
        break  # continue
    print(num)



for num in nums:
    for letter in 'abc':
        print(num, letter)



for i in range(10):
    print(i)



for i in range(1, 11):
    print(i)




x = 0
while True:
    if x == 5:
        break
    print(x)
    x += 1
