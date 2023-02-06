"""

Helper system containing shared system NLTK functions.

"""

__version__ = '1.0'
__author__ = 'Hugo Zhang'

# NLTK configuration.
import nltk

# NLTK downloads.
nltk.download("punkt")
nltk.download("averaged_perceptron_tagger")
nltk.download('maxent_ne_chunker')
nltk.download('words')

# NLTK library imports.
from nltk import word_tokenize, pos_tag

def pos_tag_text(text, lowercase=True, filter_stop_words=False):
    if (lowercase): text = text.lower()

    words = word_tokenize(text)

    if filter_stop_words: words = [word for word in words if word.casefold() not in stop_words]

    words = nltk.pos_tag(words)

    return words

def chunk_tagged_text(text_list, chunk_rule, draw_tree=False):
    chunk_parser = nltk.RegexpParser(chunk_rule)
    tree = chunk_parser.parse(text_list)
    if draw_tree: tree.draw()

    results = []
    for subtree in tree.subtrees(filter=lambda t: t.label() == chunk_rule.split(':')[0]):
        extracted_text = []
        for pos_tuple in subtree[0:]:
            extracted_text.append(pos_tuple[0])
        results.append(" ".join(extracted_text))
    
    return results

def pretty_print_answers(answers):
    for obj in answers:
        if type(answers[obj]) is dict:
            print("\nAward:", obj.title())
            print("Presenters:", "N/A" if answers[obj]["presenters"] == [] else ", ".join(answers[obj]["presenters"]))
            print("Nominees:", "N/A" if answers[obj]["nominees"] == [] else ", ".join(answers[obj]["nominees"]))
            print("Winner:", answers[obj]["winner"])
        else:
            print("Host(s):", answers[obj])