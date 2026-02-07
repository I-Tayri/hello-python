#!/usr/bin/env python3
"""Script simple pour apprendre les bases de Python."""

def greet(name: str) -> str:
    """Retourne un message de salutation."""
    return f"Bonjour, {name} ! Bienvenue en Python."

def main():
    print("=" * 40)
    print(greet("Amazigh"))
    print("=" * 40)
    
    # Exemple de boucle
    langages = ["Python", "JavaScript", "HTML", "CSS"]
    print("\nMes langages préférés :")
    for i, lang in enumerate(langages, 1):
        print(f"  {i}. {lang}")

if __name__ == "__main__":
    main()
