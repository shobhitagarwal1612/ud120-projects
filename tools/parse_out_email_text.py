#!/usr/bin/python

import string

from nltk.stem.snowball import SnowballStemmer


def parseOutText(f):
    """ given an opened email file f, parse out all text below the
        metadata block at the top
        (in Part 2, you will also add stemming capabilities)
        and return a string that contains all the words
        in the email (space-separated) 
        
        example use case:
        f = open("email_file_name.txt", "r")
        text = parseOutText(f)
        
        """

    f.seek(0)  ### go back to beginning of file (annoying)
    all_text = f.read()

    ### split off metadata
    content = all_text.split("X-FileName:")

    words = ""
    if len(content) > 1:
        ### remove punctuation
        translator = str.maketrans({key: None for key in string.punctuation})
        text_string = content[1].translate(translator)
        text_string = text_string.translate(str.maketrans("\n\t","  "))
        ### project part 2: comment out the line below
        # words = text_string

        ### split the text string into individual words, stem each word,
        ### and append the stemmed word to words (make sure there's a single
        ### space between each stemmed word)

        split_text = text_string.strip().split(' ')
        text_string = []
        for text in split_text:
            if text != '':
                text_string.append(text)

        stemmer = SnowballStemmer("english", ignore_stopwords=True)
        words = [stemmer.stem(word) for word in text_string]

    return ' '.join(words)


def main():
    ff = open("../text_learning/test_email.txt", "r")
    text = parseOutText(ff)
    print(text)


if __name__ == '__main__':
    main()
