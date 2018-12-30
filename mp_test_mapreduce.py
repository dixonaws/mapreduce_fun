from MapReduceUtil import Clean
from itertools import islice
import multiprocessing as mp
import random
import string

import json
import sys


def map(str_filename, int_desired_number_of_datasets):
	"""
	map() calculates the number of datasets and their sizes
	:param str_filename: the dataset, name of the file to process (assume it is in the working directory)
	:param int_desired_number_of_datasets: the number of sub datasets to calculate
	:return: dict_map, a dict object containing two keys: the total number of lines in the file, and int_lines_in_dataset, the
	number of lines that should be in each sub dataset
	"""
	int_num_lines = 0
	dict_map = {}
	with open(str_filename, "r") as file:
		for i, l in enumerate(file):
			pass
		int_num_lines = i

	int_lines_in_dataset = int_num_lines / int_desired_number_of_datasets
	dict_map["int_lines_in_dataset"] = int_lines_in_dataset
	dict_map["int_num_lines"] = int_num_lines

	return (dict_map)


# map()

# *****

def reduce(str_filename, int_startpos, int_dataset_size, output):
	"""
	reduce() processes a sub dataset by reading the portion of the file that represents the sub dataset
	:param str_filename:
	:param int_startpos:
	:param int_dataset_size: number of lines to process for the sub dataset
	:return: dict_dataset, with words as keys and frequency as values for the sub dataset
	"""
	str_dataset = ""
	dict_dataset = {}
	with open(str_filename, "r") as file:
		file.seek(0)
		for row in islice(file, int_startpos, int_dataset_size):
			str_dataset += row.strip() + " "

		str_clean_dataset = Clean.clean(str_dataset)
		lst_dataset = str_clean_dataset.split(" ")

	for word in lst_dataset:
		try:
			dict_dataset[word] += 1
		except KeyError:
			dict_dataset[word] = 1

	# return (dict_dataset)
	output.put(dict_dataset)


# reduce()

# *****

def main():
	lst_all_datasets = []
	dict_all_words = {}

	output = mp.Queue()

	random.seed(123)

	pool = mp.Pool(processes=8)

	str_filename = "bible.txt"
	int_desired_number_of_datasets = 25
	dict_map = map(str_filename, int_desired_number_of_datasets)

	int_num_lines = dict_map["int_num_lines"]
	int_lines_in_dataset = dict_map["int_lines_in_dataset"]

	int_step = (int_num_lines / int_desired_number_of_datasets)

	lst_processes = []

	# create a list so that we can start threads for each call to reduce()
	for x in range(0, int_num_lines, int_step):
		# lst_all_datasets.append(reduce(str_filename, x, (x + int_step)))
		lst_processes.append(mp.Process(target=reduce, args=(str_filename, x, (x + int_step), output)))

	print("lst_processes contains " + str(len(lst_processes)) + " processes")

	lst_results = []

	# start the parallel processes
	for p in lst_processes:
		p.start()

	# exit the completed processes
	for p in lst_processes:
		print(p.name + ": " + str(p.is_alive()))
		lst_results.append(output.get())

	print("lst_results contains: " + str(len(lst_results)) + " elements")

	print("lst_results is a " + str(type(lst_results)))

	for dict_word_count in lst_results:
		for word in dict_word_count:
			try:
				dict_all_words[word] += dict_word_count.get(word)
			except KeyError:
				dict_all_words[word] = dict_word_count.get(word)
	# for word
	# for lst_words

	lst_sorted_word_count = (sorted(dict_all_words.items(), key=lambda t: t[1], reverse=True))

	print("All words, word count: " + str(lst_sorted_word_count))


# main()

main()
