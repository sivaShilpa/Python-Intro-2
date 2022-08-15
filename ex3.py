def calc_bmi(people_list):
    newList = []

    for people in people_list:
        bmi = round(people['weight_kg'] / people['height_meters'] ** 2, 1)
        people["bmi"] = bmi
        newList.append(people)

    return newList
