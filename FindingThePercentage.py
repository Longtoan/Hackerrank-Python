#INPUT                   
# 3
# Krishna 67 68 69  
# Arjun 70 98 63
# Malika 52 56 60
# Malika
###################
#OUTPUT
#56.00
n = int(input())
student_marks = {}
for _ in range(n):
    name, *line = input().split()
    scores = list(map(float, line))
    student_marks[name] = scores
query_name = input()
scro = 0
for i in student_marks:
    if(i == query_name):
        for j in student_marks[i]:
            scro += j
            
print("{0:.2f}".format(scro/3))
    