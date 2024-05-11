import tkinter as tk
from tkinter import messagebox
from student import Student
from data_handling import save_scores

"""
Grade Application GUI.

This class manages the graphical user interface for the grade calculator application.
It allows for input of student names and scores, calculation of grades, and displays the results.
"""

class GradeApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Grade Calculator")
        self.geometry("300x400")  # Window size
        self.students = []

        self.create_widgets()

    def create_widgets(self):
        self.input_frame = tk.Frame(self)
        self.input_frame.pack(pady=20)

        tk.Label(self.input_frame, text="Student name:").pack()
        self.name_entry = tk.Entry(self.input_frame, width=25)
        self.name_entry.pack()

        tk.Label(self.input_frame, text="Number of attempts:").pack()
        self.attempts_var = tk.StringVar()
        self.attempt_entry = tk.Entry(self.input_frame, textvariable=self.attempts_var, width=25)
        self.attempt_entry.pack()
        self.attempts_var.trace_add("write", self.setup_score_entries)

        self.score_frame = tk.Frame(self.input_frame)
        self.score_frame.pack(pady=10)
        self.score_entries = []

        self.submit_button = tk.Button(self.input_frame, text="SUBMIT", command=self.submit_scores)
        self.submit_button.pack(pady=20)

        self.output_frame = tk.Frame(self)
        self.output_frame.pack(fill=tk.BOTH, expand=True)

    def setup_score_entries(self, *args):
        try:
            raw_value = self.attempts_var.get().strip()
            if raw_value.isdigit():
                num_attempts = int(raw_value)
                if num_attempts < 1 or num_attempts > 4:
                    raise ValueError("Number of attempts must be between 1 and 4")
                self.clear_existing_entries()
                self.create_score_entries(num_attempts)
            else:
                self.clear_existing_entries()
        except ValueError as e:
            messagebox.showerror("Error", str(e))

    def clear_existing_entries(self):
        for widget in self.score_frame.winfo_children():
                widget.destroy()
        self.score_entries.clear()

    def create_score_entries(self, num_attempts):
        for i in range(num_attempts):
            label = tk.Label(self.score_frame, text=f"Score {i+1}:")
            label.pack()
            entry = tk.Entry(self.score_frame, width=10)
            entry.pack()
            self.score_entries.append(entry)

    def submit_scores(self):
        name = self.name_entry.get().strip()
        if not name:
            messagebox.showerror("Error", "Student name cannot be empty")
            return

        try:
            scores = [int(entry.get()) for entry in self.score_entries]
            if any(score < 0 or score > 100 for score in scores):
                raise ValueError("All scores must be integers between 0 and 100")
            student = Student(name, scores)
            student.calculate_statistics()
            self.students.append(student)
            save_scores("scores.csv", self.students)
            self.clear_entries()
            label = tk.Label(self.output_frame, text=f"Submitted: {name}")
            label.pack()
        except ValueError as e:
            messagebox.showerror("Error", str(e))

    def clear_entries(self):
        for entry in self.score_entries:
            entry.delete(0, tk.END)
            entry.pack_forget()
        for label in self.score_frame.winfo_children():
            if isinstance(label, tk.Label):
                label.pack_forget()
        self.name_entry.delete(0, tk.END)
        self.attempt_entry.delete(0, tk.END)

app = GradeApp()
app.mainloop()
