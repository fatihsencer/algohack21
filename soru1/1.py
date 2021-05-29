import string

text = input('Enter text: ')[::-1]

new_text = []

for x in text:

    if x in string.ascii_letters:

        if len(new_text) == 0:
            new_text.append(x)

        else:
            for y in new_text:

                if x in new_text:
                    continue

                else:
                    new_text.append(x)

print(''.join(new_text))
