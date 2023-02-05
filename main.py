"""

CS337 Intro NLP Project 1 - Group 10

"""

__version__ = '1.0'
__author__ = 'Hugo Zhang'

# System imports.
from helpers_system import pos_tag_text, chunk_tagged_text
from regex_system import get_actors, get_media, get_award, award_type_check, expand_hashtags
from type_system import getAwardType, isMovie, isShow

# Other imports.
import json
from collections import Counter
import timeit

OFFICIAL_AWARDS_1315 = ['cecil b. demille award', 'best motion picture - drama', 'best performance by an actress in a motion picture - drama', 'best performance by an actor in a motion picture - drama', 'best motion picture - comedy or musical', 'best performance by an actress in a motion picture - comedy or musical', 'best performance by an actor in a motion picture - comedy or musical', 'best animated feature film', 'best foreign language film', 'best performance by an actress in a supporting role in a motion picture', 'best performance by an actor in a supporting role in a motion picture', 'best director - motion picture', 'best screenplay - motion picture', 'best original score - motion picture', 'best original song - motion picture', 'best television series - drama', 'best performance by an actress in a television series - drama', 'best performance by an actor in a television series - drama', 'best television series - comedy or musical', 'best performance by an actress in a television series - comedy or musical', 'best performance by an actor in a television series - comedy or musical', 'best mini-series or motion picture made for television', 'best performance by an actress in a mini-series or motion picture made for television', 'best performance by an actor in a mini-series or motion picture made for television', 'best performance by an actress in a supporting role in a series, mini-series or motion picture made for television', 'best performance by an actor in a supporting role in a series, mini-series or motion picture made for television']

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

def main():
    """ Main entry point of the app """

    # Starting total runtime timer.
    start = timeit.default_timer()

    h = open('gg2013-host.json')
    host_data = json.load(h)
    host_tally = dict()

    w = open('gg2013-winner.json')
    data = json.load(w)
    winner_tally = dict()

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
        if lim == 10: break
    
    c = Counter(host_tally)
    top_two_results = c.most_common(2)
    print("Dictionary after the increment of key : " + str(host_tally))
    print("Top five hosts:", top_two_results)
    answer_json["host"] = [top_two_results[0][0], top_two_results[1][0]]

    lim = 0

    # Determine winners from award names.
    for award_category in OFFICIAL_AWARDS_1315:
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
                        winner_tally[entity] = winner_tally.get(entity, 0) + 1

            lim = lim + 1
            if lim % 1000 == 0: print(award_category, lim)
        lim = 0
        c = Counter(winner_tally)
        top_three_results = c.most_common(3)
        print(award_category, top_three_results)
        if top_three_results != []:
            answer_json[award_category]["winner"] = top_three_results[0][0]
        winner_tally.clear()

    lim = 0

    # Determine presenters from award names.
    for award_category in OFFICIAL_AWARDS_1315:
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
        print("Top Five Presenters (if any):", top_five_results)
        if top_five_results != []:
            answer_json[award_category]["presenters"] = top_five_results[0][0]
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
            if lim % 1000 == 0: print(award_category, lim)
        c = Counter(nominee_tally)
        top_five_results = c.most_common(5)
        print("Top 5 Nominees (if any):", top_five_results)
        nominees = []
        if top_five_results != []:
            for nominee in top_five_results:
                nominees.append(nominee[0])
        answer_json[award_category]["nominees"] = nominees
        nominee_tally.clear()

    # Write answers to file.
    with open('answers.json', 'w', encoding='utf-8') as f:
        json.dump(answer_json, f, ensure_ascii=False, indent=4)

    h.close()
    w.close()
    p.close()
    n.close()

    # Stopping the runtime timer.
    stop = timeit.default_timer()
    print('Total runtime elapsed: ', stop - start)

if __name__ == "__main__":
    """ This is executed when run from the command line """
    main()