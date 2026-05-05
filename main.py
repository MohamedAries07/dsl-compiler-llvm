from lexer import tokenize
from parser import Parser
from codegen import CodeGen

code = "3 + 5 * 2"

tokens = tokenize(code)
parser = Parser(tokens)
ast = parser.expr()

codegen = CodeGen()
result = codegen.generate(ast)
llvm_ir = codegen.finalize(result)

print("Generated LLVM IR:\n")
print(llvm_ir)