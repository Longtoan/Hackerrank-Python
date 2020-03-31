#Input 5
#input 2 3 6 6 5
#output 5

n = int(input())
a = list(map(int,input().split()))
# max = 0
rev_arr = sorted(a, reverse = True)

for i in range(len(rev_arr)):
    if(rev_arr[i+1] < max(rev_arr)):
        print(rev_arr[i+1])
        break 