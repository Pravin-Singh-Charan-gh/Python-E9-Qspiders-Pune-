##Exercise 28. Odd/Even List Splitter
##Practice Problem: Start with a list of 10 numbers. Iterate through them and sort them into two separate lists: one for even numbers and one for odd numbers.

def odd_even_split(nums):
    ans = [[],[]]
    for i in nums:
        if i%2:
            ans[1].append(i)
        else:
            ans[0].append(i)
    return ans

nums = eval(input('Enter the list : '))

ans = odd_even_split(nums)

print('Evens :',ans[0])
print('Odds :', ans[1])

class Main{
    public static void main(String []args){
        System.out.println('Hello World');
    }
}
