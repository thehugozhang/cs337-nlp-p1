"""

Binning system for pre-ceremony setup.

"""

__version__ = '1.0'
__author__ = 'Hugo Zhang'

# System imports.
from helpers_system import pos_tag_text, chunk_tagged_text

# Other imports.
import json
import re

# Process individual tweets.
def bin_tweet(tweet):
    bins = [None, None, None, None, None, None]

    full_tweet = tweet
    tweet = tweet["text"]

    # Skip retweets.
    if tweet.find("RT") != -1:
        return bins

    # Tag parts of speech.
    lowercase_original_tweet = pos_tag_text(tweet, True, False)

    # Award Category chunking RegEx.
    # Grammar rule: optional determiner (DD), superlative adverb/adjective (best), any number of adjectives (JJ), noun (actor)
    # Ex. the (DD) Best (RBS) Supporting (JJ) Actress (NN)
    category_grammar = "Award Category: {<RBS|JJS>}"
    category_chunks = chunk_tagged_text(lowercase_original_tweet, category_grammar, False)

    # Bin any tweets with superlatives ("best", "biggest", "most") into our winner dataset.
    if len(category_chunks):
        bins[1] = full_tweet

    # Bin any tweets with some form of "host" into our host dataset.
    host_regex = re.compile(r'[Hh]ost')
    if host_regex.search(tweet):
        bins[2] = full_tweet

    # Bin any tweets with some form of "present" into our presenter dataset.
    presenter_regex = re.compile(r'[Pp]resent')
    if presenter_regex.search(tweet):
        bins[3] = full_tweet

    # Bin any tweets with some form of "nomin" into our nominee dataset.
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

    # Write to JSON files.
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