import os

def simple_function(num):
	if "DATABASE_URL" in os.environ:
		print(os.environ["DATABASE_URL"])
		return num
	else:
		return "Error"




