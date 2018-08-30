#!/usr/bin/env python3
import re

password = raw_input("Choisir un mot de passe: ")
print password

# Verifier 'password'
    # Password OK si :
    #     1 lettre majuscule ou plus
    #     1 lettre minuscule ou plus
    #     1 chiffre entre 0 et 9
    #     1 caractere special entre $ & ou @
    #     Longueur min: 6 carac
    #     Longueur max: 12 carac

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
          print("Mot de passe valide")
          i = False
          break

  if i:
    print("Mot de passe invalide")

password_check(password)


