import io
import string
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


def multi_replace(string, replacements, ignore_case=False):
	"""
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


f = open("tale_of_two_cities.txt", "r")
str_input_dataset = f.read()

str_clean_dataset = clean(str_input_dataset)

print(str_clean_dataset)

print("Number of characters: " + str(len(str_clean_dataset)))

lst_new_dataset = str_clean_dataset.split("\n")
print(str(type(lst_new_dataset)))
print("Number of elements (lines): " + str(len(lst_new_dataset)))

str_line = lst_new_dataset[0]
print("Line 0: " + str_line)

lst_words = str_line.split(" ")
print("Line 0 has " + str(len(lst_words)) + " words")

sys.stdout.write("{")
for word in lst_words:
	print(word)

sys.stdout.write("}")

print
print

"""
Now using islice, we can read certain sections of the file without reading it all in to memory first
"""

# this would be a map() function -- just calculate the number of datasets and their size
# get the number of lines in the file
int_num_lines = 0
with open("tale_of_two_cities.txt", "r") as file:
	for i, l in enumerate(file):
		pass
	int_num_lines = i

print("Number of lines in the file: " + str(int_num_lines))

int_data_set_size = 25
int_lines_in_dataset = int_num_lines / int_data_set_size

print("Number of sub datasets: " + str(int_data_set_size))
print("Number of lines in each sub dataset: " + str(int_lines_in_dataset))
# end map() function

# a split() function would start the mp jobs, reduce() functions, to process each sub dataset
# each mp job would read the specified number of lines from the file, independently

# read the first 5 lines of the file into str_content
int_start_line = 0
int_num_of_lines = 5
str_content = ""

print
print("test using islice:")

def reduce(file_dataset, int_start_line, int_num_lines):
	str_content = ""
	dict_word_count={}

	with open(file_dataset, "r") as file:
		for row in islice(file, int_start_line, int_start_line + int_num_of_lines):
			str_content += row.strip() + " "

	str_clean_content = clean(str_content)
	lst_words = str_clean_content.split(" ")
	for word in lst_words:
		if word == "": break
		try:
			dict_word_count[word]+=1
		except KeyError:
			dict_word_count[word] = 1

	return(dict_word_count)

print

lst_word_counts=[]
lst_word_counts.append(reduce("tale_of_two_cities.txt", 0, 5))
lst_word_counts.append(reduce("tale_of_two_cities.txt", 6, 5))
lst_word_counts.append(reduce("tale_of_two_cities.txt", 11, 5))

# now the join() function would wait for all jobs to finish, then combine their results
def join(lst_word_counts):
	dict_combined_word_count = {}
	for lst_word_count in lst_word_counts:
		for word in lst_word_count:
			if word == "": break
			try:
				dict_combined_word_count[word] += lst_word_count[word]
			except KeyError:
				dict_combined_word_count[word] = lst_word_count[word]

	return(dict_combined_word_count)

print
print("Combined word count:")
print(json.dumps(join(lst_word_counts)))
