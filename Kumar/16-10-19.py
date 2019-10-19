#modules save another .py file in same folder
import task1
print(task1.a)
print(task1.add(10,20))



#from module_name import property

from task1 import a
print(a)
from task1 import add
print(add(10,20))

from task1 import div
print(div(88,2))

from task1 import avg
print(avg(1,2))

