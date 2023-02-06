"""

CS337 Intro NLP Project 1 - Group 10

"""

__version__ = '1.0'
__author__ = 'Hugo Zhang'

# System imports.
from helpers_system import pos_tag_text, chunk_tagged_text, pretty_print_answers
from regex_system import get_actors, get_media, get_award, award_type_check, expand_hashtags
from type_system import getAwardType, isMovie, isShow

# Other imports.
import json
from collections import Counter
import timeit
import re

OFFICIAL_AWARDS_1315 = ['best motion picture - drama', 'best performance by an actress in a motion picture - drama', 'best performance by an actor in a motion picture - drama', 'best motion picture - comedy or musical', 'best performance by an actress in a motion picture - comedy or musical', 'best performance by an actor in a motion picture - comedy or musical', 'best animated feature film', 'best foreign language film', 'best performance by an actress in a supporting role in a motion picture', 'best performance by an actor in a supporting role in a motion picture', 'best director - motion picture', 'best screenplay - motion picture', 'best original score - motion picture', 'best original song - motion picture', 'best television series - drama', 'best performance by an actress in a television series - drama', 'best performance by an actor in a television series - drama', 'best television series - comedy or musical', 'best performance by an actress in a television series - comedy or musical', 'best performance by an actor in a television series - comedy or musical', 'best mini-series or motion picture made for television', 'best performance by an actress in a mini-series or motion picture made for television', 'best performance by an actor in a mini-series or motion picture made for television', 'best performance by an actress in a supporting role in a series, mini-series or motion picture made for television', 'best performance by an actor in a supporting role in a series, mini-series or motion picture made for television', 'cecil b. demille award']

answer_json = {
    "hosts": [],
    "awards": [],
    "nominees": {
        "best motion picture - drama": [],
        "best performance by an actor in a motion picture - drama": [],
        "best performance by an actress in a motion picture - drama": [],
        "best motion picture - comedy or musical": [],
        "best performance by an actress in a motion picture - comedy or musical": [],
        "best performance by an actor in a motion picture - comedy or musical": [],
        "best animated feature film": [],
        "best foreign language film": [],
        "best performance by an actress in a supporting role in a motion picture": [],
        "best performance by an actor in a supporting role in a motion picture": [],
        "best director - motion picture": [],
        "best screenplay - motion picture": [],
        "best original score - motion picture": [],
        "best original song - motion picture": [],
        "best television series - drama": [],
        "best performance by an actress in a television series - drama": [],
        "best performance by an actor in a television series - drama": [],
        "best television series - comedy or musical": [],
        "best performance by an actress in a television series - comedy or musical": [],
        "best performance by an actor in a television series - comedy or musical": [],
        "best mini-series or motion picture made for television": [],
        "best performance by an actress in a mini-series or motion picture made for television": [],
        "best performance by an actor in a mini-series or motion picture made for television": [],
        "best performance by an actress in a supporting role in a series, mini-series or motion picture made for television": [],
        "best performance by an actor in a supporting role in a series, mini-series or motion picture made for television": [],
        "cecil b. demille award": [],
    },
    "presenters":  {
        "best motion picture - drama": [],
        "best performance by an actor in a motion picture - drama": [],
        "best performance by an actress in a motion picture - drama": [],
        "best motion picture - comedy or musical": [],
        "best performance by an actress in a motion picture - comedy or musical": [],
        "best performance by an actor in a motion picture - comedy or musical": [],
        "best animated feature film": [],
        "best foreign language film": [],
        "best performance by an actress in a supporting role in a motion picture": [],
        "best performance by an actor in a supporting role in a motion picture": [],
        "best director - motion picture": [],
        "best screenplay - motion picture": [],
        "best original score - motion picture": [],
        "best original song - motion picture": [],
        "best television series - drama": [],
        "best performance by an actress in a television series - drama": [],
        "best performance by an actor in a television series - drama": [],
        "best television series - comedy or musical": [],
        "best performance by an actress in a television series - comedy or musical": [],
        "best performance by an actor in a television series - comedy or musical": [],
        "best mini-series or motion picture made for television": [],
        "best performance by an actress in a mini-series or motion picture made for television": [],
        "best performance by an actor in a mini-series or motion picture made for television": [],
        "best performance by an actress in a supporting role in a series, mini-series or motion picture made for television": [],
        "best performance by an actor in a supporting role in a series, mini-series or motion picture made for television": [],
        "cecil b. demille award": [],
    },
    "winners": {
        "best motion picture - drama": "",
        "best performance by an actor in a motion picture - drama": "",
        "best performance by an actress in a motion picture - drama": "",
        "best motion picture - comedy or musical": "",
        "best performance by an actress in a motion picture - comedy or musical": "",
        "best performance by an actor in a motion picture - comedy or musical": "",
        "best animated feature film": "",
        "best foreign language film": "",
        "best performance by an actress in a supporting role in a motion picture": "",
        "best performance by an actor in a supporting role in a motion picture": "",
        "best director - motion picture": "",
        "best screenplay - motion picture": "",
        "best original score - motion picture": "",
        "best original song - motion picture": "",
        "best television series - drama": "",
        "best performance by an actress in a television series - drama": "",
        "best performance by an actor in a television series - drama": "",
        "best television series - comedy or musical": "",
        "best performance by an actress in a television series - comedy or musical": "",
        "best performance by an actor in a television series - comedy or musical": "",
        "best mini-series or motion picture made for television": "",
        "best performance by an actress in a mini-series or motion picture made for television": "",
        "best performance by an actor in a mini-series or motion picture made for television": "",
        "best performance by an actress in a supporting role in a series, mini-series or motion picture made for television": "",
        "best performance by an actor in a supporting role in a series, mini-series or motion picture made for television": "",
        "cecil b. demille award": "",
    },
}

