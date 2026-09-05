#WAP for printing the winner of rock paper scissor

u1 = input('Enter Rock, Paper or Scissor: ')
u2 = input('Enter Rock, Paper or Scissor: ')

d={'rock':'paper', 'paper':'scissor', 'scissor':'rock'}

if (d.get(u1) and d.get(u2))==None:
    print('Invalid Input')
elif u1==u2:
    print('TIE')
elif d[u1]==u2:
    print('USER 2 WINS!')
else:
    print('USER 1 WINS')


#if u1==u2:
#    print("TIE")
    
#elif u1=='Rock':
#    if u2=='Scissor':
#        print('U1')
#    else:
#        print('U2')
        
#elif u1=='Paper':
#    if u2=='Scissor':
#        print('U2')
#    else:
#        print('U1')
        
#else:
#    if u2=='Rock':
#        print('U2')
#    else:
#        print('U1')
