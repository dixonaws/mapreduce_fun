import multiprocessing as mp
import random
import string

random.seed(123)

output=mp.Queue()

def rand_string(length, output):
	""" Generates a random string of numbers """
	rand_str=''.join(random.choice(
		string.ascii_lowercase +
		string.ascii_uppercase +
		string.digits)
	for i in range(length))

	output.put(rand_str)
# rand_string()

processes=[mp.Process(target=rand_string, args=(5, output)) for x in range(4)]

# run the processes
for p in processes:
	p.start()

# exit the completed processes
for p in processes:
	print(p.name + ": " + str(p.is_alive()))
	p.join()

# get process results from the output queue
results=[output.get() for p in processes]

print results