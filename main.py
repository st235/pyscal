import sys

from pyscal.interpreter import Interpreter

def __repl():
    while True:
        try:
            text = input("calc> ")
        except EOFError:
            break

        if not text:
            continue

        interpreter = Interpreter(text)
        result = interpreter.interpret()
        print(result)
        print(interpreter)

def __eval_file(file_name: str):
    with open(file_name, "r") as f:
        file = f.read()

        interpreter = Interpreter(file)
        result = interpreter.interpret()
        print(result)
        print(interpreter)

def main():
    if len(sys.argv) == 1:
        __repl()
    elif len(sys.argv) > 1:
        __eval_file(sys.argv[1])
    else:
        print("Usage: pyscal [filename]")

if __name__ == "__main__":
    main()
