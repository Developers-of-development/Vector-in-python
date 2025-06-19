from vector import vector

# how to create vactor
vec = vector([1,2,3,4,5])

# printing vector
vec.show()

# push_back func + print that
vec.push_back(6)
vec.show()

# pop_back 
vec.pop_back() # it should empty bcz it remove last value only like cpp
vec.show()

# at - works like list[] it show index
print(vec.at(2)) #3

# back return last valule
print(vec.back())

# front return first value
print(vec.front())

# show - can print all vector easyly without any loop directly
vec.show()

# ease - remove value by entering value if they are in vector

vec.ease(1)
vec.show() # 2 3 4 5

# In - shows it value index if avaible and if not then shows value not found
print(vec.In(5))