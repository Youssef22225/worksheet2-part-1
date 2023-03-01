from BinarySearchTree import BinarySearchTree

def generate_morse_tree():

    tree = BinarySearchTree()

    # 0 level
    tree[320] = "start"

    # 1st Level
    tree[160] = "E"
    tree[480] = "T"

    # 2nd Level
    tree[80] = "I"
    tree[240] = "A"
    tree[400] = "N"
    tree[560] = "M"

    # 3rd Level
    tree[40] = "S"
    tree[120] = "U"
    tree[200] = "R"
    tree[280] = "W"

    tree[360] = "D"
    tree[440] = "K"
    tree[520] = "G"
    tree[600] = "O"

    # 4th Level
    tree[20] = "H"
    tree[60] = "V"
    tree[100] = "F"
    tree[140] = ""
    tree[180] = "L"
    tree[220] = ""
    tree[260] = "P"
    tree[300] = "J"

    tree[340] = "B"
    tree[380] = "X"
    tree[420] = "C"
    tree[460] = "Y"
    tree[500] = "Z"
    tree[540] = "Q"
    tree[580] = ""
    tree[620] = ""

    # 5th Level
    tree[10] = "5"
    tree[30] = "4"
    tree[50] = ""
    tree[70] = "3"
    tree[90] = ""
    tree[110] = "¿"
    tree[130] = "?"
    tree[150] = "2"

    tree[170] = "&"
    tree[190] = ""
    tree[210] = "+"
    tree[230] = ""
    tree[250] = ""
    tree[270] = ""
    tree[290] = ""
    tree[310] = "1"

    tree[330] = "6"
    tree[350] = "="
    tree[370] = "/"
    tree[390] = ""
    tree[410] = ""
    tree[430] = ""
    tree[450] = "("
    tree[470] = ""

    tree[490] = "7"
    tree[510] = ""
    tree[530] = ""
    tree[550] = ""
    tree[570] = "8"
    tree[590] = ""
    tree[610] = "9"
    tree[630] = "0"

    # 6th Level
    tree[45] = ""
    tree[135] = "_"
    tree[185] = '"'
    tree[215] = "."
    tree[305] = "'"
    tree[335] = "-"
    tree[425] = ";"
    tree[435] = "!"
    tree[455] = "("
    tree[495] = "¡"
    tree[515] = ","
    tree[565] = ":"

    # 7th Level
    tree[46] = "$"

    return tree


morse_code_tree = generate_morse_tree()


def encode(msg: str) -> str:
    msg = msg.upper().strip().split()
    morseCode = ""

    for word in msg:
        wordMorseCode = ""
        for char in word:
            char_code = []
            getMorseCode(morse_code_tree.root, char, char_code)
            code = "".join(char_code)
            wordMorseCode = wordMorseCode + code + " "
        
        wordMorseCode = wordMorseCode.strip()
        morseCode = morseCode + wordMorseCode + " / "

    return morseCode.strip().rsplit('/', 1)[0].strip()


def getMorseCode(node, character, code):
  
    if node == None:
        return False
  
    elif node.payload == character:
  
        return True
  
    else:  

        if getMorseCode(node.leftChild, character, code) == True:
      
            code.insert(0, ".")
            return True
    
        elif getMorseCode(node.rightChild, character, code) == True:
      
            code.insert(0, "-")
            return True

    return False


def decode(msg: str) -> str:
    message = ""
    coded_letters = msg.split(" ")
    
    for coded_letter in coded_letters:
        current_node = morse_code_tree.root
        
        for char in coded_letter:
            
            if char == '.' :
                current_node = current_node.leftChild
            elif char == '-':
                current_node = current_node.rightChild

        letter = current_node.payload

        if coded_letter == '/':
            message = message + ' '
        else:
            message = message + letter

    return message.lower()
