x = 24
team = 'flyers'
win = False
print(x)
if(x > 10):
    print('that is larger than 10')
else:
    print('that is not larger than 10')
if(x < 0 and win == False):
    print('negative and true')
elif(x >= 0 and win == False):
    print('positive and false')
elif(x > 100 or win == True):
    print('large or true')
else:
    print("i don't know")

equipment = ['skates' , 'helmet' , 'stick']
my_nums = [1,2,3,4,5,6]

for string in equipment:
    print(string)

for num in my_nums:
    print('look at this number: ', num)

def static_grettings():
    print('hello mark')

static_grettings()

def dynamic_gretting(to_greet):
    print('hola' , to_greet)

dynamic_gretting('bob')
dynamic_gretting('jill')
dynamic_gretting('jack')



