# 17.	Rock-Paper-Scissors game logic.

u1 = input('Enter rock-paper-scissor : ')
u2 = input('Enter rock-paper-scissor : ')

hm = {
    'rock':'scissor',
    'paper':'rock',
    'scissor':'paper'
}

if None in (hm.get(u1),hm.get(u2)):
    print('INVALID INPUT')
elif u1==u2:
    print('TIE')
elif hm[u1]==u2:
    print('USER 1 WINS : ',u1)
elif hm[u2]==u1:
    print('USER 2 WINS : ',u2)