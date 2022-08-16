def get_people(people_list):
    newList = []

    for person in people_list:
        if person['weight'] >= 15:
            newList.append(person)

    return newList
