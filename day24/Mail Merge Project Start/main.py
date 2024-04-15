NAMES_FILE_PATH = "day24/Mail Merge Project Start/Input/Names/invited_names.txt"
LETTER_FILE_PATH = "day24/Mail Merge Project Start/Input/Letters/starting_letter.txt"
FILE_PATH_TO_CREATE_LETTER = (
    "day24/Mail Merge Project Start/Output/ReadyToSend/example.txt"
)

def file_reader(file_path: str) -> list:
    with open(file_path, mode="r") as file_to_read:
        return [i for i in file_to_read]


def write_file(
    file_path_to_save: str,
    input_data: str,
) -> None:
    with open(file_path_to_save, mode="w") as file_to_save:
        file_to_save.write(input_data)


names: list = file_reader(NAMES_FILE_PATH)
letter: list = file_reader(LETTER_FILE_PATH)

for name in names:
    composed_letter = ""
    for line in letter:
        if "[name]" in line:
            composed_letter += line.replace("[name],", name.strip() + ",")
        else:
            composed_letter += line
    write_file(
        f"day24/Mail Merge Project Start/Output/ReadyToSend/letter_for_{name}.txt",
        composed_letter.strip(),
    )
