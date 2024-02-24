#take input and print output as we want
roll_no=12  #0
name="Vivek"  #1
age=345  #2
str="roll no is {}  name is {} age is {}"
# the input is taking as default 0,1,2
print(str.format(roll_no,name,age))
str="roll no is {0}  name is {1} age is {2}"
# the input is taking as default 0,1,2
print(str.format(roll_no,age,name))