### Unit one section two question 1
''' Write a function reverse_sentence() that takes 
in a string sentence and returns the sentence with
the order of the words reversed. The sentence will 
contain only alphabetic characters and spaces to
separate the words. If there is only one word in 
the sentence, the function should return the original string.'''
'''
def reverse_sentence(sentence):
    words=sentence.split()
    if(len(words)>1):
        return (words[::-1])
    else:
        return sentence
    pass
sentence = "tubby little cubby all stuffed with fluff"
print (reverse_sentence(sentence))
'''




### Unit one section two question 2
'''
In the extended universe of fictional bears, Goldilocks
finds an enticing list of numbers in the Three Bears' 
\house. She doesn't want to take a number that's too high 
\or too low - she wants a number that's juuust right.
Write a function goldilocks_approved() that takes in 
the list of distinct positive integers nums and returns
any number from the list that is neither the minimum nor 
the maximum value in the array, or -1 if there is no such number.
'''
'''
def goldilocks_approved(nums):
    if len(nums) < 3:
        return -1
    max_number = max(nums)
    min_number = min(nums)
    result =[]
    for i in nums:
        if(i != max_number and i != min_number):
              result.append(i)
    return result
    pass
nums = [3, 2, 1, 4]
print(goldilocks_approved(nums))
'''




### Unit one section two question 3
'''
Pooh is eating all of his hunny jars in order
of smallest to largest. Given a list of integers
hunny_jar_sizes, write a function delete_minimum_elements()
that continuously removes the minimum element until the 
list is empty. Return a new list of the elements of 
hunny_jar_sizes in the order in which they were removed.
'''
'''
def delete_minimum_elements(hunny_jar_sizes):
    result = []
    while len(hunny_jar_sizes) > 0:  
        min_value = min(hunny_jar_sizes) 
        result.append(min_value) 
        hunny_jar_sizes.remove(min_value)  
    return result 
hunny_jar_sizes = [5, 1, 3, 2, 4]
removed_order = delete_minimum_elements(hunny_jar_sizes)
print(removed_order)  # Output: [1, 2, 3, 4, 5]
'''


### Unit one section two question 4
'''
Write a function sum_of_digits() that accepts 
an integer num and returns the sum of num's digits.
'''
'''
def sum_of_digits(num):
    total = 0
    for i in str(num):
        total += int(i)
    return total
num = 423
print(sum_of_digits(num))
'''



### Unit one section two question 5
'''
Tigger has developed a new programming language
 Tiger with only four operations and one variable tigger.
bouncy and flouncy both increment the value of the variable tigger by 1.
trouncy and pouncy both decrement the value of the variable tigger by 1.
Initially, the value of tigger is 1 because he's the only tigger around!
 Given a list of strings operations containing a list of operations, return
   the final value of tigger after performing all the operations.
'''
'''
def final_value_after_operations(operations):
	trigger = 1
	for i in operations:
		if i in ("bouncy", "flouncy"):
			trigger+=1
		elif i in ("trouncy", "pouncy"):
			trigger-=1
	return trigger
	pass
operations = ["trouncy", "flouncy", "flouncy"]
print(final_value_after_operations(operations))
'''



### Unit one section two question 6
'''
Given an array of strings words and a string s,
implement a function is_acronym() that returns True if s 
is an acronym of words and returns False otherwise.
The string s is considered an acronym of words if it 
can be formed by concatenating the first character of 
each string in words in order. For example, "pb" can be
formed from ["pooh"", "bear"], but it can't be formed 
from ["bear", "pooh"].
'''
'''
def is_acronym(words, s):
    for i in range(len(words)):
        if words[i][0] != s[i]:
            return False
    return True
    pass
words = ["christopher", "robin", "milne"]
s = "crm"
print(is_acronym(words, s))
'''



### Unit one section two question 7
'''
Write a function make_divisible_by_3() that accepts an integer 
array nums. In one operation, you can add or subtract 1 from 
any element of nums. Return the minimum number of operations 
to make all elements of nums divisible by 3.
'''
'''
def make_divisible_by_3(nums):
    total_operations = 0
    for num in nums:
        remainder = num % 3
        if remainder == 0:
            continue
        elif remainder == 1:
            total_operations += 1
        else:  
            total_operations += 1
    return total_operations
nums = [7, 8, 10, 12, 14]
result = make_divisible_by_3(nums)
print(result) 
'''



### Unit one section two question 8
'''
Given two lists lst1 and lst2, write a function
 exclusive_elemts() that returns a new list that 
 contains the elements which are in lst1 but not 
 in lst2 and the elements that are in lst2 but not in lst1.
'''
'''
def exclusive_elemts(lst1, lst2):
    exclusive = []
    for item in lst1:
        if item not in lst2:
            exclusive.append(item)
    for item in lst2:
        if item not in lst1:
            exclusive.append(item)
    return exclusive
lst1 = ["pooh", "roo", "piglet"]
lst2 = ["piglet", "eeyore", "owl"]
print(exclusive_elemts(lst1, lst2))
'''



### Unit one section two question 9
'''
Write a function merge_alternately() that accepts 
two strings word1 and word2. Merge the strings by 
adding letters in alternating order, starting with word1. 
If a string is longer than the other, append the additional
letters onto the end of the merged string.
Return the merged string.
'''
'''
def merge_alternately(word1, word2):
    merged = []
    len1= len(word1)
    len2 = len(word2)
    for i in range(min(len1, len2)):
        merged.append(word1[i])
        merged.append(word2[i])
    if len1 > len2:
        merged.append(word1[len2:])
    else:
        merged.append(word2[len1:])
    return ''.join(merged)
word1 = "wol"
word2 = "oze"
print(merge_alternately(word1, word2))
'''



### Unit one section two question 10
'''
Eeyore has collected two piles of sticks to rebuild his house 
and needs to choose pairs of sticks whose lengths are the right
proportion. Write a function good_pairs() that accepts two integer
arrays pile1 and pile2 where each integer represents the length of
a stick. The function also accepts a positive integer k. The function 
should return the number of good pairs.
'''
'''
def good_pairs(pile1, pile2, k):
    count = 0
    for i in range(len(pile1)):
        for j in range(len(pile2)):
            if pile1[i] % (pile2[j] * k) == 0:
                count += 1
    return count
pile1 = [1, 3, 4]
pile2 = [1, 3, 4]
k = 1
print(good_pairs(pile1, pile2, k))
'''
