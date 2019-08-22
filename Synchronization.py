import threading

global x 
x = 0

def increment():
	global x
	x += 1
	
def thread_task():
	for _ in range(1000):
		increment()
	
if "__name__" == __main__:
	t1 = threading.Thread(target=thread_task, name="t1")
	