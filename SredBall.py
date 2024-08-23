grades = [[5, 3, 3, 4, 5], [2, 2, 2, 3], [4, 5, 5, 2], [4, 4, 3], [5, 5, 5, 4, 5]]
students = {'Johnny', 'Bilbo', 'Steve', 'Khendrik', 'Aaron'}
a = list(students)
a.sort()
#print(a)
grades[0] = sum(grades[0]) / len(grades[0]) #среднее значение
grades[1] = sum(grades[1]) / len(grades[1])
grades[2] = sum(grades[2]) / len(grades[2])
grades[3] = sum(grades[3]) / len(grades[3])
grades[4] = sum(grades[4]) / len(grades[4])
#print(grades)
stud_sr_bal = {}
#stud_sr_bal['Aaron'] = grades[0]
stud_sr_bal.update({a[0]: grades[0], a[1]: grades[1],a[2]: grades[2],a[3]: grades[3],a[4]: grades[4]})
print(stud_sr_bal)

