#Password verification method
# Conditions:
    # Password OK if :
    #     1+ cap letter
    #     1+ lowercase letter
    #     1 number between 0-9
    #     1 spec carac between $ & or @
    #     length min: 6 carac
    #     Length max: 12 carac


#!/usr/bin/env python3
import re

password = raw_input("Choose a password / Choisir un mot de passe: ")
print password


def password_check(password):
  print("checking...")

  i = True
  while i:
      if (len(password)<6 or len(password)>12):
          break
      elif not re.search("[a-z]",password):
          break
      elif not re.search("[0-9]",password):
          break
      elif not re.search("[A-Z]",password):
          break
      elif not re.search("[$#@]",password):
          break
      elif re.search("\s",password):
          break
      else:
          print("Valid password / Mot de passe valide")
          i = False
          break

  if i:
    print("Invalid password / Mot de passe invalide")


password_check(password)


