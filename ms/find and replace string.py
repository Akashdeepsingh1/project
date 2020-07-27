def findReplaceString ( S: str, indexes, sources, targets) -> str:
    if not S or not sources or not targets:
        return S

    else:
        for j in range (len (sources)):
            if sources[j] in S:
                l = len (sources[j])
                ind = S.index (sources[j][0])
                if ind > -1:
                    S = S[:ind] + targets[j] + S[ind + l:]
                    break
        return S


S = "abcd"
indexes = [0,2]
sources = ["a","cd"]
targets = ["eee","ffff"]