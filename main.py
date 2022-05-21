# HAND LANGUAGE INTERPRETER

# author: wilberquito

def clamp(cell_value):
    if (cell_value < 0):
        return 255
    elif (cell_value > 255):
        return 0
    else:
        return cell_value
    
def tape_needs_space(tape, tape_pointer):
    return len (tape) <= tape_pointer + 1

def in_tape_origin(tape_pointer):
    return tape_pointer == 0
    
def interpreter_completed(hand_code, hand_code_pointer):
    return len (hand_code) <= hand_code_pointer

def should_jump_front(tape, tape_pointer):
    return tape[tape_pointer] == 0

def should_jump_back(tape, tape_pointer):
    return tape[tape_pointer] != 0

def nested_position_jump(emojies, emoji):
    matches, index = 1, 0
    for candidate in emojies:
        if candidate == '🤛' or candidate == '🤜':
            matches += 1 if candidate == emoji else -1
        index += 1
        if matches == 0:
            break
    return index

def jump_front(hand_code, hand_code_pointer):
    future = hand_code[hand_code_pointer + 1:]
    return hand_code_pointer + nested_position_jump(future, '🤜')
                
def jump_back(hand_code, hand_code_pointer):
    history = hand_code[:hand_code_pointer]
    history.reverse()
    return len( history ) - nested_position_jump(history, '🤛')

def memory_handler(tape, tape_pointer, command):
    match command:
        case '👉':
            if tape_needs_space(tape, tape_pointer):
                tape.append(0)
            return (tape, tape_pointer + 1)
        case '👈':
            if (not in_tape_origin(tape_pointer)):
                return (tape, tape_pointer - 1)
        case '👆':
            tape[tape_pointer] = clamp(tape[tape_pointer] + 1)
        case '👇':
            tape[tape_pointer] = clamp(tape[tape_pointer] - 1)
        case _:
            raise Exception('unsupported command')
        
    return (tape, tape_pointer)

def interpreter(hand_code):
    tape = [0]
    tape_pointer = 0
    hand_code_pointer = 0
    
    message = []

    while not interpreter_completed(hand_code, hand_code_pointer):
        
        command = hand_code[hand_code_pointer]

        match command:
            case '🤜':
                if (should_jump_front(tape, tape_pointer)):
                    hand_code_pointer = jump_front(hand_code, hand_code_pointer)
            case '🤛':
                if (should_jump_back(tape, tape_pointer)):
                    hand_code_pointer = jump_back(hand_code, hand_code_pointer)
            case '👊':
                char = chr(tape[tape_pointer])
                message.append(char)
            case alloc:
                tape, tape_pointer = memory_handler(tape, tape_pointer, alloc)

        hand_code_pointer += 1
        
        # print (f"tape: {tape}", f"tape_pointer: {tape_pointer}", f"hand_code_pointer: {hand_code_pointer}")
        
    print (''.join(message))
    

with open('input.hand', encoding='utf-8') as f:
    hand_code = list(f.read())
    
interpreter(hand_code)
