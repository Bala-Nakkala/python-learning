
#
#numbers = input("please enter numbers:")
#print(numbers)

#
from importlib.metadata import files
import os
folders =input("please provide list of  folders names with spacesin between:").split()
for fol in folders:
   
   try:
       files = os.listdir(fol)
   except FileNotFoundError:
       print("please provide valid folder name")
       continue
   print(" === listingfilesfor the folder -" + fol)

   for file in files:
       print(file)  