

# Read the file.txt
# Count how many times the same word occurs

# Open the file and read it

# Write the output
# output = open("output.html", "w")


# Count how many time the same word occurs

def create_dictionary():
    fo = open("gettysburg", "r")
    dict={}
    for line in fo:
        # we are converting
        line = line.lower()
        # here we are taking a line a splitting it in a list of words
        line = line.split()
        # for every word in the list we add it into a list
        for w in line:
            add_to_dict(w, dict)
    fo.close()
    return dict

# We have to define the add to dictionary function

def add_to_dict(word, dict):
    for key in dict.keys():
        if key == word:
            dict[key] = dict[key] + 1
            return dict
    else:
        dict[word] = 1
        return dict
    # here we are storing the value as one to a word that has never been found in our dictionary


# function to create the html file

def create_html(dict):
    # fo means file object
    fo = open("output.html", "w")
    # just use single quotes so it want clash with html tags
    fo.write( ' <!DOCTYPE html><html><head lang="en"><meta charset="UTF-8"><title>Tag Cloud Generator</title></head>/'
              '<body><div style="text-align: center; vertical-align: middle; font-family: /'
              'arial; color: white; background-color:black; border:1px solid black">')

    ###fo.write('<span style="font-size: 10px"> WORD </span> </span>')

    for key in dict.keys():
        fo.write('<span style="font-size:')
        fo.write(dict[key]) # this is the frequency
        fo.write('px">')
        fo.write[key]
        fo.write('</span>')
    fo.write('</div>\
        </body>\
        </html>')


##TESTING
dict = create_dict()
create_html(dict)

