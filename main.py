from ex1 import sort_people

# people_list = [
#     {'name': 'alice', 'age': 20, 'weight': 160, 'sex': 'male', 'id': 1},
#     {'name': 'bob', 'age': 10, 'weight': 170, 'sex': 'male', 'id': 2},
#     {'name': 'charlie', 'age': 15, 'weight': 120, 'sex': 'female', 'id': 3},
# ]
# print(sort_people(people_list, 'weight', 'desc'))

 # ex2()
from ex2 import filter_males

people_list = [
    {'name': 'alice',   'age': 20, 'weight': 160, 'sex': 'male',   'id': 1},
    {'name': 'bob',     'age': 10, 'weight': 130, 'sex': 'male',   'id': 2},
    {'name': 'charlie', 'age': 15, 'weight': 120, 'sex': 'female', 'id': 3},
]
filtered_list = filter_males(people_list)
print(filtered_list)