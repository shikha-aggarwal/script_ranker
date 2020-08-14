import enchant
import re


def spell_check(text):

	d = enchant.Dict("en_US")
	words = re.findall(r'\w+', text)
	misspelt_words = {}
	
	for word in words:
		if not d.check(word) and word[0].islower():
			misspelt_words[word] = d.suggest(word)

	return len(misspelt_words), len(words), misspelt_words


if __name__ == '__main__' :
	
	filename = "../sample_texts/tea_wafts.txt"
	with open(filename, 'r') as fh:
		text = fh.read()

	num_misspelt, total_words, misspelt_words = spell_check(text)
	print("Incorrectly spelled words: ", num_misspelt, " out of ", total_words, " words.")
	print("Suggested spellings: ")
	for key in misspelt_words:
		print(key, " --> ",  misspelt_words[key])