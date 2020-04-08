# str.isalnum()
# This method check if all the charater of a string are alphanumberic (a-z and  0-9)
# >>> print 'ab123'.isalnum()
# True
# >>> print 'ab123#'.isalnum()
# False
######################################################################
# str.isalpha()
# this method check if all the charater of a string are alphabetical (a-z and A-z)
# >>> print 'abcD'.isalpha()
# True
# >>> print 'abcd1'.isalpha()
# False
######################################################################
# str.isdigit()
# this method check if all the charater of a string are digit (0-9 )
# >>> print '1234'.isdigit()
# True
# >>> print '123edsd'.isdigit()
# False
######################################################################

# INPUT
# qA2
# OUPUT
# In the first line, print True if S has any alphanumeric characters. Otherwise, print False.
# In the second line, print True if S has any alphabetical characters. Otherwise, print False.
# In the third line, print True if S has any digits. Otherwise, print False.
# In the fourth line, print True if S has any lowercase characters. Otherwise, print False.
# In the fifth line, print True if S has any uppercase characters. Otherwise, print False.


if __name__ == '__main__':
    s = input()

    print(any(i.isalnum() for i in s))
    print(any(i.isalpha() for i in s))
    print(any(i.isdigit() for i in s))
    print(any(i.islower() for i in s))
    print(any(i.isupper() for i in s))
