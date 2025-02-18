# write a function that sums number in a list.

# Method 1
def sum_list(nums):  
    total = 0  
    for num in nums:  
        total += num  
    return total  

# Method 2, using python builtin function "sum()"
def sum_list(nums):
    return sum(nums) 
# test case for the above two methods
 numbers_list = [1, 2, 3, 4, 5]
result = sum_list(numbers_list)
print("Sum:", result)



# print even numbers between 1 and 20 using a loop.
# Method 1 
def even_num():
    num = 2
    result = []
    while num <= 20:
        result.append(num)
        num += 2
    return result

print(even_num()) 

# Method 2
 for num in range(1, 21):  
    if num % 2 == 0:  
        print(num) 

# write a program to find the largest number in the list.


def largest_num(nums):
    return max(nums)

numbers = [1, 2, 3, 4, 5]
result = largest_num(numbers)
print("largest :", result)

