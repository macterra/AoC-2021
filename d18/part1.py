import json

input = """[1,2]
[[1,2],3]
[9,[8,7]]
[[1,9],[8,5]]
[[[[1,2],[3,4]],[[5,6],[7,8]]],9]
[[[9,[3,8]],[[0,9],6]],[[[3,7],[4,9]],3]]
[[[[1,3],[5,3]],[[1,3],[8,7]]],[[[4,9],[6,9]],[[8,2],[7,3]]]]"""

input = """[[[[[9,8],1],2],3],4]
[7,[6,[5,[4,[3,2]]]]]
[[6,[5,[4,[3,2]]]],1]
[[3,[2,[1,[7,3]]]],[6,[5,[4,[3,2]]]]]
[[3,[2,[8,0]]],[9,[5,[4,[3,2]]]]]"""

class Item:
    def __init__(self, val, dep):
        self.val = val
        self.dep = dep
    
    def __repr__(self):
        return f"<{self.val} {self.dep}>"

def flatten(num, dep, flat):
    if isinstance(num, int):
        flat.append(Item(num, dep))
    else:
        for i in num:
            flatten(i, dep+1, flat)
    return flat

def explode(num):
    count = len(num)
    for i in range(count):
        if num[i].dep > 4:
            if i > 0:
                num[i-1].val += num[i].val
            if i < count-2:
                num[i+2].val += num[i+1].val
            num.insert(i, Item(0,num[i].dep-1))
            del num[i+1:i+3]
            return True
    return False

lines = input.split('\n')
for line in lines:
    x = json.loads(line)
    f = flatten(x, 0, [])
    print(x)
    print(f)
    ex = explode(f)
    print(ex, f)
    print()
