

# # thisdict = {
# #   "brand": "Ford",
# #   "model": "Mustang",
# #   "year": 1964
# # }
# # thisdict.update({"year":2018})



# car = {
# "brand": "Ford",
# "model": "Mustang",
# "year": 1964
# }

# car.update({"year:2018"})
# print(car)

result = {"John": 45, "Mark": 70, "Jack": 32, "Devin": 65}
new_result = {}

for name, marks in result.items():
    if marks >= 40:
        new_result[name] = "Pass"
        new_result[name] = "Fail"

print(new_result)

    
    


