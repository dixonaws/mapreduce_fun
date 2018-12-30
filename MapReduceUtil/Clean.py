import re

def clean(str_input_dataset):
	"""
	clean()
	Given a string, clean() removes punctionation and converts all characters to lowercase
	:param str_input_dataset:
	:return:
	"""
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