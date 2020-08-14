import nltk
from linkgrammar import Sentence, ParseOptions, Dictionary, LG_TimerExhausted


def is_grammatical_sentence(sentence_text, language_dict, verbose=False):
    parse_options = ParseOptions(verbosity=0)

    parse_options.max_null_count = 999  # max number of words in single pass
    parse_options.linkage_limit = 100  # max number of linkages to generate
    parse_options.max_parse_time = 10  # in seconds

    sent = Sentence(str(sentence_text), language_dict, parse_options)
    wrong_sentences = []

    linkages = None
    try:
        linkages = sent.parse()
    except LG_TimerExhausted:
        wrong_sentences.append(sentence_text)
        if verbose:
            print('Sentence too complex for parsing in {} seconds.'.format(parse_options.max_parse_time))
        return False

    if not linkages or len(linkages) <= 0:
        wrong_sentences.append(sentence_text)
        if verbose:
            print('Error occurred - sentence ignored.')

    null_count = sent.null_count()
    if null_count == 0:
        return True
    else:
        wrong_sentences.append(sentence_text)
        return False


def get_grammar_score(text, verbose=False):
    language_dict = Dictionary('en')

    incorrect_sentence_count = 0
    sentences = nltk.sent_tokenize(text)
    for sentence in sentences:
        if not is_grammatical_sentence(sentence, language_dict):
            incorrect_sentence_count += 1
    if verbose:
        print("num incorrect sentences: ", incorrect_sentence_count)
        print("total sentences: ", len(sentences))

    return incorrect_sentence_count, len(sentences)


if __name__ == '__main__':
    filename = "../sample_texts/tea_wafts.txt"
    with open(filename, 'r') as fh:
        text = fh.read()

    incorrect_sentence_count, total_sentence_count = get_grammar_score(text, verbose=True)
    print("Incorrect sentence fraction: ", incorrect_sentence_count / total_sentence_count)
