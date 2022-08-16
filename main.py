from ex1 import sort_people

# people_list = [
#     {'name': 'alice', 'age': 20, 'weight': 160, 'sex': 'male', 'id': 1},
#     {'name': 'bob', 'age': 10, 'weight': 170, 'sex': 'male', 'id': 2},
#     {'name': 'charlie', 'age': 15, 'weight': 120, 'sex': 'female', 'id': 3},
# ]
# print(sort_people(people_list, 'weight', 'desc'))

# ex2()
from ex2 import filter_males

# people_list = [
#     {'name': 'alice',   'age': 20, 'weight': 160, 'sex': 'male',   'id': 1},
#     {'name': 'bob',     'age': 10, 'weight': 130, 'sex': 'male',   'id': 2},
#     {'name': 'charlie', 'age': 15, 'weight': 120, 'sex': 'female', 'id': 3},
# ]
# filtered_list = filter_males(people_list)
# print(filtered_list)

# ex3
from ex3 import calc_bmi

# people_list = [
#     {'id': 2, 'name': 'bob', 'weight_kg': 90, 'height_meters': 1.7},
#     {'id': 3, 'name': 'charlie', 'weight_kg': 80, 'height_meters': 1.8},
# ]
# new_people_list = calc_bmi(people_list)
# print(new_people_list)

# ex4
from ex4 import get_people

people_list = [
    {'name': 'alice',   'age': 20, 'weight': 160, 'sex': 'male',   'id': 1},
    {'name': 'bob',     'age': 10, 'weight': 130, 'sex': 'male',   'id': 2},
    {'name': 'charlie', 'age': 15, 'weight': 120, 'sex': 'female', 'id': 3},
]
print(get_people(people_list))