from llvmlite import ir

class CodeGen:
    def __init__(self):
        self.module = ir.Module(name="dsl_module")
        self.builder = None

        func_type = ir.FunctionType(ir.IntType(32), [])
        self.function = ir.Function(self.module, func_type, name="main")

        block = self.function.append_basic_block(name="entry")
        self.builder = ir.IRBuilder(block)

    def generate(self, node):
        if type(node).__name__ == 'Number':
            return ir.Constant(ir.IntType(32), node.value)

        elif type(node).__name__ == 'BinOp':
            left = self.generate(node.left)
            right = self.generate(node.right)

            if node.op == '+':
                return self.builder.add(left, right)
            elif node.op == '-':
                return self.builder.sub(left, right)
            elif node.op == '*':
                return self.builder.mul(left, right)
            elif node.op == '/':
                return self.builder.sdiv(left, right)

    def finalize(self, value):
        self.builder.ret(value)
        return str(self.module)