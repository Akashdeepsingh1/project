from collections import defaultdict


class SnapshotArray:

    def __init__ (self, length: int):
        self.len = length
        self.snapls = [0] * length
        self.snapTimeMachine = defaultdict (list)
        self.snapcount = 0

    def set (self, index: int, val: int) -> None:
        if index < self.len:
            self.snapls[index] = val

    def snap (self) -> int:
        self.snapTimeMachine[self.snapcount] = self.snapls[:]
        temp = self.snapcount
        self.snapcount += 1
        return temp

    def get (self, indext: int, snap_id: int) -> int:
        if snap_id in self.snapTimeMachine:
            t = self.snapTimeMachine[snap_id]
            return t[indext]
            #return self.snapTimeMachine[snap_id].index (indext)
        else:
            return 0
        #Your SnapshotArray object will be instantiated and called as such:
obj = SnapshotArray(3)
obj.set(0,5)
param_2 = obj.snap()
param_3 = obj.get(0,0)
print(param_3)