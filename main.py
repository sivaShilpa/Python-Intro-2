from datetime import time, datetime

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

# people_list = [
#     {'name': 'alice',   'age': 20, 'weight': 160, 'sex': 'male',   'id': 1},
#     {'name': 'bob',     'age': 10, 'weight': 130, 'sex': 'male',   'id': 2},
#     {'name': 'charlie', 'age': 15, 'weight': 120, 'sex': 'female', 'id': 3},
# ]
# print(get_people(people_list))

# ex5
from ex5 import send_message_to_sqs
from ex5 import read_message_from_sqs

# cat = {
#     "cat_id": 1,
#     "cat_name": "Gypsy",
#     "status": "hungry"
# }
# response = send_message_to_sqs(cat, 'https://sqs.us-east-1.amazonaws.com/425467241044/somequeue.fifo')
# while True:
#     time.sleep(3)
#     msg = read_message_from_sqs('https://sqs.us-east-1.amazonaws.com/425467241044/somequeue.fifo')
#     if msg:
#         print(msg)
#     else:
#         now = datetime.now().strftime("%H:%M:%S")
#         print(f"Polling SQS { now }...")

# ex6
from ex6 import save_to_cat_table

cat = {
    "cat_id": 1,
    "cat_name": "Gypsy",
    "status": "hungry"
}
save_to_cat_table(cat)
