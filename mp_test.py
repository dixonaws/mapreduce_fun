import multiprocessing as mp
import random
import string

random.seed(123)

output = mp.Queue()


def rand_string(length, output):
	""" Generates a random string of numbers """
	rand_str = ''.join(random.choice(
		string.ascii_lowercase +
		string.ascii_uppercase +
		string.digits)
					   for i in range(length))

	output.put(rand_str)


# rand_string()


# processes=[mp.Process(target=rand_string, args=(5, output)) for x in range(4)]
lst_processes = []
for x in range(4):
	lst_processes.append(mp.Process(target=rand_string, args=(5, output)))

print("lst_processes is a " + str(type(lst_processes)))

# run the processes
for p in lst_processes:
	p.start()

# exit the completed processes
for p in lst_processes:
	print(p.name + ": " + str(p.is_alive()))
	p.join()

# get process results from the output queue
# lst_results=[output.get() for p in processes]

lst_results = []
for p in lst_processes:
	lst_results.append(output.get())

print("lst_results is a " + str(type(lst_results)))
print lst_results
