import random
from re import X
from jokes import joke_list




x=59

for counter in range(30):
    num = random.randint(0,x)
    print(joke_list[num])
    joke_list.pop(num)
    x = x-1
    



