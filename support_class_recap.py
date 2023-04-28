from tkinter import *
from tkinter import messagebox

class Student:
	def __init__(self, name, credits):
		self.name = name
		self.credits = credits

s1 = Student("Jane", 85)
s2 = Student("Joan", 65)
s3 = Student("Jess", 80)

print(s1.name, "has", s1.credits)
