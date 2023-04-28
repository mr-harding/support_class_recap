from tkinter import *
from tkinter import messagebox

class Student:
	def __init__(self, name, credits):
		self.name = name
		self.credits = credits

class StudentGUI:
	def __init__(self, parent):
		label1 = Label(parent, text = "STUDENT NCEA DATA MANAGER THING")
		label1.pack()

		go_btn = Button(parent, text = "Who has passed NCEA?", command = self.check_pass)
		go_btn.pack()

	def check_pass(self):
		CREDITS_REQUIRED = 80
		print("No data yet..")		

if __name__ == "__main__":
	root = Tk()
	w = StudentGUI(root)
	root.mainloop()

"""
students = []
students.append(Student("Jane", 85))
students.append(Student("Joan", 65))
students.append(Student("Jess", 80))

for s in students:
	print(s.name, "has", s.credits, "credits")
"""