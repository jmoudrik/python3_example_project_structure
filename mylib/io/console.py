def println(text):
    print(text)


def boxed(text):
    n = 4 + len(str(text))
    println("=" * n)
    println(f"= {text} =")
    println("=" * n)
