from pathlib import Path


direct = "C:\\Users\\A1\\Desktop\\MY_Draft"

def display_tree(path: Path, indent: str = " ") -> None:
    print(indent + str(path.name))

    if path.is_dir():
        for child in path.iterdir():
            display_tree(child, indent + "    ")


if __name__ == "__main__":
    root = Path(direct)
    display_tree(root)
