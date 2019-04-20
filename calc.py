def add(a,b):
  return a+b
def sub(a,b):
  return a-b
def mult(a,b):
  return a*b
def pow(a,b):
  return a**b
def div(a,b):
  return a//b
x=int(input("Enter first number:"))
y=int(input("Enter second number:"))
while(True):
  print("Enter the choice\n1.add\n2.subtract\n3.multiply\n4.power\n5.divide\n")
  choice=int(input())
  if(choice==1):
    add(x,y)
  elif(choice==2):
    sub(x,y)
  elif(choice==3):
    mult(x,y)
  elif(choice==4):
    pow(x,y)
  elif(choice==5):
    div(x,y)
  else:
  print("Enter valid choice")
  
  
