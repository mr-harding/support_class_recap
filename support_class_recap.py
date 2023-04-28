from tkinter import *
from tkinter import messagebox

class Student:
	def __init__(self, name, credits):
		self.name = name
		self.credits = credits

class StudentGUI:
	def __init__(self, parent):
		self.students = []
		self.students.append(Student("Jane", 85))
		self.students.append(Student("Joan", 65))
		self.students.append(Student("Jess", 80))

		label1 = Label(parent, text = "STUDENT NCEA DATA MANAGER THING")
		label1.pack()

		go_btn = Button(parent, text = "Who has passed NCEA?", command = self.check_pass)
		go_btn.pack()

	def check_pass(self):
		CREDITS_REQUIRED = 80
		for student in self.students:
			if student.credits >= CREDITS_REQUIRED:
				messagebox.showinfo("PASSED!", "{} has passed with {} credits".format(student.name, student.credits))
			else:
				messagebox.showerror(":(", "{} has not yet passed. {} more credits needed".format(student.name, CREDITS_REQUIRED - student.credits))	

if __name__ == "__main__":
	root = Tk()
	w = StudentGUI(root)
	root.mainloop()