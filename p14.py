#p4) read into a file
import os
filename = input("enter file name to read from ")
if os.path.isfile(filename):
	f = None
	try:
		with open(filename, "r") as f:
			data = f.read() 
			print(data)
	except Exception as e:
		print("issue", e)
else:
	print(filename ," does not exists ")

# semi ARM --> Automatic Resource Mgt	