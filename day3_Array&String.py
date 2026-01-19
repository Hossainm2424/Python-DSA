# Array - ordered data collections 
arr = [1, 2, 3, 4, 5]
print("Array:", arr)

# String - sequence of characters but immutable
str = "Hello, World!"
print("String:", str)


# Two pointer Technique 
left =0; 
right =len(arr)-1; 

while left<right:
    if arr[left] + arr[right] == 7:
        left +=1;
    else:
        right -=1;


# Interview Style question 
# 1. Reverse aan array - using two pointer technique

def reverse_array(arr): 
    left =0;
    right =len(arr)-1;
    while left<right:
        arr[left], arr[right] = arr[right], arr[left]
        left +=1;   
        right -=1;
    return arr
print("Reversed Array:", reverse_array([1, 2, 3, 4, 5]))


# 2. Check if a string is a palindrome
def is_palindrome(s):
    left =0; 
    right =len(s)-1;
    while left<right:
        if s[left] != s[right]:
            return False
        left +=1;
        right -=1;
    return True

print("Is 'racecar' a palindrome?", is_palindrome("racecar"))

# 3. remove duplicates from sorted Array 
def remove_duplicateds(arr):
    i =0
    for j in range(1, len(arr)):
        if arr[j] != arr[i]:
            i +=1
            arr[i] = arr[j]
    return arr[:i+1];
print("Length after removing duplicates:", remove_duplicateds([1, 1, 2, 2, 3, 4, 4, 5]))


# 4. Valid Anagram -using dictionary 
def is_anagram(s1, s2):
    if len(s1) !=len(s2):
        return False; 
    count ={}
    for char in s1:
        count[char] = count.get(char,0)+1
    for char in s2:
        if char not in count or count[char] ==0:
            return False
        count[char] -=1
    return True
print("Are 'listen' and 'silent' anagrams?", is_anagram("listen", "silent"))

# Sliding Window Technique - Used for problems involving subarrays or substrings

