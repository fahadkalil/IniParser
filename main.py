from core.lexer import IniLexer
from core.parser import IniParser
import json

if __name__ == '__main__':

    lexer = IniLexer()
    parser = IniParser()    

    text = '''; last modified 1 April 2001 by John Doe
[owner]
name = John Doe
organization = Acme Widgets Inc.

[database]
; use IP address in case network name resolution is not working
server = 192.0.2.62     
port = 143
file = "payroll.dat"
'''

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



