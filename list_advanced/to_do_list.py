to_do_notes = ['' for el in range(10)]

while True:
    note = input()
    if note == 'End':
        break
    note_list = note.split('-')
    idx = int(note_list[0]) - 1
    action = note_list[1]

    to_do_notes[idx] = action


print([n for n in to_do_notes if not n == ''])