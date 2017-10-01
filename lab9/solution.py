def create_dict():
    fo = open("gettysburg", "r")
    dict={}
    for line in fo:
        line = line.lower()
        line = line.split()
        print(line)
        for w in line:
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

def create_html(dict):
    fo = open("output.html", "w")
    fo.write('<!DOCTYPE html>\
<html>\
<head lang="en">\
<meta charset="UTF-8">\
<title>Tag Cloud Generator</title>\
</head>\
<body>\
<div style="text-align: center; vertical-align: middle; font-family: arial; color: white; background-color:black; border:1px solid black">')

    ###fo.write('<span style="font-size: 10px"> WORD </span> </span>')

    for key in dict.keys():
        fo.write('<span style="font-size: 0')
        fo.write(str(dict[key])) #here we are calling back the related key
        fo.write('px"> ')
        fo.write(key)
        fo.write('</span> </span>')

    fo.write('</div>\
</body>\
</html>')

##TESTING
dict = create_dict()
create_html(dict)
