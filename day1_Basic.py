# Basic of python programming

# variable 
x=10; 
name = "John Doe"
print("Value of x:", x)
print("Name:", name)


# Loops 
for i in range(1,5):
    print("Iteration:", i)


# condition 

if x>5 :
    print("x is greater than 5")
else:
    print("x is less than or equal to 5")

# List (dynamic array)
arr=[1,2,3,4,5]
arr.append(6)
arr.pop()
print("List elements:")
for item in arr:
    print("array element", item)


# dictionary (hash map )
frequencies ={'a':3, 'b':5, 'c':2}
frequencies['d'] =4
print("Dictionary elements:")
for key, value in frequencies.items():
    print(f"Key: {key}, Value: {value}")


# Sets
s = set([1,2,3,4])
for item in s:
    print("Set element:", item)


# string 
s = "Hello, World!"
reversed_s = s[::-1]
print(reversed_s)  # print reversed string
print(s[::-1]) # print reversed string

# reverse the string in different way 
s = "Hello, World!"
rev="".join(reversed(s))
print(rev)  # print reversed string


#List comprehension
sqr = [x*2 for x in range(4)]
print("List comprehension result:", sqr)  

# Enumerate 
for i, val in enumerate(['a','b','c']):
    print(f"Index: {i}, Value: {val}")


# reverse a list 

def reverseList(lis):
    return lis[::-1]
print(reverseList([1,2,3,4,5]))


# find the max element in a list 
def findMax(lis):
    m = lis[0]
    for i in lis:
        if i>m:
            m=i
    return m
print(findMax([1,5,3,9,2]))


# count the frequency 
def countFrequency(lis):
    freq = {}
    for item in lis:
        freq[item] =freq.get(item,0)+1
    return freq
print(countFrequency(['a','b','a','c','b','a']))


# check palindrome 
def ispalindrome(s):
    return s==s[::-1]

print(ispalindrome("racecar"))  # True


