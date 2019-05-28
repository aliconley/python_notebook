from datetime import date



"""
Note Book app

Notes will have three parts:
ID
Content
Date/Time
"""

counter = 1
notebook = []
now = date.today()


while counter <= 5:
    content = input("what is the note? \n>")
    note_id = counter
    note = (note_id, str(now), content)
    counter += 1
    notebook.append(note)
    print(notebook)