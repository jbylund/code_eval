#!/usr/bin/python
import sys, re, string, collections, operator

def find_following(wordlist,iwords):
    following_words = collections.Counter()
    denom = 0
    for i in xrange(0,len(wordlist)-len(iwords)):
        if(iwords == wordlist[i:i+len(iwords)]):
            following_words[wordlist[i+len(iwords)]] += 1
            denom += 1
    mycommons = sorted(following_words.most_common(), key=operator.itemgetter(0))
    mycommons = sorted(mycommons, key=operator.itemgetter(1),reverse=True)
    ans = ""
    for i in mycommons:
        ans += i[0]
        ans +=","
        num = float(i[1])/float(denom)
        ans += '{0:.3f}'.format(num)
        ans +=";"
    print ans.rstrip(";")
    return

poem = """Mary had a little lamb its fleece was white as snow;
And everywhere that Mary went, the lamb was sure to go. 
It followed her to school one day, which was against the rule;
It made the children laugh and play, to see a lamb at school.
And so the teacher turned it out, but still it lingered near,
And waited patiently about till Mary did appear.
\"Why does the lamb love Mary so?\" the eager children cry;
\"Why, Mary loves the lamb, you know\" the teacher did reply.\""""

word_list = list()
pattern = re.compile('[^a-z ]+')
poem = pattern.sub(' ', poem.lower())
for iword in poem.split():
    word_list.append(iword)

#print " ".join(word_list)
test_cases = open(sys.argv[1], 'r')
for test in test_cases:
    test = test.rstrip().lower()
    if(0 == len(test)):
        continue
    ngram_len = int(test.split(",")[0])
    words = test.split(",")[1].split()
    find_following(word_list,words)


