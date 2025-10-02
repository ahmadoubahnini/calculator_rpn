from calculatrice import Calculatrice

def main():
    calc = Calculatrice()
    print("=== Calculatrice RPN (notation polonaise inversée) ===")
    print("Entrez une expression en notation polonaise inversée (ex: '3 4 +').")
    print("Tapez 'quitter' pour sortir.")

    while True:
        entree = input("> ")
        if entree.lower() in ["quitter", "exit"]:
            break
        try:
            tokens = entree.split()
            resultat = calc.evaluer(tokens)
            print("Résultat:", resultat)
        except Exception as e:
            print("Erreur:", e)

if __name__ == "__main__":
    main()
