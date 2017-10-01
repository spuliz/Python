def create_stopdict():
    fo = open("stopword", "r")
    stopdict={}
    for line in fo:
        line = line.lower()
        stopdict = line
    fo.close()
    return stopdict

def create_dict():
    fo = open("gettysburg", "r")
    dict={}
    for word in fo:
        if word not in stopdict:
            word = word.lower()
            word = word.split()
            print(word)
            for w in word:
                add_to_dict(w, dict)
    fo.close()
    return dict


def add_to_dict(word, dict):
    for key in dict.keys():
        if key == word:
            dict[key] = dict[key]+1
            return dict
    else:
        dict[word] =1
        return dict

dict = create_dict()
