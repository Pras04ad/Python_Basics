def Bayes(dict):
    pVal = (P["B|A"]*P["A"])/P["B"]
    return pVal
P = {"A":0.1,"B":0.05,"B|A":0.07}
res = Bayes(P)
print(res)

# P.clear()
# print(P)

# copyP = P.copy()
# print(copyP)

selKeys = ('A','B')
skDict = P.fromkeys(selKeys)
print(skDict)

print(P.get("A"))
print(P.items())
print(P.keys())
