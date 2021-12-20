import re
import numpy as np
from scipy.spatial.transform import Rotation as R

input = """--- scanner 0 ---
-1,-1,1
-2,-2,2
-3,-3,3
-2,-3,1
5,6,-4
8,0,7"""

input = """--- scanner 0 ---
1,1,1"""

class Scanner:
    def __init__(self, n, lines, i):
        self.n = n
        beacons = []    
        while i < len(lines):
            if not lines[i]:
                break
            x, y, z = lines[i].split(',')
            i += 1
            print('beacon', i, x, y, z)
            beacons.append([x,y,z])
        self.beacons = beacons
        self.generateVariants()

    def __repr__(self):
        return f"scanner {self.n} {self.beacons}"

    def beaconCount(self):
        return len(self.beacons)

    def generateVariants(self):
        var1 = []
        var = np.array(self.beacons).astype(int)        
        print(var)
        var1.append(var)

        r = R.from_euler('x', 90, degrees=True)
        var = r.apply(var).astype(int)
        print(var)
        var1.append(var)
        
        #r = R.from_euler('x', 180, degrees=True)
        var = r.apply(var).astype(int)
        print(var)
        var1.append(var)
        
        #r = R.from_euler('x', 270, degrees=True)
        var = r.apply(var).astype(int)
        print(var)
        var1.append(var)        

        # var2 = []

        # for arr in var1:
        #     var2.append(arr)

        #     r = R.from_euler('y', 90, degrees=True)
        #     var = r.apply(arr).astype(int)
        #     print(var)
        #     var2.append(var)
            
        #     r = R.from_euler('y', 180, degrees=True)
        #     var = r.apply(arr).astype(int)
        #     print(var)
        #     var2.append(var)
            
        #     r = R.from_euler('y', 270, degrees=True)
        #     var = r.apply(arr).astype(int)
        #     print(var)
        #     var2.append(var)

        # var3 = []

        # for arr in var2:
        #     var3.append(arr)            
        
        #     r = R.from_euler('z', 90, degrees=True)
        #     var = r.apply(arr).astype(int)
        #     print(var)
        #     var3.append(var)
            
        #     r = R.from_euler('z', 180, degrees=True)
        #     var = r.apply(arr).astype(int)
        #     print(var)
        #     var3.append(var)
            
        #     r = R.from_euler('z', 270, degrees=True)
        #     var = r.apply(arr).astype(int)
        #     print(var)
        #     var3.append(var)

        print(var1, len(var1)) 
        # print(var2, len(var2)) 
        # print(var3, len(var3))

        variants = []
        for var in var1:
            x = [tuple(row) for row in var]
            variants.append(x)
        print(variants, len(variants))
        svar = {tuple(x) for x in variants}
        print(svar, len(svar))

  
lines = input.split('\n')
scanners = []
i = 0
while i < len(lines):
    line = lines[i]
    print(i, line)
    m = re.match('--- scanner \d+ ---', line)
    if m:
        n = len(scanners)
        scanner = Scanner(n, lines, i+1)
        i += scanner.beaconCount()
        scanners.append(scanner)
    i += 1

print(scanners)