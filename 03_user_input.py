# ------------SECTION 3: list---------------
friends = ["Jim", "Karen", "Tommy"]
mixed = ["Jim", 23, True, "Kevin", "Laurie"]  # this is also fine in python
lucky_numbers = [3, 7, -1, 9, 17, 67]
# print(mixed)
# print(mixed[0])
# print(mixed[-1])  # negative index means searching from the end of the list, here -1 stands for 'True'
# print(mixed[1:3])  # an index range is supported. including 1, excluding 3 !!!
# print(mixed[1:])  # from 1 to the end

# -----------list functions---------------
friends.extend(mixed)
print(friends)  # mixed is appended to the trailing of friends
friends.append("Creed")  # append element to the end of the list
friends.insert(2, "3rd")  # insert element at a certain index
print(friends)
friends.remove("3rd")  # remove certain elements
print(friends)
friends.pop(0)  # remove an element at a certain index
print(friends)
friends.pop()  # remove an element at the end of the list
print(friends)
print(friends.index("Jim"))  # get the index of an element
# print(friends.index("NO such element"))  # this will get an error
print(friends.count("Jim"))  # how many Jim are there in the list?

lucky_numbers.sort()
print(lucky_numbers)  # sort a list with all elements of the same type!!! otherwise will be an error!!
lucky_numbers.reverse()
print(lucky_numbers)

friends_2 = friends.copy()
print(friends_2)




