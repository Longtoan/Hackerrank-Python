# Consider a list (list = []). You can perform the following commands:

# insert i e: Insert integer  at position .
# print: Print the list.
# remove e: Delete the first occurrence of integer .
# append e: Insert integer  at the end of the list.
# sort: Sort the list.
# pop: Pop the last element from the list.
# reverse: Reverse the list
# INPUT
# 12
# insert 0 5
# insert 1 10
# insert 0 6
# print
# remove 6
# append 9
# append 1
# sort
# print
# pop
# reverse
# print
# OUTPUT
# [6, 5, 10]
# [1, 5, 9, 10]
# [9, 5, 1]

result = []
n = int(input())
for _ in range(n):
    userInput = input().split(" ")
    command =  userInput[0]
    if(command == "insert"):
        result.insert(int(userInput[1]),int(userInput[2]))
    if(command == "remove"):
        result.remove(int(userInput[1]))
    if(command == "append"):
        result.append(int(userInput[1]))
    if(command == "sort"):
        result.sort()
    if(command == "reverse"):
        result.reverse()
    if(command == "pop"):
        result.pop()
    if(command == "print"):
        print(result)
    