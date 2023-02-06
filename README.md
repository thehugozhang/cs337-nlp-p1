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