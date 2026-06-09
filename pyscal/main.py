from pyscal.interpreter import Interpreter

def main():
    while True:
        try:
            text = input("calc> ")
        except EOFError:
            break

        if not text:
            continue

        interpreter = Interpreter(text)
        result = interpreter.expr()
        print(result)
        print(interpreter)

if __name__ == "__main__":
    main()
