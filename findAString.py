def count_substring(string, sub_string):
    string.lower()
    sub_string.lower()
    len_sub = len(sub_string)
    count = 0
    for i in range(len(string)):
        if(string[i] == sub_string[0]):
            if(string[i:(i+len_sub)] == sub_string): 
                count += 1

    return count


if __name__ == '__main__':
    string = input().strip()
    sub_string = input().strip()

    count = count_substring(string, sub_string)
    print(count)
