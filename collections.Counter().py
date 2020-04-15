# he first line contains , the number of shoes.
# The second line contains the space separated list of all the shoe sizes in the shop.
# The third line contains , the number of customers.
# The next  lines contain the space separated values of the  desired by the customer and , the price of the shoe.

shoes = int(input())

allsize = list(map(int,input().split()))
n = int(input())

result = 0
for i in range(n):
    size,price = map(int,input().split())
    if(size in allsize):
        allsize.remove(size)
        result += price
print(result)
