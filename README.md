# calculator_rpn
calculatrice en notation polonaise inversée (RPN)

https://fr.wikipedia.org/wiki/Notation_polonaise_inverse

## Description

Ce projet implémente une calculatrice utilisant la notation polonaise inversée (Reverse Polish Notation - RPN). La calculatrice permet d’évaluer des expressions mathématiques sous forme de liste de tokens en notation RPN.

La notation polonaise inversée élimine le besoin de parenthèses en plaçant l’opérateur après ses opérandes. Par exemple, l’expression classique `(3 + 4) * 5` s’écrit en RPN : `3 4 + 5 *`.

## Fonctionnalités

Cette calculatrice supporte les opérations suivantes :

- `+` : addition
- `-` : soustraction
- `*` : multiplication
- `/` : division
- `%` : modulo (division avec reste)
- `^` : puissance
- `!` : factoriel

## Installation

1. Cloner le dépôt :

```bash
git clone https://github.com/ahmadoubahnini/calculator_rpn.git
cd calculator_rpn
