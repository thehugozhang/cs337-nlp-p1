# NLTK Configuration.
import nltk
# NLTK Downloads.
nltk.download("punkt")
nltk.download("stopwords")
nltk.download("averaged_perceptron_tagger")
# NLTK Library Imports.
from nltk import word_tokenize, pos_tag
from nltk.corpus import stopwords
# Fuzzywuzzy Library.
from fuzzywuzzy import fuzz
from fuzzywuzzy import process
# Other imports.
import json
import requests


nltk.download('averaged_perceptron_tagger')
nltk.download('maxent_ne_chunker')
nltk.download('words')

award_list = ['best motion picture - drama', 'best motion picture - musical or comedy', 'best performance by an actress in a motion picture - drama', 'best performance by an actor in a motion picture - drama', 'best performance by an actress in a motion picture - musical or comedy', 'best performance by an actor in a motion picture - musical or comedy', 'best performance by an actress in a supporting role in any motion picture', 'best performance by an actor in a supporting role in any motion picture', 'best director - motion picture', 'best screenplay - motion picture', 'best motion picture - animated', 'best motion picture - foreign language', 'best original score - motion picture', 'best original song - motion picture', 'best television series - drama', 'best television series - musical or comedy', 'best television limited series or motion picture made for television', 'best performance by an actress in a limited series or a motion picture made for television', 'best performance by an actor in a limited series or a motion picture made for television', 'best performance by an actress in a television series - drama', 'best performance by an actor in a television series - drama', 'best performance by an actress in a television series - musical or comedy', 'best performance by an actor in a television series - musical or comedy', 'best performance by an actress in a supporting role in a series, limited series or motion picture made for television', 'best performance by an actor in a supporting role in a series, limited series or motion picture made for television', 'cecil b. demille award']

tweet = "Kerry Washington is totally showing J.Lo how you wear nude and sequins. Time for a new queen... #goldenglobes"
tweet1 = "Brad Pitt wins the Golden Globe for Best Performance #GoldenGlobes #Winners"
tweet2 = "WINNER: Ben Affleck wins best film director motion picture for “Argo” #GOLDENGLOBES"
tweet3 = "Jennifer Lawrence wins Best actress in a motion picture #GoldenGlobes ('best director - motion picture', 52) ['Jennifer Lawrence']"
tweet4 = "RT @nbc: Christoph Waltz wins the award for Best Supporting Actor in a Motion Picture over Joey Billycoochiegobbler for his role in Django Unchained! #GoldenGlobes"
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

def get_actors(text):
    url = "https://text-analysis12.p.rapidapi.com/ner/api/v1.1"

    payload = {
        "language": "english",
        "text": text,
    }
    headers = {
        "content-type": "application/json",
        "X-RapidAPI-Key": "dce9755f64mshe61076df41050e4p1e1571jsn25bf332ab4e6",
        "X-RapidAPI-Host": "text-analysis12.p.rapidapi.com"
    }

    response = requests.request("POST", url, json=payload, headers=headers)
    data = response.json()
    names = []
    for entity in data['ner']:
        if entity['label'] == 'PERSON' and entity['entity'] != "Best Actress":
            names.append(entity['entity'])
    return names

# award_list
def get_award(text, category):
    best_match = process.extractOne(text, [category], scorer=fuzz.token_sort_ratio)
    # print(best_match)
    return best_match

# winner = get_actors(tweet4)[0]
# award = get_award(tweet4, "best performance by an actor in a supporting role in a motion picture")

# print(f'{winner} wins the Golden Globe for {award}')

def award_type_check(text, award):
    if award.lower().find("actress") != -1 and text.lower().find("actress") != -1:
        return True
    elif text.lower().find("actor") != -1 and award.lower().find("actor") != -1:
        return True
    elif award.lower().find("actress") == -1 and text.lower().find("actress") == -1 and text.lower().find("actor") == -1 and award.lower().find("actor") == -1:
        return True
    else:
        return False