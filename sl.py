import nltk
from nltk.stem import PorterStemmer

ps = PorterStemmer()
training_file = "WSJ_02-21.pos-chunk" /* specificy your file */
test_file = "WSJ_23.pos"

class TokenTraining:
    def __init__(self, word, POS, BIO, pre_word, pre_POS, pre_BIO):
        self.word = word
        self.POS = POS
        self.BIO = BIO
        self.pre_word = pre_word
        self.pre_POS = pre_POS
        self.pre_BIO = pre_BIO

class TokenTest:
    def __init__(self, word, POS, pre_word, pre_POS, stemmed, capitalized):
        self.word = word
        self.POS = POS
        self.pre_word = pre_word
        self.pre_POS = pre_POS
        self.stemmed = stemmed
        self.capitalized = capitalized

def training(file):
    pre_POS = ''
    pre_BIO = ''
    pre_word = ''
    count = 0
    with open(file) as fp:
        while True:
            line = fp.readline()
            if line != '\n':
                try:
                    pro = line.strip().split('\t')
                    token = TokenTraining(pro[0], pro[1], pro[2], pre_word, pre_POS, pre_BIO)
                    write_line('{}\tPOS={}\tprevious_POS={}\tprevious_word={}\tprevious_BIO={}\t{}\n'.format(token.word,
                    token.POS,pre_POS,pre_word, pre_BIO,token.BIO),'training')
                    pre_POS = token.POS
                    pre_BIO = token.BIO
                    pre_word = token.word
                    print('Wrote %d lines' % count)
                    count += 1
                except:
                    print("End Line.")
            else:
                write_line('\n', 'training')
                count += 1
            if not line:
                fp.close()
                print('Training File Output Successfully..')
                break

def test(file):
    pre_POS = ''
    pre_word = ''
    count = 0
    with open(file) as fp:
        while True:
            line = fp.readline()
            if line != '\n':
                try:
                    pro = line.strip().split('\t')
                    stemmed = ps.stem(pro[0])
                    capitalized = pro[0].istitle()
                    token = TokenTest(pro[0], pro[1], pre_word, pre_POS, stemmed, str(capitalized))
                    write_line(
                        '{}\tPOS={}\tprevious_POS={}\tprevious_word={}\tstemmed={}\tcapitalized={}\n'.format(token.word,
                        token.POS,pre_POS,pre_word,token.stemmed,token.capitalized),'test')
                    pre_POS = token.POS
                    pre_word = token.word
                    print('Wrote %d lines' % count)
                    count += 1
                except:
                    print("End of Line.")
            else:
                write_line('\n', 'test')
                count += 1
            if not line:
                fp.close()
                break

def write_line(line, file_type):
    if file_type == 'test':
        with open('test.feature', 'a') as f:
            f.write(line)
    else:
        with open('training.feature', 'a') as f:
            f.write(line)

training(training_file)
test(test_file)
