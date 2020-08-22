def createGraph(grph):
    from collections import defaultdict

    adjaMatrix = defaultdict(list)

    for each in grph:

        adjaMatrix[each[0]].append(each[1])
        # adjaMatrix[each[1]].append(each[1])

    print(adjaMatrix)


graph = [["ATH", "TBS"], ["TBS", "DME"], ["DME", "LCA"], ["LCA", "TLV"], ["TLV", "ATH"],
         ["ICN", "IKT"], ["IKT", "DME"], ["DME", "LED"],
         ["LED", "SVO"], ["SVO", "BEG"], ["BEG", "TIV"],
         ["SVO", "PRG"], ["LED", "PRG"],
         ["PRG", "DUB"], ["PRG", "MXP"], ["PRG", "ORY"], [
    "PRG", "CRL"], ["PRG", "AMS"],
    ["DME", "AUH"], ["AUH", "CGK"], ["CGK", "DPS"], [
    "DPS", "SIN"], ["SIN", "CGK"],
    ["KUL", "DPS"], ["SIN", "BKK"], ["SIN", "PEK"], ["PEK", "MSQ"], ["MSQ", "LED"]]

createGraph(graph)
