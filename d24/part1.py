input = """inp w
add z w
mod z 2
div w 2
add y w
mod y 2
div w 2
add x w
mod x 2
div w 2
mod w 2"""

class ALU:
    def __init__(self, input):
        prog = []
        lines = input.split('\n')
        for line in lines:
            prog.append(line.split(' '))
        self.prog = prog
        self.w = 0
        self.x = 0
        self.y = 0
        self.z = 0

    def __repr__(self):
        return f"w={self.w} x={self.x} y={self.y} z={self.z}"

    def run(self, input):
        self.input = [x for x in str(input)]

        for p in self.prog:
            self.execute(p)
            print(self)
        return self.z == 0  

    def execute(self, p):
        op = p[0]
        reg = p[1]
        print(f"exec {op} on {reg}")

        if op == 'inp':
            self._inp(reg)
        else:
            b = p[2]
            if b in "wxyz":
                b = self._reg(b)
            else:
                b = int(b)

            if op == 'add':
                self._add(reg, b)
            elif op == 'mul':
                self._mul(reg, b)
            elif op == 'div':
                self._div(reg, b)
            elif op == 'mod':
                self._mod(reg, b)
            elif op == 'eql':
                self._eql(reg, b)              

    def _reg(self, reg):
        if reg == 'w':
            return self.w
        if reg == 'x':
            return self.x
        if reg == 'y':
            return self.y
        if reg == 'z':
            return self.z

    def _inp(self, reg):
        v = int(self.input.pop(0))
        print(f"inp {v} into {reg}")
        print(self.input)
        if reg == 'w':
            self.w = v
        elif reg == 'x':
            self.x = v
        elif reg == 'y':
            self.y = v
        elif reg == 'z':
            self.z = v

    def _add(self, reg, b):
        if reg == 'w':
            self.w += b
        elif reg == 'x':
            self.x += b
        elif reg == 'y':
            self.y += b
        elif reg == 'z':
            self.z += b

    def _mul(self, reg, b):
        if reg == 'w':
            self.w *= b
        elif reg == 'x':
            self.x *= b
        elif reg == 'y':
            self.y *= b
        elif reg == 'z':
            self.z *= b

    def _div(self, reg, b):
        if reg == 'w':
            self.w //= b
        elif reg == 'x':
            self.x //= b
        elif reg == 'y':
            self.y //= b
        elif reg == 'z':
            self.z //= b

    def _mod(self, reg, b):
        if reg == 'w':
            self.w %= b
        elif reg == 'x':
            self.x %= b
        elif reg == 'y':
            self.y %= b
        elif reg == 'z':
            self.z %= b

    def _eql(self, reg, b):
        if reg == 'w':
            self.w = 1 if self.w == b else 0
        elif reg == 'x':
            self.x = 1 if self.x == b else 0
        elif reg == 'y':
            self.y = 1 if self.y == b else 0
        elif reg == 'z':
            self.z = 1 if self.z == b else 0

input = open('data', 'r').read()
alu = ALU(input)
print(alu.prog)

valid = alu.run(13579246899999)
print(valid)
