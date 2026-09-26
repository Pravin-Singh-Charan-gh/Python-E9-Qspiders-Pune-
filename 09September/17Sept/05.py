
#         * 
#       * * 
#     * * * 
#   * * * * 
# * * * * * 

n = int(input('Enter the number : '))
for i in range(n,-1,-1):
    for j in range(n):
        if j<i:
            print(end='  ')
        else:
            print(end='* ')
    print()
    
