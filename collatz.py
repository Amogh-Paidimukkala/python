a=int(input("Enter a number greater than 0"));
print("You chose number ",a);
while(a>1):
	if(a%2==0):
		a=a/2;
		print(a);
	
	elif(a==1):
		break;

	else:
		a=(a*3)+1;
		print(a);

			
else:
	print("Enter a number greater than 0")
