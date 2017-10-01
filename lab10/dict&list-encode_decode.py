# Write a Python function that takes two parameters – the original message and the key, and
# returns the encoded message.

# message = input("Insert a message ")
#
# def cipher(p):
#     key = ""
#     for c in p:
#         new_c = ord(c)
#         new_c += 1
#         new_c = chr(new_c)
#         key = key + new_c
#     return key.upper()
#
# print(cipher(message))
#
# key = cipher(message)
#
# def decode(p):
#     decoded_message = ""
#     for c in key:
#         decoded_c = ord(c)
#         decoded_c = decoded_c - 1
#         decoded_c = chr(decoded_c)
#         decoded_message = decoded_message + decoded_c
#     return decoded_message.lower()
#
# print(decode(key))

print("Welcome!\n" "What would you like to do?")

alphabet = list("ABCDEFGHIJKLMNOPQRSTUVWXYZ")
key = list("VJZBGNFEPLITMXDWKQUCRYAHSO")

menu = {}
menu['1']="Encode"
menu['2']="Decode"
menu['3']="Exit"
while True:
  print("\nMENU")
  sorted_options = sorted(menu.keys())
  for entry in sorted_options:
      print(entry, menu[entry])

  selection= input("Please Select:")
  if selection =='1':
      message = list(input("Insert an uppercase message: "))
      def cipher(p):
          new_c = ""
          for c in p:
              for l in alphabet:
                  if c == l:
                      new_c = new_c + key[alphabet.index(l)]
          return new_c
      print("The encoded message is: ", cipher(message))
  elif selection == '2':
      encoded_message = list(input("Insert the decoded message: "))
      def decode(p):
          decoded_message = ""
          for c in p:
              for l in key:
                  if c == l:
                      decoded_message = decoded_message + alphabet[key.index(l)]
          return decoded_message
      print("The decoded message is: ", decode(encoded_message))
  elif selection == '3':
      print("Bye!")
      break
  else:
      print ("Unknown Option Selected!")

