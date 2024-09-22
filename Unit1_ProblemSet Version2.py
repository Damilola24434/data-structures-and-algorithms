'''
def are_equivalent(word1, word2):
    string1 = ''.join(word1)
    string2 = ''.join(word2)
    return string1 == string2
word1 = ["bat", "man"]
word2 = ["b", "atman"]
print(are_equivalent(word1, word2))
'''
'''
def count_evens(lst):
    j = 0
    
    for i in lst:
        if len(i) % 2 == 0:
            j += 1
    
    return j
lst = ["na", "nana", "nanana", "batman", "!"]
print(count_evens(lst))
'''
'''
def remove_name(people, secret_identity):
    for person in people[:]:
        if person == secret_identity:
            people.remove(person)

people = ["Bruce Wayne", "Clark Kent", "Bruce Wayne", "Diana Prince"]
secret_identity = "Bruce Wayne"
remove_name(people, secret_identity)
print(people)  
'''
'''
def move_zeroes(lst):
    result = []
    zero_count = 0
    for i in lst:
        if i == 0:
            zero_count +=1
        else:
            result.append(i)
    result.extend([0]*zero_count)
    return result
lst = [1, 0, 2, 0, 3, 0]
print(move_zeroes(lst))
'''


        