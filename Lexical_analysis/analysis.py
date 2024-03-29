import os
import re
import string

KEYWORDS = ['if', 'then', 'else', 'int', 'char', 'for']
SEPARATORS = [',', ';', '"']
OPERATORS = ['=', '>=', '==', '+', '/', '%', '++']
CONSTVAL = []
VAL = []

def set_code(string_s):
    # 删除注释
    string_s = re.sub(r'#.*', '', string_s)
    # 删除空白行和额外的空格
    string_s = '\n'.join(line.strip() for line in string_s.split('\n') if line.strip())
    return string_s

def collect_constants_and_variables(code):
    tokens = re.findall(r'\b[a-zA-Z]\w{0,9}\b|\S', code.lower())
    for token in tokens:
        if re.match(r'\d+', token) and token not in CONSTVAL:
            CONSTVAL.append(token)
        elif re.match(r'[a-zA-Z]\w*', token) and token not in KEYWORDS and token not in VAL and token != 'over':
            VAL.append(token)

def lexical_analysis(code):
    tokens = re.findall(r'\b[a-zA-Z]\w{0,9}\b|<=|>=|==|\S', code.lower())
    symbol_table = []
    for token in tokens:
        if token == 'over':
            break
        elif token in KEYWORDS:
            symbol_table.append((token, '壹' + str(KEYWORDS.index(token))))
        elif token in CONSTVAL:
            symbol_table.append((token, '肆' + str(CONSTVAL.index(token))))
        elif token in OPERATORS:
            symbol_table.append((token, '叁' + str(OPERATORS.index(token))))
        elif token in SEPARATORS:
            symbol_table.append((token, '贰' + str(SEPARATORS.index(token))))
        elif token in VAL:
            symbol_table.append((token, '伍' + str(VAL.index(token))))
        else:
            symbol_table.append((token, 'err'))
    return symbol_table

code = """
for (i=1;i<=100;i++)
{     printf("%d ", i );  
}
over
"""

if __name__ == "__main__":
    code = set_code(code)
    collect_constants_and_variables(code)
    symbol_table = lexical_analysis(code)
    for token, kind in symbol_table:
        if(token=="over"):
            print("over")
            break
        print(f'{token}\t{kind}')
    print("常数表中的内容为：", ', '.join(CONSTVAL))
    print("变量表（标识符表）中的内容为：", ', '.join(VAL))