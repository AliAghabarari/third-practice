a = [True for i in range(3)]
b = [True for i in range(3)]
c = [True for i in range(3)]
d = [True for i in range(3)]

""" 

a[0] is about c and c[0] is opposite of that
a[1] is about b and c[1] and b[2] are opposites of that
a[2] is correct
b[0] is about d and d[0] is opposite of that
b[1] is about d and d[2] is opposite of that
c[2] is about d and d[1] is opposite of that

"""

true_statement = 0
false_statement = 0


if a[0]:

    c[0] = False

if a[1]:

    c[1], b[2] = False, False

if b[0]:

    d[0] = False

if b[1]:

    d[2] = False

if c[2]:

    d[1] = False


all_statement = []

for i in (a, b, c, d):
    all_statement.extend(i)

for i in all_statement:
    if i:
        true_statement += 1
    else:
        false_statement += 1

if true_statement == false_statement:
    print("The thief is B because :")
    print("Person D is not thief because the fisrt statement of it is false or lie")
    print("Person A is not thief because the third statement of D is lie and the second statement of A is correct")
    print("Person C is not thief because the second statement of it is false and the second statement of A is correct")
    print("As a result B is the thief")
