import  make_pizza#importing an entire module
make_pizza.make_pizza(16,'apple','milk')
make_pizza.make_pizza(12,'cake')
from make_pizza import  make_pizza#importing a specific functiong
make_pizza(16, 'pepperoni')
make_pizza(12, 'mushrooms', 'green peppers', 'extra cheese')
from make_pizza import  make_pizza as mp #using as to give a function an alias
mp(16, 'pepperoni')
mp(12, 'mushrooms', 'green peppers', 'extra cheese')
from make_pizza import * #从module中导入所有的函数，当function和project中函数同名时会产生冲突
make_pizza(20, 'pepperoni')
make_pizza(22, 'mushrooms', 'green peppers', 'extra cheese')