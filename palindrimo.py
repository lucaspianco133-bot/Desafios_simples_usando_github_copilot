def inverte_string(s):
    return s[::-1]


if __name__ == "__main__":
    s = input("Digite uma string: ")
    print("Invertida:", inverte_string(s))
    s_clean = ''.join(ch.lower() for ch in s if ch.isalnum())
    print("É palíndromo?", "Sim" if s_clean == s_clean[::-1] else "Não")
