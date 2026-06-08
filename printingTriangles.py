# Just a bit of school CS coursework.
# I wanted to print triangles. Right-angled triangles, specifically. And I wanted to print a ton of them. So let's try that!

i = 1
n = int(input("Enter number of triangles to be printed "))
s = int(input("Enter length of perpendicular/base "))
while i <= n:
    j = 1
    while j <= s:
        print("*"*j)
        j += 1
    print() # start again in a new line, otherwise all the "triangles" will be on one line
    i += 1
