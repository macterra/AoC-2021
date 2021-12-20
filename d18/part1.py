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

#input = "[[[[[9,8],1],2],3],4]"
#input = "[7,[6,[5,[4,[3,2]]]]]"
input = "[[6,[5,[4,[3,2]]]],1]"
#input = "[[3,[2,[1,[7,3]]]],[6,[5,[4,[3,2]]]]]"

def explode2(lt, rt, depth):
    print(f"explode d={depth} lt={lt} rt={rt}")

    if isinstance(lt, list):
        a, b = lt

        if depth > 2:
            if isinstance(a, list):
                c, d = a
                return [[0, d+b], rt]
            if isinstance(b, list):
                c, d = b
                return [[a+c, 0], rt]

        return [explode(a, b, depth+1), rt]
    elif isinstance(rt, list):
        a, b = rt

        if depth > 2:
            if isinstance(a, list):
                c, d = a
                return [lt, [0, d+b]]
            if isinstance(b, list):
                c, d = b
                return [lt, [a+c, 0]]

        return [lt, explode(a, b, depth+1)]
    else:
        return explode(lt, rt, depth+1)

def explode(left, right, depth):
    print(f"explode d={depth} lt={left} rt={right}")

    if isinstance(left, list):
        return explode(left[0], left[1], depth+1)

    if isinstance(right, list):
        return explode(right[0], right[1], depth+1)

    return [left, right], depth > 4

def reduce(num):
    a, b = num
    return explode(a, b, 1)

lines = input.split('\n')
for line in lines:
    x = json.loads(line)
    f = reduce(x)
    print(x)
    print(f)
    print()

