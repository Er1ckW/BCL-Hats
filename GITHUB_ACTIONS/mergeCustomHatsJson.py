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

customGMHDict["hats"].extend(customDict["hats"])
customGMHDict["hats"].extend(customGMDict["hats"])

aSet = set()
for hat in customDict["hats"]:
    if hat["name"] in aSet:
        customDict["hats"].remove(hat)
    else:
        aSet.add(hat["name"])

f = open("TheOtherHats/CustomHats.json", "w")
f.write(json.dumps(customDict))
f.close()

