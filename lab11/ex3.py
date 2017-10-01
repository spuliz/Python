# Given a string, return the largest "block" in the string. A block is a run of adjacent chars
# that are the same.

# a = "hoopla"
# p = ""
# for c in a:
#     if c == p:
#         print(p)
#
#
# a = list(a)
# print(a)
#
# already_done = []
# for element in a:
#     already_done.append(element)
#     print(already_done)
#     if element in already_done:
#         print(element)
#
# same = ""
# for c in a:
#     if c == same:


a = "hoopla"
block = ""
for i in range (0, len(a)+1):
    if a[i] == a[i+1]:
        block = block + a[i]

