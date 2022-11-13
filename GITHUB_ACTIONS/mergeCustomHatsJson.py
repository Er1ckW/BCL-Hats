import json

custom = open("TheOtherHats/CustomHats.json","r")
customGM = open("TheOtherHats/CustomGMHats.json","r")
customGMH = open("TheOtherHats/CustomGMHHats.json","r")

customDict = json.loads(custom.read())
customGMDict = json.loads(customGM.read())
customGMHDict = json.loads(customGMH.read())

custom.close()
customGM.close()
customGMH.close()

for i in range(len(customGMHDict["hats"])):
    oldName = customGMHDict["hats"][i]["name"]
    author = customGMHDict["hats"][i]["author"]
    newName = f"{oldName}_{author}"
    customGMHDict["hats"][i]["name"] = newName
for i in range(len(customGMDict["hats"])):
    oldName = customGMDict["hats"][i]["name"]
    author = customGMDict["hats"][i]["author"]
    newName = f"{oldName}_{author}"
    customGMDict["hats"][i]["name"] = newName
for i in range(len(customDict["hats"])):
    oldName = customDict["hats"][i]["name"]
    author = customDict["hats"][i]["author"]
    newName = f"{oldName}_{author}"
    customDict["hats"][i]["name"] = newName

customGMHDict["hats"].extend(customGMDict["hats"])
customGMHDict["hats"].extend(customDict["hats"])

hatSet = set()
for hat in customGMHDict["hats"]:
    if hat["name"] in hatSet:
        customGMHDict["hats"].remove(hat)
    else:
        hatSet.add(hat["name"])

f = open("TheOtherHats/CustomHats.json", "w")
f.write(json.dumps(customGMHDict))
f.close()

