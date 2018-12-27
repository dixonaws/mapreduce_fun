import io
import sys
import time
import json

def main():
	int_master_start_time = int(round(time.time() * 1000))

	sys.stdout.write("Opening file... ")
	file_plaintext=open("tale_of_two_cities.txt", "r")
	print("done (" + file_plaintext.name + ")")

	# read each line of the file into a string
	sys.stdout.write("Reading file... ")
	int_start_time = int(round(time.time() * 1000))
	list_plaintext_lines = file_plaintext.readlines()
	int_end_time = int(round(time.time() * 1000))
	int_elapsed_time = int_end_time - int_start_time
	print("done (" + str(int_elapsed_time) + "ms).")

	sys.stdout.write("Closing file... ")
	file_plaintext.close()
	print("done.")

	# run a simulated map() function
	sys.stdout.write("Running map() function... ")
	int_start_time=int(round(time.time() * 1000))
	list_line_packages=map(list_plaintext_lines, 25)
	int_end_time = int(round(time.time() * 1000))
	int_elapsed_time = int_end_time - int_start_time
	print("done (" + str(int_elapsed_time) + "ms).")

	# run a simulated reduce() function
	int_start_time = int(round(time.time() * 1000))
	sys.stdout.write("Running reduce() function... ")
	list_lines=reduce(list_line_packages)
	int_end_time = int(round(time.time() * 1000))
	int_elapsed_time = int_end_time - int_start_time
	print("done (" + str(int_elapsed_time) + "ms).")

	print("list_lines has " + str(len(list_lines)) + " elements.")
	# print(list_sorted_lines)

	# combine the results from the map() function into list_result - the frequency of all words in the text file
	dict_result={}
	for package in list_lines:
		for word in package:
			# dict_result[word]=dict_result[word]+dict_result.get(word)

			try:
				dict_result[word] = dict_result[word] + package.get(word)
			except KeyError:
				dict_result[word] = 1
			# try
		# for word
	# for package

	print("Distinct words: " + str(len(dict_result)))

	list_sorted_word_count = (sorted(dict_result.items(), key=lambda t: t[1], reverse=True))

	print("dict_result: " + str(json.dumps(list_sorted_word_count)))

	int_master_end_time = int(round(time.time() * 1000))

	int_master_elapsed_time=int_master_end_time-int_master_start_time
	print("Finished in " + str(int_master_elapsed_time) + "ms.")


# main()

# Input: A file object and the desired number of packages to produce
# Output: list_packages, a list containing "packages" of lines from the input file
# Description: The map() function transforms a text file into packages of lines that can be used
# in a reduce() function to count the frequency of words in the file. Each package is a list of strings.
# The number of packages is defined by int_number_of_packages
# Example: a text file containing 100222 lines and a desired package size of 25 would produce packages that have 4008 lines each (for example the bible.txt file included in this repo)
def map(list_plaintext_lines, int_desired_packages):
	list_packages=[]

	# sys.stdout.write("map(): Reading lines... ")
	int_number_of_lines = len(list_plaintext_lines)
	# print("done, " + str(int_number_of_lines) + " lines.")

	int_package_size = int_number_of_lines / int_desired_packages
	# print("map(): Organizing into 25 packages: " + str(int_package_size) + " lines in each package.")

	# organize the text file into 25 equal sized packages (this resembles a map() function)
	count = 0
	for i in range(0, int_number_of_lines, int_package_size):
		# print("Package " + str(count) + ": " + str(i) + " to " + str(i+int_package_size))
		list_new_package = list_plaintext_lines[i:(i + int_package_size)]
		# print("list_new_package has " + str(len(list_new_package)) + " elements.")
		list_packages.append(list_new_package)
		count=count+1

	# print("map(): list_packages has " + str(len(list_packages)) + " packages of lines.")
	# print("map(): The first element has " + str(len(list_packages[0])) + " elements/lines.")
	# print("")

	return(list_packages)
# map()

# Input: A list of packages containing lines from the input file
# Output: list_sorted_lines, a list of dictionaries that contains words on each line and their frequency
# Description: reduce() produces iterates through each input "package," which is a list of lines (strings) from the input text file
# and produces list_lines, a list containing dictionaries that describe the frequency of each word in the package
def reduce(list_line_packages):
	list_lines=[]

	# produce a list containing word counts for each package (this resembles a reduce() function)
	for i in range(0, len(list_line_packages)):
		dict_word_count = {}
		# sys.stdout.write("list_line_packages[" + str(i) + "]: ")
		for line in list_line_packages[i]:
			list_words = line.split(" ")
			for word in list_words:
				# don't count newlines as words
				if (word == "\n"): break

				try:
					dict_word_count[word] = dict_word_count[word] + 1
				except KeyError:
					dict_word_count[word] = 1
			# for word
		list_lines.append(dict_word_count)
		# for line

		# list_sorted_word_count = (sorted(dict_word_count.items(), key=lambda t: t[1], reverse=True))
		# list_sorted_lines.append(list_sorted_word_count)
	# for i

	return (list_lines)

def remove_punctuation(file):
	string_file_content = file.read()

	string_sanitized_content = string_file_content.replace('!', ' ')
	string_sanitized_content = string_sanitized_content.replace(',', ' ')
	string_sanitized_content = string_sanitized_content.replace('.', ' ')
	string_sanitized_content = string_sanitized_content.replace('"', ' ')
	string_sanitized_content = string_sanitized_content.replace('?', ' ')
	string_sanitized_content = string_sanitized_content.replace("'", " ")
	string_sanitized_content = string_sanitized_content.replace(";", " ")
	string_sanitized_content = string_sanitized_content.replace(":", " ")
	string_sanitized_content = string_sanitized_content.lower()
	string_sanitized_content = string_sanitized_content.rstrip("\r\n")
	string_sanitized_content = string_sanitized_content.rstrip()

	# get rid of characters that ascii encoding can't deal with
	string_sanitized_content = string_sanitized_content.decode("ascii", errors="ignore")

	return (string_sanitized_content)


main()