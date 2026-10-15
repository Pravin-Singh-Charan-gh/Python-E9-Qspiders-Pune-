
class GF_mandi:
    starter = ['masala papad',
               'paneer tikka',
               'paneer chilli'
               ]
    main_course = ['paneer pasanda',
                   'mushroom masal'
                   'butter chicken',
                   'fish curry' ,'rice']
    breads = ['roti',
              'butter nan',
              'garlic nan',
              'rumali roti']

user1 = GF_mandi()
user1.name = 'rohan'
user1.type = 'veg'

user2 = GF_mandi()
user2.name = 'ritesh'

print('user1 :',user1.name)
print('user1 :',user1.type)

print('user2 :',user2.name)
##print('user2 :',user2.type)   #ERROR

print(user1.main_course)
print(user2.main_course)
