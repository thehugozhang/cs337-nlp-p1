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

stop_words = set(stopwords.words("english"))
tweet_ex_1 = {"text": "Taron Egerton wins Best Actor in a Motion Picture for his portrayal of Elton John in Rocketman. #GoldenGlobes", "user": {"screen_name": "nbc", "id": 1234567890}, "id": 1234567890, "timestamp_ms": 1234567890}

def processTweet(tweet, **kwargs):
    # Keyworded variable length of arguments for parameterization.
    ceremony = kwargs.get('ceremony', 'Golden Globes')
    host = kwargs.get('host', 'Tina Fey')
    presenter = kwargs.get('presenter', '')
    category = kwargs.get('category', 'Best Actor')
    nominees = kwargs.get('nominees', [])

    print("Tweet:", tweet)
    print("Award Ceremony:", ceremony)
    print("Host:", host)
    print("Presenter:", presenter)
    print("Award Category:", category)
    print("Nominees:", nominees)
    print("\n")

    # Tokenize tweet by words.
    tweet_words = word_tokenize(tweet)
    print("Tokenized tweet", tweet_words, "\n\n")

    # Filter out stopwords from tokenized tweet.
    filtered_tweet_words = [word for word in tweet_words if word.casefold() not in stop_words]
    print("Filtered tweet words", filtered_tweet_words, "\n\n")

    # Tag filtered words in tweet by parts of speech.
    lowercase_tweet_pos_tag = nltk.pos_tag([word.lower() for word in tweet_words])
    original_tweet_pos_tag = nltk.pos_tag(tweet_words)
    print("Tagged filtered tweet words", original_tweet_pos_tag, "\n\n")

    # Award Category chunking RegEx.
    # Grammar rule: optional determiner (DD), superlative adverb (best), any number of adjectives (JJ), noun (actor)
    # Ex. the (DD) Best (RBS) Supporting (JJ) Actress (NN)
    category_grammar = "Award Category: {<DT>?<RBS><JJ>*<NN>}"

    # Chunk tweet words for award category.
    chunk_parser = nltk.RegexpParser(category_grammar)
    tree = chunk_parser.parse(lowercase_tweet_pos_tag)
    tree.draw()

    for subtree in tree.subtrees(filter=lambda t: t.label() == 'Award Category'):
        print(subtree)

    # Entity Name chunking RegEx.
    # Grammar rule: any number of proper singular nouns
    # Ex. Taron (NNP) Egerton (NNP)
    proper_entity_grammar = "Entity Name: {<NNP>*}"

    # Chunk tweet words for proper entities.
    chunk_parser = nltk.RegexpParser(proper_entity_grammar)
    tree = chunk_parser.parse(original_tweet_pos_tag)
    tree.draw()

    for subtree in tree.subtrees(filter=lambda t: t.label() == 'Entity Name'):
        print(subtree)

def main():
    """ Main entry point of the app """

    processTweet(tweet_ex_1["text"], category='Best Actor in a Motion Picture - Musical or Comedy', nominees=['Taron Egerton', 'Daniel Craig', 'Roman Griffin Davis', 'Leonardo DiCaprio', 'Eddie Murphy'])

if __name__ == "__main__":
    """ This is executed when run from the command line """
    main()