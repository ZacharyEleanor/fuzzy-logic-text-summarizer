# Fuzzy Logic Text Summarizer

This repository contains an implementation of text summarization utilizing fuzzy logic. The text file is taken as input and output is a summarized text.

## Language & Package

* Python 3.6
* skfuzzy from sci-kit fuzzy
* nltk



### Preprocessing

The data is preprocessed using the following techniques:

* Lemmatization
* Stopwords
* Sentence tokenizing

## Fuzzifier

This step involves getting features from the extracted sentence

### Features Extraction

The features extracted include:

* Tight weight
* Sentence location
* Sentence length
* Thematic word
* Term weight
* Sentence similarity
* Proper noun
* Numerical data

### Membership function

The membership functions used are:

* Triangular membership function
* Auto membership function

### Inference Engine

This is rule-based.

## Defuzzifier

This step involves converting the fuzzified values to crisp for sentence selection.


## Sentence Selection

The compression rate is 20%, which means the top 20% sentence with the highest score from the list of all the sentences in the corpus are chosen.