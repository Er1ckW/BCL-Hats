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

customDict["hats"].extend(customGMDict["hats"])
customDict["hats"].extend(customGMHDict["hats"])

aSet = set()
for hat in customDict["hats"]:
    if hat["name"] in aSet:
        customDict["hats"].remove(hat)
    else:
        aSet.add(hat["name"])

f = open("TheOtherHats/CustomHats.json", "w")
f.write(json.dumps(customDict))
f.close()

