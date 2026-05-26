from sly import Lexer

class IniLexer(Lexer):
    tokens = {SECTION_NAME, KEY, VALUE}

    ignore_comment = r';[^\n]*'
    ignore = '\t'
    
    #COMMENT = r';.*\n'
    
    SECTION_NAME = r'\[[a-zA-Z0-9 \./]+\]'

    # deve aparecer antes do VALUE
    KEY = r'[a-zA-Z_][\w.\-]*'

    @_(r'[^=\n;][^\n]*')
    def VALUE(self, t):        
        t.value = t.value.strip()
        #if t.value.startswith('= '):
        #    t.value = t.value.replace('= ', '')
        return t

    @_(r'\n+')
    def newline(self, t):
        self.lineno += len(t.value)

    def error(self, t):
        print("Caractere ilegal {}".format(t.value[0]))
        self.index +=1
