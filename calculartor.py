def add(P,Q):
 return P+Q
def subtract(P,Q):
 return P-Q
def multiply(P,Q):
  return P*Q
def divide(P,Q):
 return P/Q
print('Please select the opration')
print('1.add')
print('2.subtract')
print('3.multiply')
print('4.divide')
choice=input('please enter your choice')
num1=int(input('please enter the first number'))
num2=int(input('please enter the second number'))
if choice=='1':
 print(add(num1,num2))
elif choice =='2':
 print(subtract(num1,num2))
elif choice =='3':
 print(multiply(num1,num2))
elif choice =='4':
 print(divide(num1,num2))
else:
 print('invalid input')