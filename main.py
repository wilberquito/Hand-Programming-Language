import hpl

if __name__ == "__main__":
    with open('test2.hand', encoding='utf-8') as f:
        hand_code = list(f.read())
    message = hpl.interpreter(hand_code)
    print(message)