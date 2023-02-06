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

# For pretty-print parsing.
OFFICIAL_AWARDS_1315 = ['best motion picture - drama', 'best performance by an actress in a motion picture - drama', 'best performance by an actor in a motion picture - drama', 'best motion picture - comedy or musical', 'best performance by an actress in a motion picture - comedy or musical', 'best performance by an actor in a motion picture - comedy or musical', 'best animated feature film', 'best foreign language film', 'best performance by an actress in a supporting role in a motion picture', 'best performance by an actor in a supporting role in a motion picture', 'best director - motion picture', 'best screenplay - motion picture', 'best original score - motion picture', 'best original song - motion picture', 'best television series - drama', 'best performance by an actress in a television series - drama', 'best performance by an actor in a television series - drama', 'best television series - comedy or musical', 'best performance by an actress in a television series - comedy or musical', 'best performance by an actor in a television series - comedy or musical', 'best mini-series or motion picture made for television', 'best performance by an actress in a mini-series or motion picture made for television', 'best performance by an actor in a mini-series or motion picture made for television', 'best performance by an actress in a supporting role in a series, mini-series or motion picture made for television', 'best performance by an actor in a supporting role in a series, mini-series or motion picture made for television', 'cecil b. demille award']

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
    print("Host(s):", answers["hosts"])

    mined_award_list = answers["awards"]
    pretty_mined_award_list = []
    for mined_award in mined_award_list:
        pretty_mined_award_list.append(mined_award.title())
    print("\nMined Award Names:", ", ".join(pretty_mined_award_list))

    for award in OFFICIAL_AWARDS_1315:
        print("\nAward:", award.title())
        print("Presenters:", "N/A" if answers["presenters"][award] == [] else ", ".join(answers["presenters"][award]))
        print("Nominees:", "N/A" if answers["nominees"][award] == [] else ", ".join(answers["nominees"][award]))
        print("Winner:", "N/A" if answers["winners"][award] == "" else answers["winners"][award])
            