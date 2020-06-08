# data types or variable data types in python
x=5
print(id(x)) #address of x

# Every value in python has a data type .
# Basic data types :
# Numbers(int,floatannd complex)
# strings
# booolean
x=3
y=4.6
z=3+4j
print(x,type(x))
print(y,type(y))
print(z)
print(x,y,z)

lang_name="python"
print(lang_name)
my_name="bibekanand"
print(my_name)
print(my_name,type(my_name))
my_value=True
my_new_value=False
print(my_value,type(my_value))
print(my_value,type(my_new_value))

# Typecasting or type conversion
x=56
print(x,type(x))
y=str(x)
print(y,type(y))
z=bool(x)
print(z,type(z))
m=5.6
print(int(x))
x="45"
print(int(x))

# Any datatype can be converted into boolean
# bool(any_data_type)=True or False
# bool(empty)=False bool(0) bool(None) bool(()) bool({}) bool([])
# Ant datatype can be converted into string but reverse is not always true
# bool(non-empty)=True
bool(0)
bool(None)
bool(())
