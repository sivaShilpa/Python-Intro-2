def filter_males(people_list):
    newList = []
    for people in people_list:
        if people['sex'] == 'male':
            newList.append(people)

    return newList
