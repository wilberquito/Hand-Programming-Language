# Hand Programming Language Interpreter
# author: wilberquito

def interpreter(code):
    tape = [0]
    tape_pointer = 0
    code_pointer = 0
    
    message = []

    while not completed(code, code_pointer):
        cmd = code[code_pointer]
        match cmd:
            case '🤜':
                if (should_jump_front(tape, tape_pointer)):
                    code_pointer = jump_front(code, code_pointer)
            case '🤛':
                if (should_jump_back(tape, tape_pointer)):
                    code_pointer = jump_back(code, code_pointer)
            case '👊':
                char = chr(tape[tape_pointer])
                message.append(char)
            case alloc:
                tape, tape_pointer = memory_handler(tape, tape_pointer, alloc)

        code_pointer += 1
        
        # print (f"tape: {tape}", f"tape_pointer: {tape_pointer}", f"code_pointer: {code_pointer}")
        
    return ''.join(message)

def completed(code, code_pointer):
    return len (code) <= code_pointer

def should_jump_front(tape, tape_pointer):
    return tape[tape_pointer] == 0

def should_jump_back(tape, tape_pointer):
    return tape[tape_pointer] != 0

def jump_front(code, code_pointer):
    future = code[code_pointer + 1:]
    return code_pointer + nested_position_jump(future, '🤜')
                
def jump_back(code, code_pointer):
    history = code[:code_pointer]
    history.reverse()
    return len( history ) - nested_position_jump(history, '🤛')

def memory_handler(tape, tape_pointer, cmd):
    match cmd:
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
            raise Exception('unsupported cmd')
        
    return (tape, tape_pointer)

def nested_position_jump(emojies, emoji):
    matches, index = 1, 0
    for candidate in emojies:
        if candidate == '🤛' or candidate == '🤜':
            matches += 1 if candidate == emoji else -1
        index += 1
        if matches == 0:
            break
    return index    

def tape_needs_space(tape, tape_pointer):
    return len (tape) <= tape_pointer + 1

def in_tape_origin(tape_pointer):
    return tape_pointer == 0

def clamp(cell_value):
    if (cell_value < 0):
        return 255
    elif (cell_value > 255):
        return 0
    else:
        return cell_value
