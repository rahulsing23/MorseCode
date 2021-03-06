MORSE_CODE_DICT = { 'A':'|^|' , 'B':'|-]' ,   'C':'<('  ,
                    'D':'|>'  , 'E':'[-'  ,   'F':'|='  ,
                    'G':'(-|' , 'H':'|-|' ,   'I':'!'   ,
                    'J':'~?'  , 'K':'|<'  ,   'L':'|_'  ,
                    'M':'|\/|', 'N':'|\|' ,   'O':'()'  ,
                    'P':'|*'  , 'Q':'[]_' ,   'R':'|\*' ,
                    'S':'&'   , 'T':'-|-' ,   'U':'|_|' ,
                    'V':'\/'  , 'W':'\/\/',   'X':')('  ,
                    'Y':'\|/' , 'Z':'-/_' ,   '1':'I'   ,
                    '2':'Z'   , '3':'E'   ,   '4':'Y'   ,
                    '5':'S'   , '6':'b'   ,   '7':'F'   ,
                    '8':'B'   , '9':'G'   ,   '0':'O'}
def encrypt(message):
    CODE = ''
    for letter in message:
        if letter != ' ':
            CODE += MORSE_CODE_DICT[letter] + ' '
        else:
            CODE += ' '
  
    return CODE

def decrypt(message):
    message += ' '
    DECODE = ''
    TEXT = ''
    for letter in message:
        if (letter != ' '):
            i = 0
            TEXT += letter
  
        else:
            i += 1
            if i == 2 :
                DECODE += ' '
            else:
                DECODE += list(MORSE_CODE_DICT.keys())[list(MORSE_CODE_DICT
                .values()).index(TEXT)]
                TEXT = ''
  
    return DECODE
def main():
    message = input("Press any text")
    result = encrypt(message.upper())
    print (result)
    
    message = "|-| ! ~? |^| <( |< [- |>"
    result = decrypt(message)
    print (result)
   
  
if __name__ == '__main__':
    main()    
