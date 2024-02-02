

def echo(text: str, repetitions: int = 3) -> str:
    """Imitate a real-world echo."""
    echo = ""

    for i in range(repetitions):
        echo += text + "\n"
        text = text[:-1]

    return echo

if __name__ == "__main__":
    text = input("Yell something at a mountain: ")
    print(echo(text))