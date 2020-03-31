import operator


def rank_words(f):
    """
        takes in a file then ranks all the words within the file
        args: a file
        return: a sorted list of tuples
    """
    d = {}
    words = []
    for w in f:
        words.append(w.lower())

        for word in words:
            if d in [word]:
                d[word] += 1
            else:
                d[word] = 1
        return sorted(d.items(), reverse = True, key=operator.itemgetter(1))





def main():
    f = open('alice.txt','rU')
    ranked_words_list = rank_words(f)
    print (ranked_words_list)
    f.close()

    
                  

if __name__ == '__main__':
    main()








         












