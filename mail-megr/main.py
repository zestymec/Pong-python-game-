place_holder = "[name]"

with open("/Users/apple/umeraziz/Pong-python-game-/mail-megr/Input/Names/invited_names.txt", "r") as names_file:
    names_lines = names_file.readlines()

with open("/Users/apple/umeraziz/Pong-python-game-/mail-megr/Input/Letters/starting_letter.txt", "r") as letter_file:
    letters_contents = letter_file.read()

for name in names_lines:
    stripped_name = name.strip()
    new_letter = letters_contents.replace(place_holder, stripped_name)

    output_file = f"/Users/apple/umeraziz/Pong-python-game-/mail-megr/Output/ReadyToSend/letter_for_{stripped_name}.docx"

    with open(output_file, mode="w") as completed_letter:
        completed_letter.write(new_letter)
