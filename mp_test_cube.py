import multiprocessing as mp
import random
import string

random.seed(123)

output=mp.Queue()

def cube(x):
	""" Generates the cube of the input x """
	return(x**3)

# cube()

pool=mp.Pool(processes=6)

results0=[pool.apply(cube, args=(x,)) for x in range(1,7)]
print results0

print

results1=pool.map(cube, range(1,7))
print results1

print

lst_args=[1,2,3,4,5,6]
results2=pool.map(cube,lst_args)
print results2


