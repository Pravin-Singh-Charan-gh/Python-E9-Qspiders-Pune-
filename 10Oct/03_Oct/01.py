#Write a program which takes n number of inputs from the user
#and give the sum of it

def n_sum(*args):
    s = 0
    for i in args:
        s+=i
    return s

print(n_sum(1,2,3,4,5))
