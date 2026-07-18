grammar PlantUML;

program: STARTUML classDeclaration+ ENDUML EOF;

classDeclaration: CLASS ID LBRACE member* RBRACE;

member: attribute
      | method
      ; 

attribute: visibility ID ':' type;

visibility: PLUS
            | MINUS
            | HASH
            ;

type: 'String'
    | 'int'
    | 'bool'
    | 'float'
    ;

STARTUML: '@startuml';
ENDUML: '@enduml';
CLASS: 'class';
LBRACE: '{';
RBRACE: '}';
PLUS: '+';
MINUS: '-';
HASH: '#';


ID: [a-zA-Z_][a-zA-Z0-9_]*;
WS: [ \t\r\n]+ -> skip;