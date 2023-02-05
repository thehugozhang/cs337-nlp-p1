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
from collections import Counter
import re
from regex_system import get_actors, get_media, get_award, award_type_check, expand_hashtags
from type_system import getAwardType, isMovie, isShow

stop_words = set(stopwords.words("english"))
tweet_ex_1 = {"text": "WINNER: Ben Affleck wins best film director for “Argo” #GOLDENGLOBES", "user": {"screen_name": "variety", "id": 1234567890}, "id": 1234567890, "timestamp_ms": 1234567890}

awards_list_1315 = ['cecil b. demille award', 'best motion picture - drama', 'best performance by an actress in a motion picture - drama', 'best performance by an actor in a motion picture - drama', 'best motion picture - comedy or musical', 'best performance by an actress in a motion picture - comedy or musical', 'best performance by an actor in a motion picture - comedy or musical', 'best animated feature film', 'best foreign language film', 'best performance by an actress in a supporting role in a motion picture', 'best performance by an actor in a supporting role in a motion picture', 'best director - motion picture', 'best screenplay - motion picture', 'best original score - motion picture', 'best original song - motion picture', 'best television series - drama', 'best performance by an actress in a television series - drama', 'best performance by an actor in a television series - drama', 'best television series - comedy or musical', 'best performance by an actress in a television series - comedy or musical', 'best performance by an actor in a television series - comedy or musical', 'best mini-series or motion picture made for television', 'best performance by an actress in a mini-series or motion picture made for television', 'best performance by an actor in a mini-series or motion picture made for television', 'best performance by an actress in a supporting role in a series, mini-series or motion picture made for television', 'best performance by an actor in a supporting role in a series, mini-series or motion picture made for television']


answer_json = {
    "host": "",
    "cecil b. demille award": {
        "presenters": [],
        "nominees": [],
        "winner": "",
    },
    "best motion picture - drama": {
        "presenters": [],
        "nominees": [],
        "winner": "",
    },
        "best performance by an actor in a motion picture - drama": {
        "presenters": [],
        "nominees": [],
        "winner": "",
    },
    "best performance by an actress in a motion picture - drama": {
        "presenters": [],
        "nominees": [],
        "winner": "",
    },
    "best motion picture - comedy or musical": {
        "presenters": [],
        "nominees": [],
        "winner": "",
    },
    "best performance by an actress in a motion picture - comedy or musical": {
        "presenters": [],
        "nominees": [],
        "winner": "",
    },
    "best performance by an actor in a motion picture - comedy or musical": {
        "presenters": [],
        "nominees": [],
        "winner": "",
    },
    "best animated feature film": {
        "presenters": [],
        "nominees": [],
        "winner": "",
    },
    "best foreign language film": {
        "presenters": [],
        "nominees": [],
        "winner": "",
    },
    "best performance by an actress in a supporting role in a motion picture": {
        "presenters": [],
        "nominees": [],
        "winner": "",
    },
    "best performance by an actor in a supporting role in a motion picture": {
        "presenters": [],
        "nominees": [],
        "winner": "",
    },
    "best director - motion picture": {
        "presenters": [],
        "nominees": [],
        "winner": "",
    },
    "best screenplay - motion picture": {
        "presenters": [],
        "nominees": [],
        "winner": "",
    },
    "best original score - motion picture": {
        "presenters": [],
        "nominees": [],
        "winner": "",
    },
    "best original song - motion picture": {
        "presenters": [],
        "nominees": [],
        "winner": "",
    },
    "best television series - drama": {
        "presenters": [],
        "nominees": [],
        "winner": "",
    },
    "best performance by an actress in a television series - drama": {
        "presenters": [],
        "nominees": [],
        "winner": "",
    },
    "best performance by an actor in a television series - drama": {
        "presenters": [],
        "nominees": [],
        "winner": "",
    },
    "best television series - comedy or musical": {
        "presenters": [],
        "nominees": [],
        "winner": "",
    },
    "best performance by an actress in a television series - comedy or musical": {
        "presenters": [],
        "nominees": [],
        "winner": "",
    },
    "best performance by an actor in a television series - comedy or musical": {
        "presenters": [],
        "nominees": [],
        "winner": "",
    },
    "best mini-series or motion picture made for television": {
        "presenters": [],
        "nominees": [],
        "winner": "",
    },
    "best performance by an actress in a mini-series or motion picture made for television": {
        "presenters": [],
        "nominees": [],
        "winner": "",
    },
    "best performance by an actor in a mini-series or motion picture made for television": {
        "presenters": [],
        "nominees": [],
        "winner": "",
    },
    "best performance by an actress in a supporting role in a series, mini-series or motion picture made for television": {
        "presenters": [],
        "nominees": [],
        "winner": "",
    },
    "best performance by an actor in a supporting role in a series, mini-series or motion picture made for television": {
        "presenters": [],
        "nominees": [],
        "winner": "",
    },
}

# cecil b. demille award

other_awards = [
    "best motion picture - drama",
    "best motion picture - comedy or musical",
    "best animated feature film",
    "best foreign language film",
    "best screenplay - motion picture",
    "best original score - motion picture",
    "best original song - motion picture",
    "best television series - drama",
    "best television series - comedy or musical",
    "best mini-series or motion picture made for television",
]

people_awards = [    "best performance by an actress in a motion picture - drama",    "best performance by an actor in a motion picture - drama",    "best performance by an actress in a motion picture - comedy or musical",    "best performance by an actor in a motion picture - comedy or musical",    "best performance by an actress in a supporting role in a motion picture",    "best performance by an actor in a supporting role in a motion picture",    "best director - motion picture",    "best performance by an actress in a television series - drama",    "best performance by an actor in a television series - drama",    "best performance by an actress in a television series - comedy or musical",    "best performance by an actor in a television series - comedy or musical",    "best performance by an actress in a mini-series or motion picture made for television",    "best performance by an actor in a mini-series or motion picture made for television",    "best performance by an actress in a supporting role in a series, mini-series or motion picture made for television",    "best performance by an actor in a supporting role in a series, mini-series or motion picture made for television"]

