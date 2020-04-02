#INPUT
# HackerRank.com presents "Pythonist 2".
#OUPUT
#hACKERrANK.COM PRESENTS "pYTHONIST 2".

def swap_case(s):
    result = ""
    for i in range(len(s)):
        if(s[i].islower() == True):
            result += s[i].upper()
        else:
            result += s[i].lower()
    print(result)

if __name__ == '__main__':
    s = input()
    swap_case(s)