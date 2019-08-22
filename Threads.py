#python program to illustrate the concept of multithreading
#importing threading library
import threading

global x 
x = 10

def print_cube(num):
	'''
		Function to print the cube of a number
	'''
	print("Cube of :{}".format(num * num * num))
	global x
	x = 20
	print("Modifying x : {}".format(x))
	
def print_square(num):
	'''
	function to print the square of a number
	'''
	print("Square:{}".format(num * num))
	global x
	x = 30
	print("Modifying in print square method:{}".format(x))

if __name__=="__main__":
	t1 = threading.Thread(target=print_cube, args=(10,))
	t2 = threading.Thread(target=print_square, args=(5,))
	
	#starting thread 1
	t1.start()
	
	#starting thread 2
	t2.start()
	
	#wait until thread 1 is completely executed
	#t1.join()
	
	#wait until thread 2 is completely executed
	#t2.join()
	
	print("Continue with main program")
	
	print("Global x : {} ".format(x))
	#both threads are executed successfully
	print("Done!")



