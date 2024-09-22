'''
def is_unique(s):
    seen = set()
    for char in s:
        if char in seen:
            return False
        seen.add(char)
    return True
# Example usage:
print(is_unique("abcdef"))  # Expected Output: True
print(is_unique("aabbcc"))  # Expected Output: False
print(is_unique(""))        # Expected Output: True
'''
'''
def strStr(haystack: str, needle: str) -> int:
    return haystack.find(needle)

# Test cases
print(strStr("sadbutsad", "but"))    # Output: 0 (needle "sad" starts at index 0)
print(strStr("leetcode", "leeto"))   # Output: -1 (needle "leeto" is not found)
print(strStr("sad", "sadbutsad"))    # Output: -1 (needle "sadbutsad" is longer than haystack)
'''
def reverse_lst(lst):
    left = 0
    right = len(lst)-1
    while left < right:
        temp = lst[left]
        lst[left] = lst[right]
        lst[right] = temp
        left +=1
        right -1
    return lst
# Test cases
lst = [1, 2, 3, 4, 5]
print(reverse_lst(lst))  # Expected output: [5, 4, 3, 2, 1]


