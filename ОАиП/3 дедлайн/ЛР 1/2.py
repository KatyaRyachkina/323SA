def make_bold(func):
    def wrapper():
        result = func()
        return f"<b>{result}</b>"
    return wrapper

@make_bold
def get_text():
    return "Hello, World!"

if __name__ == "__main__":
    print(get_text())
