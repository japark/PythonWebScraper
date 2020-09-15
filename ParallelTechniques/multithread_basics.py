import time
import _thread

'''
Basic example of multi-thread using _thread module
'''

def print_time(threadName, delay, iterations):
	start = int(time.time())
	for i in range(0, iterations):
		time.sleep(delay)
		seconds_elapsed = str(int(time.time()) - start)
		print('{} {}'.format(seconds_elapsed, threadName))


try:
	_thread.start_new_thread(print_time, ('Counter', 1, 100))
	_thread.start_new_thread(print_time, ('Fizz', 3, 33))
	_thread.start_new_thread(print_time, ('Buzz', 5, 20))
except:
	print ("Error: unable to start thread")

while 1:
	pass
