place_holder = "[name]"


f = open("Mail Merge Project Start/Input/Names/invited_names.txt", "r")
Names_lines = f.readlines()
print(Names_lines)

with open("./Input/Letters/starting_letter.decx") as letter_file:
    letters_contents = letter_file.read()


    