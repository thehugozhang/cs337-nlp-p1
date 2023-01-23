# Python 3.11.1
"""
CS337 Intro NLP Project 1
Group 10: Hugo Zhang, Aliyah Tenner, Peter Sheldon
"""

# NLTK Configuration.
import nltk
# NLTK Downloads.
nltk.download("punkt")
nltk.download("stopwords")
nltk.download("averaged_perceptron_tagger")
# NLTK Library Imports.
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
# Other imports.
import json

stop_words = set(stopwords.words("english"))
tweet_ex_1 = {"text": "WINNER: Ben Affleck wins best film director for “Argo” #GOLDENGLOBES", "user": {"screen_name": "variety", "id": 1234567890}, "id": 1234567890, "timestamp_ms": 1234567890}

# HELPER FUNCTIONS
def pos_tag_text(text, lowercase=True, filter_stop_words=False):
    if (lowercase): text = text.lower()
    words = word_tokenize(text)
    if filter_stop_words:
        words = [word for word in words if word.casefold() not in stop_words]
    words = nltk.pos_tag(words)
    return words

def chunk_tagged_text(text_list, chunk_rule, draw_tree=False):
    chunk_parser = nltk.RegexpParser(chunk_rule)
    tree = chunk_parser.parse(text_list)
    if draw_tree: tree.draw()

    results = []
    for subtree in tree.subtrees(filter=lambda t: t.label() == 'Entity Name'):
        extracted_text = []
        for pos_tuple in subtree[0:]:
            extracted_text.append(pos_tuple[0])
        results.append(" ".join(extracted_text))
    
    return results

def main():
    """ Main entry point of the app """
    print("Hello world!")

if __name__ == "__main__":
    """ This is executed when run from the command line """
    main()