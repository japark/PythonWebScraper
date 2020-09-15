import time
from multiprocessing import Process

'''
Basic example of multi-process using multiprocessing module
'''

def print_time(threadName, delay, iterations):
	start = int(time.time())
	for i in range(0, iterations):
		time.sleep(delay)
		seconds_elapsed = str(int(time.time()) - start)
		print('{} {}'.format(seconds_elapsed, threadName))

def main():
	processes = []
	processes.append(Process(target=print_time, args=('Counter', 1, 30)))
	processes.append(Process(target=print_time, args=('Fizz', 3, 10)))
	processes.append(Process(target=print_time, args=('Buzz', 5, 6)))

	for p in processes:
		p.start()

	for p in processes:
		p.join()

	print('Program complete')


if __name__ == '__main__':
	main()
