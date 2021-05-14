# Sequence-Labeling

The program would take the trainning corpus and test corpus as input, and produce two feature files called training.feature and test.feature as output. 

Using python sl.py to run the system, and output the contained tags for each attributes in feature files. 

The program would identify the attributes from each token in the trainning and test files. It will take previous word, POS, BIO token as the key to find the stemmed version of the word with different tags. The output in the feature files would have the completed BIO tag, features of the sentence and special dictionary in it.
