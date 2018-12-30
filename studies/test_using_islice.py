import re
import sys
from itertools import islice
import json


def clean(str_input_dataset):
	str_clean_dataset = str_input_dataset.lower()
	str_clean_dataset = str_clean_dataset.decode(encoding="ascii", errors="ignore")
	replacements = {",": "",
					":": "",
					"!": "",
					".": "",
					";": "",
					"?": "",
					"_": "",
					")": "",
					"(": "",
					"--": " "}

	str_clean_dataset = multi_replace(str_clean_dataset, replacements)

	return str_clean_dataset
# clean()

# *****************************************************************************

def multi_replace(string, replacements, ignore_case=False):
	"""
	    multi_replace()
	    Given a string and a dict, replaces occurrences of the dict keys found in the
	    string, with their corresponding values. The replacements will occur in "one pass",
	    i.e. there should be no clashes.
	    :param str string: string to perform replacements on
	    :param dict replacements: replacement dictionary {str_to_find: str_to_replace_with}
	    :param bool ignore_case: whether to ignore case when looking for matches
	    :rtype: str the replaced string
	    """

	rep_sorted = sorted(replacements, key=lambda s: len(s[0]), reverse=True)
	rep_escaped = [re.escape(replacement) for replacement in rep_sorted]
	pattern = re.compile("|".join(rep_escaped), re.I if ignore_case else 0)
	return pattern.sub(lambda match: replacements[match.group(0)], string)
# multi_replace()


# this would be a map() function -- just calculate the number of datasets and their size
# get the number of lines in the file
def map(file_input, int_desired_number_of_datasets):
	int_num_lines = 0
	dict_map={}
	with open(file_input, "r") as file:
		for i, l in enumerate(file):
			pass
		int_num_lines = i

	int_lines_in_dataset = int_num_lines / int_desired_number_of_datasets
	dict_map["int_lines_in_dataset"] = int_lines_in_dataset
	dict_map["int_num_lines"]=int_num_lines

	return(dict_map)
# end map() function

# a split() function would start the mp jobs, reduce() functions, to process each sub dataset
# each mp job would read the specified number of lines from the file, independently

# *****************************************************************************

def reduce(file_dataset, int_start_line, int_num_lines):
	global int_the
	str_content = ""
	dict_word_count={}

	with open(file_dataset, "r") as file:
		for row in islice(file, int_start_line, int_start_line + int_num_lines):
			str_content += row.strip() + " "

	str_clean_content = clean(str_content)
	lst_words = str_clean_content.split(" ")

	# print lst_words

	for word in lst_words:
		if word=="the": int_the=int_the+1
		if word == "": break
		try:
			dict_word_count[word]+=1
		except KeyError:
			dict_word_count[word] = 1

	return(dict_word_count)
# reduce()

# *****************************************************************************

# now the join() function would wait for all jobs to finish, then combine their results
def join(lst_word_counts):
	dict_combined_word_count = {}
	for lst_word_count in lst_word_counts:
		for word in lst_word_count:
			# if word == "": break
			try:
				dict_combined_word_count[word] += lst_word_count[word]
				# print("Summing: '" + word + "' count is " + str(dict_combined_word_count[word] + lst_word_count[word]))
			except KeyError:
				# print("(KeyError, adding '" + word + "' with initial count of " + str(lst_word_count[word]))
				dict_combined_word_count[word] = lst_word_count[word]

	return(dict_combined_word_count)

# *****************************************************************************

int_the=0

str_filename="tale_of_two_cities.txt"
lst_word_counts=[]

int_desired_number_of_datasets=25
int_dataset_size=(map(str_filename, int_desired_number_of_datasets))["int_lines_in_dataset"]
int_total_dataset_size=(map(str_filename, int_desired_number_of_datasets))["int_num_lines"]

print("Total size of input file: " + str(int_total_dataset_size))
print("Datasets: " + str(int_desired_number_of_datasets) + " datasets of " + str(int_dataset_size) + " elements")

for i in range(0,int_total_dataset_size,int_dataset_size):
	print("Calling reduce(" + str_filename + ", " + str(i) + ", " + str(i+int_dataset_size))
	lst_word_counts.append(reduce(str_filename,i,(i+int_dataset_size)))

print("lst_word_counts has " + str(len(lst_word_counts)) + " dictionaries")

print("Combined word count:")
dict_combined_word_count=join(lst_word_counts)
print json.dumps(dict_combined_word_count)

list_sorted_word_count = (sorted(dict_combined_word_count.items(), key=lambda t: t[1], reverse=True))

print(json.dumps(list_sorted_word_count))
print(len(dict_combined_word_count))

print("int_the = " + str(int_the))

