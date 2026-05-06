# list

fruits = ["apple", "banana", "orange"]
print(fruits)   

# tuples
fruits_tuple = ("apple", "mango", "orange") # This will raise an error because tuples are immutable
print(fruits_tuple)

# dictionary
fruits_dict = {"apple": "red", "banana": "yellow", "orange": "orange"}
fruits_dict["red"] = "purple"
print(fruits_dict)

# dictionary with list and tuple

data = {
    "names": ["John", "Jane", "Bob"],
    "ages": (25, 30, 35),
    "city": {"New York"}
}
data["names"][2] = "Smith"
data["ages"] = (22, 30, 35)
data["city"] = "Los Angeles"
print(data)