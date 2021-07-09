val = "coding is great"

for letter in val:
    if letter == 'i':
        continue  # continue goes back to loop
    print(letter)

for letter in val:
    if letter == 'i':
        pass  # pass does nothing
    print(letter)

for letter in val:
    if letter == 'i':
        break  # break breaks the loop
    print(letter)
