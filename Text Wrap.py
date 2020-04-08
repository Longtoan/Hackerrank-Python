# INPUT
# The first line containts a string S
# the second line contraints the with w
# OUPUT
# Print the text wrapped paragraph.

import textwrap


def wrap(string, max_width):
    my_wrap = textwrap.TextWrapper(width=max_width)

    # wraplist = my_wrap.wrap(text=string)
    # for line in wraplist:
    # print(line)
    return my_wrap.fill(text=string)


if __name__ == '__main__':
    string, max_width = input(), int(input())
    result = wrap(string, max_width)
    print(result)
