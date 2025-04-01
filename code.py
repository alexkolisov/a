def run_code(code):

    translations = {
        "напечатать": "print",
        "считать число": "int(input())",
        "считать": "input()",
        "если нет": "else",
        "конец": "break",
        "если" : "if",
        "или": "elif",
        "всегда": "while True",
        "пока": "while",
        "для": "for",
        "в диапазоне": "in range",
        "макс": "max",
        "мин": "min",
        "рандом число": "random.randint",
        "импорт рандом": "import random",
    }

    for value in translations.values():
        code = code.replace(value, "")

    for key, value in translations.items():
        code = code.replace(key, value)

    exec(code)


file = open('code.a', 'r')
code = file.read()

if len(code) == 0:
    code = """"""
    if __name__ == "__main__":
        while True:
            cmd = input(">>> ")
            if cmd == "выход":
                break
            code = code + '\n' + cmd

run_code(code)
