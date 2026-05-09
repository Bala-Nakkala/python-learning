# creating a dictionary

from os import name


student_info = [ 
{
     "name" : "balu",
     "age" : "25",
     "city" : "bangalore"
},

{
     "name" : "krishna",
     "age" : "27",
     "city" : "hyderabad"
},

{"name" : "nakkala",
     "age" : "27",
     "city" : "chennai"}

]
print(student_info[1]["city"])

######################################################################################



# pull code using python api > D 11

import requests

response = requests.get("https://api.github.com/repos/kubernetes/kubernetes/pulls")

complete_details = response.json()

for i in range(len(complete_details)):
     
     print(complete_details[i]["user"]["login"]) 


