import json
import random
def talabalar():
    import random

    massiv = []
    for i in range(1,1000+1):
        thisdict =	{
            f"talaba{i}":{
                "fan-1": random.randint(1,30),
                "fan-2": random.randint(1,30),
                "fan-3": random.randint(1,10),
                "fan-4": random.randint(1,10),
                "fan-5": random.randint(1,10),
                }
            }
        massiv.append(thisdict)


        for j in thisdict.keys():
            print(j)
        fan_1 = thisdict[f"talaba{i}"]["fan-1"] * 3.1
        fan_2 = thisdict[f"talaba{i}"]["fan-2"] * 2.1
        fan_3 = thisdict[f"talaba{i}"]["fan-3"] * 1.1
        fan_4 = thisdict[f"talaba{i}"]["fan-4"] * 1.1
        fan_5 = thisdict[f"talaba{i}"]["fan-5"] * 1.1
        u_balari = fan_1 + fan_2 + fan_3 + fan_4 + fan_5
        thisdict[f"talaba{i}"]["Umumiy_bal"] = round(u_balari,3)

        print("fan-1 --->",round(fan_1,3),"\n",
              "fan-2 ---->",round(fan_2,3),"\n",
              "fan-3 --->",round(fan_3,3),"\n",
              "fan-4 ---->",round(fan_4,3),"\n",
              "fan-5 --->",round(fan_5,3),"\n",
              thisdict)
    with open('data.json', 'w') as json_file:
        json.dump(massiv, json_file, indent=4)  # indent for pretty printing
# talabalar()
# print(massiv)

def univers():
    import random
    import json
    import random
    un = []
    for i in range(1, 10 + 1):
        universitutlar = {
            f"universitut-{i}": {
                f"{i}_1": "Derection_1",
                f'{i}_2': "Derction_2",
                f'{i}_3': "Derction_3",
                f'{i}_4': "Derction_4",
                f'{i}_5': "Derction_5",
                f'{i}_6': "Derction_6",
                f'{i}_7': "Derction_7",
                f'{i}_8': "Derction_8",
                f'{i}_9': "Derction_9",
                f'{i}_10': "Derction_10",
            }
        }
        un.append(universitutlar)
    with open('univer.json', 'w') as json_file:
        json.dump(un, json_file, indent=4)  # indent for pretty printing
# univers()



import json

# Reading from a JSON file
with open('data.json', 'r') as json_file:
    data = json.load(json_file)

# print(data)


with open('univer.json', 'r') as json_file:
    univer = json.load(json_file)

print(univer[0]['universitut-1']['1_1'])

# for i in univer:
#     # print(i)
#     for j in i:
#         # print(j)
#         for k in j:
#             print(k)
















# # Sample data
# data = {
#     "name": "Alice",
#     "age": 30,
#     "city": "New York",
#     "is_student": False
# }
#
# # Writing to a JSON file
# with open('data.json', 'w') as json_file:
#     json.dump(data, json_file, indent=4)  # `indent` for pretty formatting


# print(thisdict)
# for x in thisdict:
#     print(x)
# Writing to a JSON file
# with open('data.json', 'w') as json_file:
#     json.dump(x, json_file, indent=4)  # indent for pretty printing
# print(thisdict[f"talaba{i}"]["fan-1"])
# print(thisdict[f"talaba{i}"]["fan-2"])
# print(thisdict[f"talaba{i}"]["fan-3"])
# print(thisdict[f"talaba{i}"]["fan-4"])
# print(thisdict[f"talaba{i}"]["fan-5"])

# print(fanlar*3.1)
# print( "fan-1 --->",thisdict[f"talaba{i}"]["fan-1"]*3.1 )








