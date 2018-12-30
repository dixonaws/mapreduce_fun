from MapReduceUtil import Clean

str_input_filename= "datasets/bible.txt"
str_output_filename="datasets/clean_bible.txt"

with open(str_input_filename, "r") as infile:
	str_content=Clean.clean(infile.read())

lst_words=str_content.split(" ")

# print(lst_words)

str_output = ""
for str_word in lst_words:
	str_output += str_word + ","

with open(str_output_filename, "w") as outfile:
	outfile.write(str_output)
