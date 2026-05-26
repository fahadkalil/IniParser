from core.lexer import IniLexer
from core.parser import IniParser
import json

if __name__ == '__main__':

    lexer = IniLexer()
    parser = IniParser()    
    
    #
    # testando o arquivo 'test_file.ini'
    #
    with open("test_file.ini", "r", encoding="utf-8") as file:
        text = file.read() 

    debug_token_list = True

    if text:            
        if debug_token_list is True:
            for token in lexer.tokenize(text):
                print('type=%r, value=%r' % (token.type, token.value))            
            
        result = parser.parse(lexer.tokenize(text)) 
        print("----------------------------")
        if result is None:
            print("Sintaxe inválida!")
        else:
            print("Sintaxe Válida!")
            print(json.dumps(result, indent=2, ensure_ascii=False))



