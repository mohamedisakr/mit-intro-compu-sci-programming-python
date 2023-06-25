def avg(grades):
    assert len(grades) != 0, 'no grades data found'
    return round(sum(grades)/len(grades), 2)
    # try:
    # except ZeroDivisionError:
    #     print('warning: no grades')
    #     return 0.0


test_grades = [[['peter', 'parker'], [10.0, 5.0, 85.0]],
               [['bruce', 'wayne'], [10.0, 8.0, 74.0]],
               [['captain', 'america'], [8.0, 10.0, 96.0]],
               [['deadpool'], []]]


new_grades = []

for item in test_grades:
    # new_grades.append([item[0], item[1], avg(item[1])])
    new_grades.append([" ".join(item[0]), item[1], avg(item[1])])

print(new_grades)
