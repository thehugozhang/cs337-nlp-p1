The GitHub repository for this project can be found at https://github.com/thehugozhang/cs337-nlp-p1.

# Golden Globe Awards NLP Exploration (cs337-nlp-p1)

Developed for COMP_SCI 337 Natural Language Processing at [Northwestern University](https://www.northwestern.edu/).

## Description

This project processes a dataset of ~175k tweets (stored in gg2013.json) that were tweeted during the 2013 Golden Globe Awards and determines the hosts, award categories, winners, presenters, nominees, and other additional goals (best dressed, best acceptance speech, best celebrity crush).

## Getting Started

### Dependencies

This system depends on the following third-party modules.
* [Natural Language Toolkit (NLTK)](https://www.nltk.org/install.html)
    * [punkt](https://www.nltk.org/_modules/nltk/tokenize/punkt.html)
    * [averaged_perceptron_tagger](https://www.nltk.org/_modules/nltk/tag/perceptron.html)
    * [maxent_ne_chunker](https://www.nltk.org/_modules/nltk/chunk.html)
    * [words](https://www.nltk.org/book/ch02.html)
* [Fuzzywuzzy](https://pypi.org/project/fuzzywuzzy/)
    * [python-Levenshtein](https://github.com/ztane/python-Levenshtein/)
* [Requests](https://pypi.org/project/requests/)
* [NumPy](https://numpy.org/)

### Installing

Specific installation instructions can be found below.
* To install NLTK:
```
pip3 install --user -U nltk
```

* To install the required NLTK packages, follow the guide [here](https://www.nltk.org/data.html).

* To install Fuzzywuzzy and python-Levenshtein:
```
pip3 install fuzzywuzzy
pip3 install python-Levenshtein
```

* To install Requests:
```
pip3 install requests
```

* To install Numpy:
```
pip3 install --user -U numpy
```

### Executing the system

* To execute the system outside the associated [autograder](https://github.com/milara/gg-project-master/blob/master/autograder.py):

```
python3 main_system.py
```

* *This system takes roughly ~8-10 minutes (or an average of ~500 seconds) to run in its entirety. It will both pretty-print its results in a human-readable format to the console and write its results to answers.json on completion.*

* To run the autograder:
```
python3 autograder.py
```

## Help

For any additional troubleshooting assistance, please reach out to [hugozhang2023@u.northwestern.edu](mailto:hugozhang2023@u.northwestern.edu).

## Results

### `autograder.py` Output
```
{'2013': {'awards': {'completeness': 0.21794871794871792,
                     'spelling': 0.6140858907029437},
          'hosts': {'completeness': 1.0, 'spelling': 1.0},
          'nominees': {'completeness': 0.0, 'spelling': 0.0},
          'presenters': {'completeness': 0.09326923076923076,
                         'spelling': 0.15384615384615385},
          'winner': {'spelling': 0.8990384615384616}},
 '2015': {'awards': {'completeness': 0.21794871794871792,
                     'spelling': 0.6140858907029437},
          'hosts': {'completeness': 1.0, 'spelling': 1.0},
          'nominees': {'completeness': 0.0095, 'spelling': 0.04},
          'presenters': {'completeness': 0.0, 'spelling': 0.0},
          'winner': {'spelling': 0.0}}}
```

### Pretty-printed Output
```
Host(s): Amy Poehler, Tina Fey

Mined Award Names: Best Director, Best Original Song, Best Actor, Best Picture, Best Motion Picture - Drama, Best Screenplay, Best Actress, Best Motion Picture - Musical - Comedy, Best Drama, Best Golden Globes, Best Original Score, Best Foreign Film, Best Part, Best Actor - Drama, Best Motion Picture, Best Song, Best Original Song - Motion Picture, Best Actor In A Motion - Motion Picture - Drama, Best Tv Series - Drama, Best Actress In A Motion - Motion Picture - Drama, Best Movie, Best Television Series - Drama, Best Foreign Language, Best Actor - Musical - Comedy, Best Actor In A Motion - Motion Picture - Musical - Comedy, Best Actor In A Tv

Award: Best Motion Picture - Drama
Presenters: Julia Roberts
Nominees: N/A
Winner: Argo

Award: Best Performance By An Actress In A Motion Picture - Drama
Presenters: Lea Michele
Nominees: Lea Michele
Winner: Jessica Chastain

Award: Best Performance By An Actor In A Motion Picture - Drama
Presenters: N/A
Nominees: N/A
Winner: Daniel Day-Lewis

Award: Best Motion Picture - Comedy Or Musical
Presenters: Jay Leno
Nominees: N/A
Winner: Les Miserables

Award: Best Performance By An Actress In A Motion Picture - Comedy Or Musical
Presenters: N/A
Nominees: N/A
Winner: Jennifer Lawrence

Award: Best Performance By An Actor In A Motion Picture - Comedy Or Musical
Presenters: N/A
Nominees: N/A
Winner: Hugh Jackman

Award: Best Animated Feature Film
Presenters: N/A
Nominees: N/A
Winner: Brave

Award: Best Foreign Language Film
Presenters: N/A
Nominees: N/A
Winner: Amour

Award: Best Performance By An Actress In A Supporting Role In A Motion Picture
Presenters: Dennis Quaid
Nominees: Mary Todd Lincoln, Anne Hathaway, Les Miserables
Winner: Anne Hathaway

Award: Best Performance By An Actor In A Supporting Role In A Motion Picture
Presenters: Bradley Cooper
Nominees: Bradley Cooper, Kate Hudson
Winner: Christoph Waltz

Award: Best Director - Motion Picture
Presenters: N/A
Nominees: N/A
Winner: Ben Affleck

Award: Best Screenplay - Motion Picture
Presenters: N/A
Nominees: N/A
Winner: Django

Award: Best Original Score - Motion Picture
Presenters: N/A
Nominees: N/A
Winner: Life of Pi

Award: Best Original Song - Motion Picture
Presenters: J. Lo
Nominees: N/A
Winner: Skyfall

Award: Best Television Series - Drama
Presenters: N/A
Nominees: N/A
Winner: Homeland

Award: Best Performance By An Actress In A Television Series - Drama
Presenters: Lea Michele
Nominees: Lea Michele
Winner: Claire Danes

Award: Best Performance By An Actor In A Television Series - Drama
Presenters: N/A
Nominees: N/A
Winner: Homeland

Award: Best Television Series - Comedy Or Musical
Presenters: Jay Leno
Nominees: N/A
Winner: Girls

Award: Best Performance By An Actress In A Television Series - Comedy Or Musical
Presenters: N/A
Nominees: Lena Dunham
Winner: Lena Dunham

Award: Best Performance By An Actor In A Television Series - Comedy Or Musical
Presenters: N/A
Nominees: N/A
Winner: Don Cheadle

Award: Best Mini-Series Or Motion Picture Made For Television
Presenters: N/A
Nominees: N/A
Winner: Game Change

Award: Best Performance By An Actress In A Mini-Series Or Motion Picture Made For Television
Presenters: N/A
Nominees: N/A
Winner: Julianne Moore

Award: Best Performance By An Actor In A Mini-Series Or Motion Picture Made For Television
Presenters: N/A
Nominees: Si Robertson
Winner: Kevin Costner

Award: Best Performance By An Actress In A Supporting Role In A Series, Mini-Series Or Motion Picture Made For Television
Presenters: Maggie Smith
Nominees: N/A
Winner: Maggie Smith

Award: Best Performance By An Actor In A Supporting Role In A Series, Mini-Series Or Motion Picture Made For Television
Presenters: N/A
Nominees: N/A
Winner: Ed Harris

Award: Cecil B. Demille Award
Presenters: N/A
Nominees: N/A
Winner: N/A

Additional Goals:
Best Dressed Individual: Lea
Best Acceptance Speech: Adele
Best Celebrity Crush: Jennifer Lawrence

Total runtime elapsed:  503.532968664018
```