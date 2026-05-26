from sly import Parser
from core.lexer import IniLexer

class IniParser(Parser):

    """
    Gramática:
        https://github.com/prantlf/fast-ini/blob/master/doc/grammar.md

        <file> ::= <section_list>
        <section_list> ::= section_list section | section
        <section> ::= <SECTION_NAME> <entrylist>
        <entrylist> ::= <entrylist> <entry> | <entry>
        <entry> ::= <KEY> <VALUE>
        
    """

    debugfile = 'parser.out'
    tokens = IniLexer.tokens

    def __init__(self):
        self.sections = {}
    
    # --------------------------------------------------
    # <file> ::= <section_list>
    # --------------------------------------------------
    @_('section_list') 
    def file(self, p):                
        return p.section_list    

    # --------------------------------------------------    
    # <section_list> ::= section_list section | section
    # --------------------------------------------------
    @_('section_list section')
    def section_list(self, p):        
        p.section_list.update(p.section)
        return p.section_list
    
    @_('section')
    def section_list(self, p):        
        return p.section

    # --------------------------------------------------   
    # <section> ::= <SECTION_NAME> <entrylist>
    # --------------------------------------------------
    @_('SECTION_NAME entrylist')
    def section(self, p):        
        section_name = p.SECTION_NAME.strip()
        return {section_name: p.entrylist}
        
    # --------------------------------------------------
    # <entrylist> ::= <entrylist> <entry> | <entry>
    # --------------------------------------------------
    @_('entrylist entry')
    def entrylist(self, p):
        p.entrylist.update(p.entry)
        return p.entrylist

    @_('entry')
    def entrylist(self, p):
        return p.entry

    # --------------------------------------------------
    # <entry> ::= <KEY> <VALUE>
    # --------------------------------------------------
    @_('KEY VALUE')
    def entry(self, p):        
        if p.VALUE.startswith('='):
            if p.VALUE.find('"') != -1 and p.VALUE[-1] == '"': # detecta valor com aspas duplas
                return {p.KEY: p.VALUE[p.VALUE.find('"')+1:-1]}
            
            return {p.KEY: p.VALUE[1:].strip()}
 
    def error(self, p):        
        if p:
            print(f"Erro de sintaxe: {p}")            
            
        else:
            print("Erro de sintaxe: fim de arquivo inesperado")