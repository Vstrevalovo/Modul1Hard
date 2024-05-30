grades = [[5, 3, 3, 5, 4], [2, 2, 2, 3], [4, 5, 5, 2], [4, 4, 3], [5, 5, 5, 4, 5]]
students = {'Johnny', 'Bilbo', 'Steve', 'Khendrik', 'Aaron'}

count0 = grades[0]
count0 = len(count0)
mean0 = (sum(grades[0]))/count0
count1 = grades[1]
count1 = len(count1)
mean1 = (sum(grades[1]))/count1
count2 = grades[2]
count2 = len(count2)
mean2 = (sum(grades[2]))/count2
count3 = grades[3]
count3 = len(count3)
mean3 = (sum(grades[3]))/count3
count4 = grades[4]
count4 = len(count4)
mean4 = (sum(grades[4]))/count4
mean = [mean0, mean1, mean2, mean3, mean4]

aLphabet = {'A':1,'B':2,'C':3,'D':4,'E':5,'F':6,'G':7,'H':8,'I':9,'J':10,'K':11,'L':12,'M':13,'N':14,'O':15,'P':16,'Q':17,'R':18,'S':19,'T':20,'U':21,'V':22,'W':23,'X':24,'Y':25,'Z':26}

students = list(students)
students_Letters = {students[0][0]:students[0],students[1][0]:students[1],students[2][0]:students[2],students[3][0]:students[3],students[4][0]:students[4]}
result={students_Letters.pop(min(students_Letters))}
result=list(result)
result_f = {result[0]:mean.pop(0)}
result={students_Letters.pop(min(students_Letters))}
result=list(result)
result_f[result[0]] = mean.pop(0)
result={students_Letters.pop(min(students_Letters))}
result=list(result)
result_f[result[0]] = mean.pop(0)
result={students_Letters.pop(min(students_Letters))}
result=list(result)
result_f[result[0]] = mean.pop(0)
result={students_Letters.pop(min(students_Letters))}
result=list(result)
result_f[result[0]] = mean.pop(0)
print(result_f)