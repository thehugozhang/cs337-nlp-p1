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
# Fuzzywuzzy Imports.
from fuzzywuzzy import fuzz
from fuzzywuzzy import process
# Other imports.
import json
import re

# HELPER FUNCTIONS
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

# Process individual tweet.
def bin_tweet(tweet):
    bins = [None, None, None, None, None]

    full_tweet = tweet
    tweet = tweet["text"]

    # Skip retweets.
    if tweet.find("RT") != -1:
        return bins

    # original_tweet = pos_tag_text(tweet, False, False)
    lowercase_original_tweet = pos_tag_text(tweet, True, False)

    # Award Category chunking RegEx.
    # Grammar rule: optional determiner (DD), superlative adverb/adjective (best), any number of adjectives (JJ), noun (actor)
    # Ex. the (DD) Best (RBS) Supporting (JJ) Actress (NN)
    category_grammar = "Award Category: {<RBS|JJS>}"
    category_chunks = chunk_tagged_text(lowercase_original_tweet, category_grammar, False)

    if len(category_chunks):
        bins[1] = full_tweet

    host_regex = re.compile(r'[Hh]ost')
    if host_regex.search(tweet):
        bins[2] = full_tweet

    presenter_regex = re.compile(r'[Pp]resent')
    if presenter_regex.search(tweet):
        bins[3] = full_tweet

    nominee_regex = re.compile(r'[Nn]omin')
    if nominee_regex.search(tweet):
        bins[4] = full_tweet
    
    return bins
        
    
def main():
    """ Main entry point of the app """
    parsed_award_data = []
    parsed_winner_data = []
    parsed_host_data = []
    parsed_presenter_data = []
    parsed_nominee_data = []

    f = open('gg2013.json')
    data = json.load(f)

    lim = 0

    for tweet in data:
        # Bin individual tweets into seperate JSONs for faster processing.
        bins = bin_tweet(tweet)

        if bins[0] is not None:
            parsed_award_data.append(bins[0])
        if bins[1] is not None:
            parsed_winner_data.append(bins[1])
        if bins[2] is not None:
            parsed_host_data.append(bins[2])
        if bins[3] is not None:
            parsed_presenter_data.append(bins[3])
        if bins[4] is not None:
            parsed_nominee_data.append(bins[4])
        
        lim = lim + 1
        if lim % 1000 == 0: print(lim)

    with open('gg2013-winner.json', 'w', encoding='utf-8') as f:
        json.dump(parsed_winner_data, f, ensure_ascii=False)
    with open('gg2013-host.json', 'w', encoding='utf-8') as f:
        json.dump(parsed_host_data, f, ensure_ascii=False)
    with open('gg2013-presenter.json', 'w', encoding='utf-8') as f:
        json.dump(parsed_presenter_data, f, ensure_ascii=False)
    with open('gg2013-nominee.json', 'w', encoding='utf-8') as f:
        json.dump(parsed_nominee_data, f, ensure_ascii=False)

    f.close()

if __name__ == "__main__":
    """ This is executed when run from the command line """
    main()