""" Grouping with dictionaries """

import collections

fruit_bag = ['apple','grapes','apple','mango','mango','apple',
             'banana','orange','guava','sapota','apple','orange',
             'litchi','strawberry','lemon','apple','grapes']

def group_solution_a():

    fruit_group = {}
    for fruit in fruit_bag:
        if fruit not in fruit_group:
            fruit_group[fruit] = 0
        fruit_group[fruit] += 1 

    return fruit_group

def group_solution_b1():

    fruit_group = {}
    for fruit in fruit_bag:
        fruit_group[fruit] = fruit_group.get(fruit, 0) + 1  

    return fruit_group

def group_solution_b2():

    fruit_group = collections.defaultdict(int)
    for fruit in fruit_bag:
        fruit_group[fruit] += 1

    return fruit_group

if __name__ == "__main__":
    print group_solution_a()
    print group_solution_b1()
    print group_solution_b2()
