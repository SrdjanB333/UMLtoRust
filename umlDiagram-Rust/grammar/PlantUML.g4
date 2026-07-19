grammar PlantUML;

program: STARTUML classDeclaration+ ENDUML EOF;

classDeclaration: CLASS ID LBRACE member* RBRACE;

member: attribute
      | method
      ; 

attribute: visibility? ID ':' type;
method: visibility? ID LPAREN parametarList? RPAREN (':' type)?;

visibility: PLUS
          | MINUS
          | HASH
          ;

parametar: ID ':' type;

parametarList: parametar
             | parametar (COMMA parametar)*
             ;

type: ID;

STARTUML: '@startuml';
ENDUML: '@enduml';
CLASS: 'class';
LBRACE: '{';
RBRACE: '}';
PLUS: '+';
MINUS: '-';
HASH: '#';
LPAREN: '(';
RPAREN: ')';
COMMA: ',';


ID: [a-zA-Z_][a-zA-Z0-9_]*;
WS: [ \t\r\n]+ -> skip;