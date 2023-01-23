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
    if category in category_chunks and len(entities):
    # if category in category_chunks:
        print(category_chunks, entities)

    # naive tallying:
    if category in category_chunks:
        return entities
    else:
        return []

def main():
    """ Main entry point of the app """

    process_tweet(tweet_ex_1["text"], category=chunked_category[0], nominees=[
            "kathryn bigelow",
            "ang lee",
            "steven spielberg",
            "quentin tarantino"
         ])

    f = open('gg2013.json')
    data = json.load(f)

    lim = 0
    counts = dict()

    chunked_category = chunk_tagged_text(pos_tag_text('best director - motion picture'), "Award Category: {<RBS|JJS><NN>*}", True)
    print(chunked_category[0])

    for tweet in data:

        # Process individual tweet.
        result = process_tweet(tweet["text"], category=chunked_category[0], nominees=[
            "kathryn bigelow",
            "ang lee",
            "steven spielberg",
            "quentin tarantino"
         ])

        for entity in result:
            counts[entity] = counts.get(entity, 0) + 1

        lim = lim + 1
        if lim % 1000 == 0: print(lim)
        if lim == 100000: break

    print("Dictionary after the increment of key : " + str(counts))

    f.close()

if __name__ == "__main__":
    """ This is executed when run from the command line """
    main()