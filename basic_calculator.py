# define the functions
def add(a,b):
	return a+b
def sub(a,b):
	return a-b
def mul(a,b):
	return a*b
def div(a,b):
	return a/b

while True:
# print options to the user
	print('''operations you can perform:
press A for addition
press S for subtraction
press M for multiplication
press D for divide
press E for exit''')
# ask for values
	user=input("What operation do you want perform: ")
	if user == "E" or len(user)==0:
		break

	x=float(input("Enter the first number:"))
	y=float(input("Enter the second number:"))
	
	if user == "A":
		print("=",add(x,y),"\n")
	elif user == "S":
		print("=",sub(x,y),"\n")
	elif user == "M":
		print("=",mul(x,y),"\n")
	elif user == "D":
		print("=",div(x,y),"\n")
	
	     
	



