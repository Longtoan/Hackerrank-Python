#INPUT
#this is a string   
#OUPUT 
#this-is-a-string

# string = input().split(" ")
# print("-".join(string))

def split_and_join(line):
    # write your code here
    result = ""
    for i in range(len(line)):
        if(line[i] == " "):
            result += "-"
        else:
            result += line[i]
    return result
if __name__ == '__main__':
    line = input()
    result = split_and_join(line)
    print(result)