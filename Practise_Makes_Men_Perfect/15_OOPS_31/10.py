# Exercise 10: Notebook Class with Add & Display Notes
# Problem Statement: Write a Python program to create a Notebook class that maintains an internal list of notes. Add an add_note(note) method that appends a new note to the list, and a show_notes() method that prints all stored notes.

class Notebook:
    def __init__(self,notes):
        self.notes=notes 
    def add_note(self,note):
        self.notes.append(note)
    def show_notes(self):
        return self.notes

n1 = Notebook(['note1','note2','note3','note4'])
n1.add_note('note5')
print(n1.show_notes())