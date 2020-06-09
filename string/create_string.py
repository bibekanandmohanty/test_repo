#Intro to strings
my_name="bibek"
my_newname="bibek1"
print(f"my name is : {my_name} \nmy new name is : {my_newname}")
space=""
space1=" "
print(f"{bool(space)}")
print(f"{bool(space1)}")

my_fav_script="python scripting"
print(my_fav_script)
print(my_fav_script[0])
print(my_fav_script[5])
print(my_fav_script[5])
print(my_fav_script[-1])
print(my_fav_script[5])
print(my_fav_script[0:5]) #prints character from 0 to 4
print(my_fav_script[0:])  #prints 0 to last
print(my_fav_script[:5])  #prints character from 0 to 4
print(my_fav_script[4:11])

#strings are immutable.. That means u cant delete or assign part of the string. 
#length of the string
mystringlen=len(my_fav_script)
print(f"length of the given string is : {len(my_fav_script)}")
print(my_fav_script[-16:-5])

test=bibek
test1=mohanty
space=" "
add_test=test1+" "+test2+"is very handsome"
