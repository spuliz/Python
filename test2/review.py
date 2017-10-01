
# def create_dict():
#     fo = open("text", "r")
#     dict = {}
#     for line in fo:
#         line = line.lower()
#         line = line.split()
#         print(line)
#         for w in line():
#             frequency(w,dict)
#     fo.close()
#     return dict
#
# def frequency(word, dict):
#     for key in dict.keys():
#         if key == word:
#             dict[key] = dict[key] + 1
#             return dict
#         else:
#             dict[key] = 1
#             return dict
#
# # dict = create_dict()
#
# def create_html(dict):
#     fo = open("output.html", "w")
#     fo.write('<!DOCTYPE html>\
# <html>\
# <head lang="en">\
# <meta charset="UTF-8">\
# <title>Tag Cloud Generator</title>\
# </head>\
# <body>\
# <div style="text-align: center; vertical-align: middle; font-family: arial; color: white; background-color:black; border:1px solid black">')
#
#     for key in dict.keys():
#         fo.write('<span style="font-size: 0')
#         fo.write(str(dict[key]))
#         fo.write('px"> ')
#         fo.write(key)
#         fo.write('</span> </span>')
#
#     fo.write('</div>\ '
#              '</body>\
#              </html>')
#
#
# ##TESTING
# dict = create_dict()
# create_html(dict)

#---------------------------->

# user_input = input("Please provide list of numbers separated by comma, e.g. 1,2,3: ")
# list = list(map(int,user_input.split(',')))
#
# def sumList(list):
#     result = 0
#     for element in list:
#         result = result + element
#     print(result)
#
# my_print = sumList(list)


# SECOND SOLUTION

# list = [1,3,5,8, 10]
# def sum_all(list):
#     sum = 0
#     for i in range(0,len(list)):
#         sum = sum + list[i]
#     print(sum)
#     return sum
#
# result = sum_all(list)

