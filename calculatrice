import math

class ErreurPileVide(Exception):
    """Exception si la pile est vide ou insuffisante."""
    pass

class ErreurDivisionParZero(Exception):
    """Exception pour division par zéro."""
    pass

class Calculatrice:
    def __init__(self):
        self.pile = []

    def empiler(self, valeur: int):
        self.pile.append(valeur)

    def depiler(self) -> int:
        if not self.pile:
            raise ErreurPileVide("Pile vide")
        return self.pile.pop()

    def addition(self):
        b, a = self.depiler(), self.depiler()
        self.empiler(a + b)

    def soustraction(self):
        b, a = self.depiler(), self.depiler()
        self.empiler(a - b)

    def multiplication(self):
        b, a = self.depiler(), self.depiler()
        self.empiler(a * b)

    def division(self):
        b, a = self.depiler(), self.depiler()
        if b == 0:
            raise ErreurDivisionParZero("Division par zéro interdite")
        self.empiler(a // b)

    def modulo(self):
        b, a = self.depiler(), self.depiler()
        self.empiler(a % b)

    def puissance(self):
        b, a = self.depiler(), self.depiler()
        self.empiler(pow(a, b))

    def factoriel(self):
        a = self.depiler()
        if a < 0:
            raise ValueError("Factoriel non défini pour les nombres négatifs")
        self.empiler(math.factorial(a))

    def evaluer(self, tokens):
        """Évaluer une expression en notation polonaise inversée (liste de tokens)."""
        operations = {
            "+": self.addition,
            "-": self.soustraction,
            "*": self.multiplication,
            "/": self.division,
            "%": self.modulo,
            "^": self.puissance,
            "!": self.factoriel,
        }
        for token in tokens:
            if token.isdigit() or (token.startswith("-") and token[1:].isdigit()):
                self.empiler(int(token))
            elif token in operations:
                operations[token]()
            else:
                raise ValueError(f"Opération inconnue : {token}")
        return self.pile[-1] if self.pile else None
