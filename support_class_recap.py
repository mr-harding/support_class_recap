from tkinter import *
from tkinter import messagebox

class Student:
	def __init__(self, name, credits):
		self.name = name
		self.credits = credits

students = []
students.append(Student("Jane", 85))
students.append(Student("Joan", 65))
students.append(Student("Jess", 80))

for s in students:
	print(s.name, "has", s.credits, "credits")