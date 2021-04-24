'''
Calculates the GCD given some integer numbers using the Euclidean Algorithm.
'''

def gcd(nums):
    if len(nums) == 1:
        return nums[0]
    lst = nums
    if int(nums[0]) > int(nums[1]):
        big = int(nums[0])
        small = int(nums[1])
    else:
        small = int(nums[0])
        big = int(nums[1])

    remainder = big % small

    while len(lst) != 1:
        lst = lst[2:]
        while remainder > 0:
            big = small
            small = remainder

            if small == 0:
                lst.append(big)
            remainder = big % small

        lst.append(small)

    return lst[0]


print('Hi! Welcome to the GCD calculator!')
while True:
    numbers = input('Enter at least two numbers to calculate their GCD (q to quit): ')
    if numbers.lower() == 'q':
        break
   
    great_com_fact = gcd(numbers.split())
    print(f"\nDone! This is their GCD: {great_com_fact}\n")

print('Thank you for using the GCD calculator!')
