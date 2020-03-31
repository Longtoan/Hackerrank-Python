a= [ ]
scores = []
for _ in range(int(input())):
    name = input()
    score = float(input())
    a.append([name,score])
    scores.append(score)
min = 100
second_stored = sorted(list(dict.fromkeys(scores)))[1] #dict.fromkeys loại bỏ trùng
for i,j in sorted(a):
    if(j==second_stored):
        print(i)