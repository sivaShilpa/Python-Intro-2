def sort_people(people, attribute, order):
    if order == 'asc':
        return sorted(people, key=lambda i: i[attribute])
    elif order == 'desc':
        return sorted(people, key=lambda i: i[attribute], reverse=True)