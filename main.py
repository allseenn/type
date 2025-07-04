import typer

def main(name: str, lastname: str = "", formal: bool = False):
    """
    Say hi to NAME, optionally with a --lastname.

    If --formal is used, say hi very formally.
    """

    if formal:
        print(f"Hello Ms. {name} {lastname}")
    else:
        print(f"Hi {name} {lastname}")

if __name__ == "__main__":
    typer.run(main)