test_award = ["best television series - comedy or musical"]





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

def tally_entities():
    pass

# Process individual tweet.
def process_tweet(tweet, **kwargs):
    # Keyworded variable length of arguments for parameterization.
    ceremony = kwargs.get('ceremony', 'Golden Globes')
    host = kwargs.get('host', 'Tina Fey')
    presenter = kwargs.get('presenter', '')
    category = kwargs.get('category', 'Best Actor')
    nominees = kwargs.get('nominees', [])

    original_tweet = pos_tag_text(tweet, False, False)
    lowercase_original_tweet = pos_tag_text(tweet, True, False)

    # Award Category chunking RegEx.
    # Grammar rule: optional determiner (DD), superlative adverb/adjective (best), any number of adjectives (JJ), noun (actor)
    # Ex. the (DD) Best (RBS) Supporting (JJ) Actress (NN)
    category_grammar = "Award Category: {<RBS|JJS><NN>*}"
    category_chunks = chunk_tagged_text(lowercase_original_tweet, category_grammar, False)

    # Entity Name chunking RegEx.
    # Grammar rule: any number of proper singular noun followed by a verb (wins), following removing verbs.
    # Ex. Taron (NNP) Egerton (NNP) wins (VBZ).
    proper_entity_grammar = """Entity Name: {<NNP>*<VB.>}
                                            }<VB.>+{"""
    entities = chunk_tagged_text(original_tweet, proper_entity_grammar, False)

    # category_chunks = ["best director"]
    # if category in category_chunks:
    # if category in category_chunks and len(entities):
    # if len(category_chunks) and len(entities):
        # print(category_chunks, entities)

    # naive tallying:
    best_match = process.extractOne(tweet, [category], scorer=fuzz.token_sort_ratio)

    # if category in category_chunks:

    if best_match[1] > 50:
        print(tweet, best_match, entities)
        return entities
    else:
        return []

def main():
    """ Main entry point of the app """


    w = open('gg2013-winner.json')
    data = json.load(w)

    h = open('gg2013-host.json')
    host_data = json.load(h)
    host_tally = dict()

    p = open('gg2013-presenter.json')
    presenter_data = json.load(p)
    presenter_tally = dict()

    n = open('gg2013-nominee.json')
    nominee_data = json.load(n)

    lim = 0
    for tweet in host_data:
        tweet_text = tweet["text"]
        result = get_actors(tweet_text)
        for entity in result:
            host_tally[entity] = host_tally.get(entity, 0) + 1
        lim = lim + 1
        if lim == 10: break
    
    c = Counter(host_tally)
    top_two_results = c.most_common(2)
    print("Dictionary after the increment of key : " + str(host_tally))
    print("Top five hosts:", top_two_results)
    answer_json["host"] = [top_two_results[0][0], top_two_results[1][0]]

    lim = 0
    for award_category in awards_list_1315:
        for tweet in presenter_data:
            tweet_text = tweet["text"]

            if award_type_check(tweet_text, award_category):
                score = get_award(tweet_text, award_category)

                if score[1] > 50:
                    print(score[1], tweet["text"], result)
                    result = get_actors(tweet_text)
                    for entity in result:
                        presenter_tally[entity] = presenter_tally.get(entity, 0) + 1

            lim = lim + 1
            if lim % 1000 == 0: print(award_category, lim)
        c = Counter(presenter_tally)
        top_five_results = c.most_common(5)
        print("Dictionary after the increment of key : " + str(presenter_tally))
        print("Top five presenters:", top_five_results)
        if top_five_results != []:
            answer_json[award_category]["presenters"] = top_five_results[0][0]
        presenter_tally.clear()


    lim = 0
    counts = dict()

    chunked_category = chunk_tagged_text(pos_tag_text('best director - motion picture'), "Award Category: {<RBS|JJS><NN>*}", False)
    print(chunked_category[0])

    process_tweet(tweet_ex_1["text"], category=chunked_category[0], nominees=[
            "kathryn bigelow",
            "ang lee",
            "steven spielberg",
            "quentin tarantino"
         ])
    print("hey", len(people_awards))
    for award_category in awards_list_1315:
        for tweet in data:
            tweet_text = tweet["text"]

            if award_type_check(tweet_text, award_category):
                score = get_award(tweet_text, award_category)

                if score[1] > 50:
                    if getAwardType(award_category) == "Person":
                        result = get_actors(tweet_text)
                    else:
                        result = get_media(tweet_text)
                    for entity in result:
                        counts[entity] = counts.get(entity, 0) + 1

                    # print(score[1], tweet["text"], result)

            lim = lim + 1
            if lim % 1000 == 0: print(award_category, lim)
            # if lim % 1000 == 0: break
        lim = 0
        # print("Dictionary after the increment of key : " + str(counts))
        c = Counter(counts)
        top_three_results = c.most_common(3)
        print(award_category, top_three_results)
        if top_three_results != []:
            answer_json[award_category]["winner"] = top_three_results[0][0]
        counts.clear()
    with open('answers.json', 'w', encoding='utf-8') as f:
        json.dump(answer_json, f, ensure_ascii=False, indent=4)

    # print(answer_json)

    w.close()
    h.close()
    p.close()

if __name__ == "__main__":
    """ This is executed when run from the command line """
    main()