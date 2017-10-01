def create_stopdict():
    stopword = open("stopword", "r")
    stopdict={}
    for line in stopword:
        line = line.lower()
        line = line.split()
        for w in line:
            add_to_dict(w, dict)
    stopword.close()
    return stopdict




def add_to_dict(word, dict):
    for key in stopdict.keys():
        if key == word:
            stopdict[key] = stopdict[key]+1
            return dict
    else:
        stopdict[word] =1
        return dict


stopdict = create_stopdict()

print(stopdict)
