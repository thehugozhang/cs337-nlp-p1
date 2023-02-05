"""

Regex system where the bulk of the NLP processing occurs.

"""

__version__ = '1.0'
__author__ = 'Hugo Zhang'

# System imports.
from helpers_system import pos_tag_text, chunk_tagged_text

# Fuzzywuzzy Library.
from fuzzywuzzy import fuzz
from fuzzywuzzy import process

# Other imports.
import json
import requests
import re

def expand_hashtags(text):
    # Regex to get every hashtag.
    hashtags = re.findall(r"#(\w+)", text)
    expanded = re.sub("#[A-Za-z0-9_]+","", text)

    parsed_text = []

    # Add a space before every uppercase character and trim off the leading and trailing spaces
    for hashtag in hashtags:
        expanded = expanded + " " + re.sub(r"(\w)([A-Z])", r"\1 \2", hashtag)

    return expanded

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

def get_media(text):
    original_tweet = pos_tag_text(text, False, False)

    # Entity Name chunking RegEx.
    # Grammar rule: any number of proper singular noun followed by a verb (wins), following removing verbs.
    # Ex. Taron (NNP) Egerton (NNP) wins (VBZ).
    proper_entity_grammar = """Entity Name: {<DT>?<NNP>*<VB.>}
                                            }<VB.>+{"""
    entities = chunk_tagged_text(original_tweet, proper_entity_grammar, False)

    # Match a quotation mark and if backslash exists, gobble it.
    # Greedy inside quotes and then \1 match the same quote that was use for opening.
    greedy_quotations = re.compile(r'(["\'])((?:\\.|[^\\])*?)(\1)').findall(text)

    for quoted_entity in greedy_quotations:
        entities.append(quoted_entity[1])
    
    return entities

def get_award(text, category):
    best_match = process.extractOne(text, [category], scorer=fuzz.token_sort_ratio)
    return best_match

def award_type_check(text, award):
    if (award.lower().find("screenplay") != -1 and text.lower().find("screenplay") != -1) or (award.lower().find("screenplay") == -1 and text.lower().find("screenplay") == -1):
        if (award.lower().find("song") != -1 and text.lower().find("song") != -1) or (award.lower().find("song") == -1 and text.lower().find("song") == -1):
            if (award.lower().find("score") != -1 and text.lower().find("score") != -1) or (award.lower().find("score") == -1 and text.lower().find("score") == -1):
                if (award.lower().find("musical") != -1 and text.lower().find("musical") != -1) or (award.lower().find("musical") == -1 and text.lower().find("musical") == -1):
                    if (award.lower().find("comedy") != -1 and text.lower().find("comedy") != -1) or (award.lower().find("comedy") == -1 and text.lower().find("comedy") == -1):
                        if (award.lower().find("drama") != -1 and text.lower().find("drama") != -1) or (award.lower().find("drama") == -1 and text.lower().find("drama") == -1):
                            if (award.lower().find("television") != -1 and (text.lower().find("televison") != -1 or text.find("TV") != -1)) or (award.lower().find("television") == -1 and (text.lower().find("televison") == -1 or text.find("TV") == -1)):
                                if (award.lower().find("supporting") != -1 and text.lower().find("supporting") != -1) or (award.lower().find("supporting") == -1 and text.lower().find("supporting") == -1):
                                    if award.lower().find("actress") != -1 and text.lower().find("actress") != -1:
                                        return True
                                    elif text.lower().find("actor") != -1 and award.lower().find("actor") != -1:
                                        return True
                                    elif award.lower().find("actress") == -1 and text.lower().find("actress") == -1 and text.lower().find("actor") == -1 and award.lower().find("actor") == -1:
                                        return True
    return False