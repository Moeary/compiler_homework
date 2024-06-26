
# parsetab.py
# This file is automatically generated. Do not edit.
# pylint: disable=W,C,R
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = 'COMMA DIVIDE EQUALS FLOAT ID INT LPAREN MINUS MOD PLUS RPAREN SEMICOLON TIMESprogram : declaration_list statement_listdeclaration_list : declaration declaration_list\n                       | declarationdeclaration : INT L SEMICOLON\n                   | FLOAT L SEMICOLONL : ID RR : COMMA ID R\n       | statement_list : statement statement_list\n                      | statementstatement : E SEMICOLONE : ID EQUALS EE : E PLUS TE : E MINUS TE : TT : T TIMES FT : T DIVIDE FT : T MOD FT : FF : LPAREN E RPARENF : ID'
    
_lr_action_items = {'INT':([0,3,26,29,],[4,4,-4,-5,]),'FLOAT':([0,3,26,29,],[5,5,-4,-5,]),'$end':([1,6,7,17,18,],[0,-1,-10,-9,-11,]),'ID':([2,3,4,5,7,12,13,18,19,20,21,22,23,24,26,28,29,],[9,-3,15,15,9,9,-2,-11,31,31,9,31,31,31,-4,38,-5,]),'LPAREN':([2,3,7,12,13,18,19,20,21,22,23,24,26,29,],[12,-3,12,12,-2,-11,12,12,12,12,12,12,-4,-5,]),'SEMICOLON':([8,9,10,11,14,15,16,27,30,31,32,33,34,35,36,37,38,39,],[18,-21,-15,-19,26,-8,29,-6,-13,-21,-14,-12,-16,-17,-18,-20,-8,-7,]),'PLUS':([8,9,10,11,25,30,31,32,33,34,35,36,37,],[19,-21,-15,-19,19,-13,-21,-14,19,-16,-17,-18,-20,]),'MINUS':([8,9,10,11,25,30,31,32,33,34,35,36,37,],[20,-21,-15,-19,20,-13,-21,-14,20,-16,-17,-18,-20,]),'EQUALS':([9,],[21,]),'TIMES':([9,10,11,30,31,32,34,35,36,37,],[-21,22,-19,22,-21,22,-16,-17,-18,-20,]),'DIVIDE':([9,10,11,30,31,32,34,35,36,37,],[-21,23,-19,23,-21,23,-16,-17,-18,-20,]),'MOD':([9,10,11,30,31,32,34,35,36,37,],[-21,24,-19,24,-21,24,-16,-17,-18,-20,]),'RPAREN':([9,10,11,25,30,31,32,33,34,35,36,37,],[-21,-15,-19,37,-13,-21,-14,-12,-16,-17,-18,-20,]),'COMMA':([15,38,],[28,28,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'program':([0,],[1,]),'declaration_list':([0,3,],[2,13,]),'declaration':([0,3,],[3,3,]),'statement_list':([2,7,],[6,17,]),'statement':([2,7,],[7,7,]),'E':([2,7,12,21,],[8,8,25,33,]),'T':([2,7,12,19,20,21,],[10,10,10,30,32,10,]),'F':([2,7,12,19,20,21,22,23,24,],[11,11,11,11,11,11,34,35,36,]),'L':([4,5,],[14,16,]),'R':([15,38,],[27,39,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> program","S'",1,None,None,None),
  ('program -> declaration_list statement_list','program',2,'p_program','G2_G3_Parse.py',73),
  ('declaration_list -> declaration declaration_list','declaration_list',2,'p_declaration_list','G2_G3_Parse.py',77),
  ('declaration_list -> declaration','declaration_list',1,'p_declaration_list','G2_G3_Parse.py',78),
  ('declaration -> INT L SEMICOLON','declaration',3,'p_declaration','G2_G3_Parse.py',82),
  ('declaration -> FLOAT L SEMICOLON','declaration',3,'p_declaration','G2_G3_Parse.py',83),
  ('L -> ID R','L',2,'p_L','G2_G3_Parse.py',89),
  ('R -> COMMA ID R','R',3,'p_R','G2_G3_Parse.py',93),
  ('R -> <empty>','R',0,'p_R','G2_G3_Parse.py',94),
  ('statement_list -> statement statement_list','statement_list',2,'p_statement_list','G2_G3_Parse.py',101),
  ('statement_list -> statement','statement_list',1,'p_statement_list','G2_G3_Parse.py',102),
  ('statement -> E SEMICOLON','statement',2,'p_statement','G2_G3_Parse.py',106),
  ('E -> ID EQUALS E','E',3,'p_E_assign','G2_G3_Parse.py',110),
  ('E -> E PLUS T','E',3,'p_E_plus','G2_G3_Parse.py',117),
  ('E -> E MINUS T','E',3,'p_E_minus','G2_G3_Parse.py',123),
  ('E -> T','E',1,'p_E_T','G2_G3_Parse.py',129),
  ('T -> T TIMES F','T',3,'p_T_times','G2_G3_Parse.py',133),
  ('T -> T DIVIDE F','T',3,'p_T_divide','G2_G3_Parse.py',139),
  ('T -> T MOD F','T',3,'p_T_mod','G2_G3_Parse.py',145),
  ('T -> F','T',1,'p_T_F','G2_G3_Parse.py',151),
  ('F -> LPAREN E RPAREN','F',3,'p_F_paren','G2_G3_Parse.py',155),
  ('F -> ID','F',1,'p_F_id','G2_G3_Parse.py',159),
]
