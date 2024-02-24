a,b=input("enter number").split()
#split use take input in string format
print(a*2)
#so we need to type cast in int format
a=int(a)
b=int(b)
#use map to read multiple input from single line
c=a*b
print("the multiply of %d and%d is %d"%(a,b,c))