def main():
    """ Main entry point of the app """

    # Starting total runtime timer.
    start = timeit.default_timer()

    h = open('gg2013-host.json')
    host_data = json.load(h)
    host_tally = dict()

    w = open('gg2013-winner.json')
    winner_data = json.load(w)
    winner_tally = dict()
    award_name_tally = dict()
    # Additional goals using winner data.
    best_dressed_tally = dict()
    best_acceptance_speech_tally = dict()
    best_celebrity_crush_tally = dict()

    p = open('gg2013-presenter.json')
    presenter_data = json.load(p)
    presenter_tally = dict()

    n = open('gg2013-nominee.json')
    nominee_data = json.load(n)
    nominee_tally = dict()
    
    lim = 0

    # Determine hosts.
    for tweet in host_data:
        tweet_text = tweet["text"]
        result = get_actors(tweet_text)
        for entity in result:
            host_tally[entity] = host_tally.get(entity, 0) + 1
        lim = lim + 1
        print("Determining hosts.")
        # Truncate function earlier because it's already conclusive.
        if lim == 10: break
    
    c = Counter(host_tally)
    top_two_results = c.most_common(2)
    # Uncomment this line if you want to view the entire tallied dictionary of phrases.
    # print("Dictionary after the increment of key : " + str(host_tally))
    print("Top two hosts:", top_two_results)
    answer_json["host"] = [top_two_results[0][0], top_two_results[1][0]]

    lim = 0

    # Determine award names.
    keywords = ["motion picture", "musical", "comedy", "drama"]
    for tweet in winner_data:
        tweet_text = tweet["text"]

        # Skip awards without "best" to speed up iterations.
        if tweet_text.lower().find("best") == -1:
            continue
        
        # Tag parts of speech.
        lowercase_original_tweet = pos_tag_text(tweet_text, True, False)

        # Award Category chunking RegEx.
        # Grammar rule: optional determiner (DD), superlative adverb/adjective (best), any number of adjectives (JJ), noun (actor)
        # Ex. the (DD) Best (RBS) Supporting (JJ) Actress (NN)
        category_grammar = "Award Category: {<RBS|JJS><JJ|NN>?<NN.*>*?<IN>?<DT>?<JJ.*>*<NN>}"
        category_chunks = chunk_tagged_text(lowercase_original_tweet, category_grammar, False)
        
        for identified_award in category_chunks:
            full_award = identified_award
            for keyword in keywords:
                # Key mentioned in tweet but not already mentioned in award name, so must be a category.
                if tweet_text.lower().find(keyword) != -1 and full_award.lower().find(keyword) == -1:
                    full_award = full_award + " - " + keyword
            award_name_tally[full_award] = award_name_tally.get(full_award, 0) + 1

        lim = lim + 1
        if lim % 1000 == 0: print("Determining award names. Another", lim, "tweets processed.")

    c = Counter(award_name_tally)
    top_award_results = c.most_common(26)
    # Uncomment this line if you want to view the entire tallied dictionary of phrases.
    # print("Dictionary after the increment of key : " + str(award_name_tally))
    print("Top 26 mined award names:", top_award_results)
    answer_json["awards"] = [award[0] for award in top_award_results]

    lim = 0

    # Determine winners from hardcoded award names to 
    # prevent cascading errors from award name mining.
    for award_category in OFFICIAL_AWARDS_1315:
        for tweet in winner_data:
            tweet_text = tweet["text"]

            if award_type_check(tweet_text, award_category):
                score = get_award(tweet_text, award_category)

                if score[1] > 50:
                    if getAwardType(award_category) == "Person":
                        result = get_actors(tweet_text)
                    else:
                        result = get_media(tweet_text)
                    for entity in result:
                        winner_tally[entity] = winner_tally.get(entity, 0) + 1

            lim = lim + 1
            if lim % 1000 == 0: print("Determining winners. Another", lim, "tweets processed.")
        lim = 0
        c = Counter(winner_tally)
        top_three_results = c.most_common(3)
        # Uncomment this line if you want to view the entire tallied dictionary of phrases.
        # print("Dictionary after the increment of key : " + str(winner_tally))
        print('Top 3 winners for "' + award_category + '":', top_three_results)
        if top_three_results != []:
            answer_json["winners"][award_category] = top_three_results[0][0]
        winner_tally.clear()

    lim = 0

    # Determine presenters from award names.
    for award_category in OFFICIAL_AWARDS_1315:
        for tweet in presenter_data:
            tweet_text = tweet["text"]

            if award_type_check(tweet_text, award_category):
                score = get_award(tweet_text, award_category)

                if score[1] > 50:
                    result = get_actors(tweet_text)
                    for entity in result:
                        presenter_tally[entity] = presenter_tally.get(entity, 0) + 1

            lim = lim + 1
            if lim % 1000 == 0: print("Determining presenters. Another", lim, "tweets processed.")
        c = Counter(presenter_tally)
        top_five_results = c.most_common(5)
        # Uncomment this line if you want to view the entire tallied dictionary of phrases.
        # print("Dictionary after the increment of key : " + str(presenter_tally))
        # Uncomment this line if you want to view the top tallied phrases.
        # print("Top Five Presenters (if any):", top_five_results)
        if top_five_results != []:
            answer_json["presenters"][award_category] = [top_five_results[0][0]]
        presenter_tally.clear()

    lim = 0

    # Determine nominees from award names.
    for award_category in OFFICIAL_AWARDS_1315:
        for tweet in nominee_data:
            tweet_text = tweet["text"]

            if award_type_check(tweet_text, award_category):
                score = get_award(tweet_text, award_category)

                if score[1] > 50:
                    if getAwardType(award_category) == "Person":
                        result = get_actors(tweet_text)
                    else:
                        result = get_media(tweet_text)
                    for entity in result:
                        nominee_tally[entity] = nominee_tally.get(entity, 0) + 1

            lim = lim + 1
            if lim % 1000 == 0: print("Determining nominees. Another", lim, "tweets processed.")
        c = Counter(nominee_tally)
        top_five_results = c.most_common(5)
        # Uncomment this line if you want to view the top tallied phrases.
        # print("Top 5 Nominees (if any):", top_five_results)
        nominees = []
        if top_five_results != []:
            for nominee in top_five_results:
                nominees.append(nominee[0])
        # Uncomment this line if you want to view the entire tallied dictionary of phrases.
        # print("Dictionary after the increment of key : " + str(nominee_tally))
        answer_json["nominees"][award_category] = nominees
        nominee_tally.clear()

    lim = 0

    # Determine additional goals including best dressed, best acceptance speech, and best celebrity crush.
    best_dressed_regex = re.compile(r'[Bb]est [Dd]ress')
    best_acceptance_speech_regex = re.compile(r'(?:acceptance)? [Ss]peech')
    best_celebrity_crush_regex = re.compile(r'[Cc]rush')

    for tweet in winner_data:
        if lim >= 2500:
            tweet_text = tweet["text"]

            if best_dressed_regex.search(tweet_text):
                result = get_actors(tweet_text)
                for entity in result:
                    best_dressed_tally[entity] = best_dressed_tally.get(entity, 0) + 1

            if best_acceptance_speech_regex.search(tweet_text):
                result = get_actors(tweet_text)
                for entity in result:
                    best_acceptance_speech_tally[entity] = best_acceptance_speech_tally.get(entity, 0) + 1

            if best_celebrity_crush_regex.search(tweet_text):
                result = get_actors(tweet_text)
                for entity in result:
                    best_celebrity_crush_tally[entity] = best_celebrity_crush_tally.get(entity, 0) + 1

        lim = lim + 1
        if lim % 1000 == 0: print("Determining additional goals. Another", lim, "tweets processed.")
        # Truncate function earlier in the interest of runtime.
        if lim == 2750: break

    c_dress = Counter(best_dressed_tally)
    c_speech = Counter(best_acceptance_speech_tally)
    c_crush = Counter(best_celebrity_crush_tally)

    # Uncomment these lines if you want to view the entire tallied dictionary of phrases.
    # print("Dictionary after the increment of key : " + str(best_dressed_tally))
    best_dressed_individual = c_dress.most_common(1)
    # print("Dictionary after the increment of key : " + str(best_acceptance_speech_tally))
    best_acceptance_speech = c_speech.most_common(1)
    # print("Dictionary after the increment of key : " + str(best_celebrity_crush_tally))
    best_celebrity_crush = c_crush.most_common(1)

    print("Best Dressed Individual:", best_dressed_individual[0][0])
    print("Best Acceptance Speech:", best_acceptance_speech[0][0])
    print("Best Celebrity Crush:", best_celebrity_crush[0][0])

    # Write answers to file.
    with open('answers.json', 'w', encoding='utf-8') as f:
        json.dump(answer_json, f, ensure_ascii=False, indent=4)

    h.close()
    w.close()
    p.close()
    n.close()

    print("\n\n\nPretty-printing total results...\n\n\n")

    pretty_print_answers(answer_json)
    print("\nAdditional Goals:")
    print("Best Dressed Individual:", best_dressed_individual[0][0])
    print("Best Acceptance Speech:", best_acceptance_speech[0][0])
    print("Best Celebrity Crush:", best_celebrity_crush[0][0])

    # Stopping the runtime timer.
    stop = timeit.default_timer()
    print('\nTotal runtime elapsed: ', stop - start)

if __name__ == "__main__":
    """ This is executed when run from the command line """
    main()