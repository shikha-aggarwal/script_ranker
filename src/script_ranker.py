#!/usr/bin/python

import spellings
import grammar

input_filename = "../sample_texts/tea_wafts.txt"
with open(input_filename, 'r') as fh:
	text = fh.read()

print("Performing spell check")
num_misspellings, total_word_count, misspelt_list = spell_check(text)

print("Now Grammar check")
incorrect_sentence_count, total_sentence_count = get_grammar_score(text)

#TODO(shikha): Need to implement this
print("Ahem ... coherence")
coherenceScore = 3

# Some statistics
avg_sentence_length = total_word_count/total_sentence_count

