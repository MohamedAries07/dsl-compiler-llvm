# dsl-compiler-llvm
# 🚀 DSL Compiler using LLVM (End-to-End)

A fully functional **Domain-Specific Language (DSL) Compiler** built from scratch using Python and LLVM infrastructure.
This project demonstrates the complete compilation pipeline from **source code → tokens → AST → LLVM IR**.

---

## 🧠 Project Overview

This compiler translates a simple custom language into **LLVM Intermediate Representation (IR)** using `llvmlite`.
It simulates how real-world compilers like GCC/Clang work internally, but in a simplified and educational form.

---

## 🔥 Features

* ✅ Lexical Analysis (Tokenization)
* ✅ Syntax Parsing (Recursive Descent Parser)
* ✅ Abstract Syntax Tree (AST) Generation
* ✅ LLVM IR Code Generation
* ✅ Operator Precedence Handling
* ✅ Modular Compiler Architecture
* ⚡ Lightweight and fast execution

---

## ⚙️ Compiler Pipeline

```text
Source Code
   ↓
Lexer (Tokenization)
   ↓
Parser (Syntax Analysis)
   ↓
AST (Abstract Syntax Tree)
   ↓
Code Generator
   ↓
LLVM IR Output
```

---

## 🧪 Example

### Input DSL Code:

```python
3 + 5 * 2
```

### Generated LLVM IR:

```llvm
define i32 @"main"()
{
entry:
  %".2" = mul i32 5, 2
  %".3" = add i32 3, %".2"
  ret i32 %".3"
}
```

---

## 📂 Project Structure

```
dsl-compiler/
│── lexer.py        # Tokenization logic
│── parser.py       # Syntax parsing (recursive descent)
│── ast_nodes.py    # AST node definitions
│── codegen.py      # LLVM IR generation
│── main.py         # Entry point
```

---

## 🛠️ Tech Stack

* **Python 3**
* **llvmlite** (LLVM binding for Python)
* **LLVM IR**

---

## 📦 Installation

```bash
pip install llvmlite
```

---

## ▶️ How to Run

```bash
python main.py
```

---

## 🧠 Concepts Used

* Compiler Design Fundamentals
* Finite Automata (Lexical Analysis)
* Recursive Descent Parsing
* Abstract Syntax Trees (AST)
* Intermediate Representation (IR)
* LLVM Backend Concepts

---

## 🚀 Future Improvements

* 🔹 Variable support (`a = 10`)
* 🔹 Conditional statements (`if-else`)
* 🔹 Loop constructs (`while`, `for`)
* 🔹 Function definitions
* 🔹 Optimization techniques (constant folding)
* 🔹 Direct machine code generation using LLVM `llc`

---

## 🎯 Use Cases

* Educational compiler design projects
* Understanding LLVM architecture
* Building custom programming languages
* Research & academic demonstrations

---

## 📸 Demo (Optional)

> Add your VS Code screenshots here for better presentation

---

## 🧑‍💻 Author

**Your Name**
B.Tech AI & ML
Passionate about Systems, AI, and Cybersecurity

---

## ⭐ Why This Project Matters

This project showcases:

* Strong understanding of **compiler internals**
* Ability to build **end-to-end systems**
* Practical use of **LLVM infrastructure**
* Clean modular software engineering design

---

## 📜 License

This project is open-source and available for educational use.

