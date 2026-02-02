# Array 
nums = [1,2,3,4,5]
print("Original array:", nums)

# Index based looping 
for i in range(len(nums)):
    print(nums[i])

# value based looping 
print("Value based looping:")
for num in nums:
    print(num)

# index and value based looping
print("Index and value based looping:")
for i, v in enumerate("Hello"):
    print(i, v)

# Reverse a String 
s = "Hello World"
def reverse_String(s):
    result = ""
    for char in s :
        result = char + result
    return result
print("Reversed String:", reverse_String(s))


# Check Palindrome 



