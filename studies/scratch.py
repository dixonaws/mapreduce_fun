import collections

def remove_punctuation(lst_lines):
	lst_sanitized_lines=[]

	for line in lst_lines:
		str_sanitized_line = line.decode("ascii", errors="ignore")
		str_sanitized_line=line.replace('!', ' ')
		str_sanitized_line=line.lower()
		str_sanitized_line=line.rstrip("\r\n")
		str_sanitized_line=line.replace(",", "")
		str_sanitized_line = line.replace(".", "")

		lst_sanitized_lines.append(str_sanitized_line)

	# string_sanitized_content=string_file_content.replace('!', ' ')
	# string_sanitized_content=string_sanitized_content.replace(',', ' ')
	# string_sanitized_content = string_sanitized_content.replace('.', ' ')
	# string_sanitized_content = string_sanitized_content.replace('"', ' ')
	# string_sanitized_content = string_sanitized_content.replace('?', ' ')
	# string_sanitized_content = string_sanitized_content.replace("'", " ")
	# string_sanitized_content = string_sanitized_content.replace(";", " ")
	# string_sanitized_content = string_sanitized_content.replace(":", " ")
	# string_sanitized_content=string_sanitized_content.lower()
	# string_sanitized_content=string_sanitized_content.rstrip("\n\r")
	# string_sanitized_content = string_sanitized_content.rstrip()
	#
	# string_sanitized_content=string_sanitized_content.decode("ascii", errors="ignore")

	return(lst_sanitized_lines)

file=open("tale_of_two_cities.txt", "r")
lst_lines=file.readlines()

sanitized_content=remove_punctuation(lst_lines)

file.close()

print("sanitized string: ******")
print(sanitized_content)