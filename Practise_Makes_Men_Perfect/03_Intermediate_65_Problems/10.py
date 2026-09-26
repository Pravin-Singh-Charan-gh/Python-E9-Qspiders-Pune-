##Exercise 10: Circular Shift (Rotation)
##Practice Problem: Create a function rotate_list(lst, n, direction) that shifts the elements of a list by N positions. The direction can be ‘left’ or ‘right’.


def rotate_list(lst,k,direction):
    if not lst:
        return lst
    k = k%len(lst)
    if direction=='left':
        return lst[k:]+lst[:k:]
    else:
        return lst[-k:] + lst[:-k]
    
lst = eval(input('Enter the list : '))
n = int(input('Enter the number : '))
direction = input('Enter the dirction(left or right) : ')

print(rotate_list(lst,n,direction))
