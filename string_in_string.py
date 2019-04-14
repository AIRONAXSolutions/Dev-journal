#python code to find a string within a string

list = [
"IF7MF8IPDD4VET2CZB14",
"3P37D5RYYX0GLQBKJVXZ",
"TBLG5SU8SV52R0HI06FY",
"BLG5SU8SV52R0HIIF7MF",]

str = "IF7MF"
for key in list:
	if str in key:
	    print('=========== match ===========')
	else:
		print('=========== unique ===========')
