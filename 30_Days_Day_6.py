# Hackerrank 30 days challenge day 5 Solution

# Given a string, , of length  that is indexed from  to , print its even-indexed and odd-indexed characters as  space-separated strings on a single line (see the Sample below for more detail).

# Note:  is considered to be an even index.

# Solution 

for i in range(int(input())):
    s=input()
    print(s[::2], s[1::2])
