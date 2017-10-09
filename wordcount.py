import string
import sys

# print('Arguments:', len(sys.argv))
# print('List:', str(sys.argv))
# if sys.argv < 2:
#     print('Too few arguments, please specify a file name')



def count_words(file_path):
    word_count = {}
    file_open = open(file_path)
    for line in file_open:
        line = line.rstrip()
        words = line.split(" ")

        for word in words:
            if word[-1] in string.punctuation:
                word = word[0:-1]
            elif word[0] in string.punctuation:
                word = word[1:]
            word_count[word.lower()] = word_count.get(word.lower(), 0) + 1

    print word_count

filename = sys.argv[1]
print('Filename:', filename)    
count_words(filename)
