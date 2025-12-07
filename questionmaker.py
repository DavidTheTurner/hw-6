from pathlib import Path
from typing import Generator


def main():

    question_nums: list[int] = list(i for i in range(1, 6))

    questions_dir: Path = Path("./questions")
    for question_num in question_nums:
        question_num_dir: Path = questions_dir / f"b{question_num}"
        question_num_dir.mkdir(exist_ok=True)

        question_parts: Path = question_num_dir / "parts"
        question_parts.mkdir(exist_ok=True)

        question_tex: Path = question_num_dir / f"b{question_num}.tex"
        question_tex.touch()


def _get_letter_gen() -> Generator[str]:
    def _generator():
        alphabet: str = "abcdefghijklmnopqrstuvwxyz"
        for letter in alphabet:
            yield letter
    return _generator()


def make_parts(question_num: int, num_parts: int):

    parts_dir: Path = Path(f"./questions/b{question_num}/parts")

    import_str: str = ""
    for part_num in range(1, num_parts + 1):
        part_file: Path = parts_dir / f"{part_num}.tex"
        part_file.touch()
        part_file.write_text(f"\\question{{(B{question_num}.{part_num})}}{{\n}}")

        rel_path: Path = part_file.relative_to("./questions")
        part_import: str = f"\\import{{{str(rel_path.parent)}}}{{{rel_path.name}}}\n"
        import_str += part_import

    print(import_str)


if __name__ == "__main__":
    # main()
    make_parts(5, 3)
