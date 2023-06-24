import tkinter as tk
from tkinter import messagebox
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
class StudyPlannerApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Study Planner")
        self.geometry("600x400")
        self.tasks = []
        self.goals = []
        self.subjects = []
        self.main_frame = tk.Frame(self)
        self.main_frame.pack(padx=20, pady=20)
        self.task_frame = tk.Frame(self.main_frame)
        self.goal_frame = tk.Frame(self.main_frame)
        self.subject_frame = tk.Frame(self.main_frame)
        self.report_frame = tk.Frame(self.main_frame)
        self.task_frame.pack(fill='both', expand=True)
        self.task_listbox = tk.Listbox(self.task_frame)
        self.task_listbox.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        self.task_entry = tk.Entry(self.task_frame)
        self.task_entry.pack(side=tk.LEFT, padx=10)
        self.task_add_button = tk.Button(self.task_frame, text="Add Task", command=self.add_task)
        self.task_add_button.pack(side=tk.LEFT)
        self.goal_button = tk.Button(self.task_frame, text="Goals", command=self.show_goal_section)
        self.goal_button.pack(side=tk.RIGHT)
        self.goal_listbox = tk.Listbox(self.goal_frame)
        self.goal_listbox.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        self.goal_entry = tk.Entry(self.goal_frame)
        self.goal_entry.pack(side=tk.LEFT, padx=10)
        self.goal_add_button = tk.Button(self.goal_frame, text="Add Goal", command=self.add_goal)
        self.goal_add_button.pack(side=tk.LEFT)
        self.subject_button = tk.Button(self.goal_frame, text="Subjects", command=self.show_subject_section)
        self.subject_button.pack(side=tk.RIGHT)
        self.subject_listbox = tk.Listbox(self.subject_frame)
        self.subject_listbox.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        self.subject_entry = tk.Entry(self.subject_frame)
        self.subject_entry.pack(side=tk.LEFT, padx=10)
        self.subject_add_button = tk.Button(self.subject_frame, text="Add Subject", command=self.add_subject)
        self.subject_add_button.pack(side=tk.LEFT)
        self.report_button = tk.Button(self.subject_frame, text="Progress Report", command=self.show_report_section)
        self.report_button.pack(side=tk.RIGHT)
        self.report_figure = plt.Figure(figsize=(6, 4), dpi=100)
        self.report_canvas = FigureCanvasTkAgg(self.report_figure, master=self.report_frame)
        self.report_canvas.get_tk_widget().pack()
        self.back_button = tk.Button(self.report_frame, text="Back", command=self.show_subject_section)
        self.back_button.pack(side=tk.BOTTOM)
        self.mainloop()
    def add_task(self):
        task_text = self.task_entry.get()
        if task_text:
            self.tasks.append(task_text)
            self.task_listbox.insert(tk.END, task_text)
            self.task_entry.delete(0, tk.END)
    def add_goal(self):
        goal_text = self.goal_entry.get()
        if goal_text:
            self.goals.append(goal_text)
            self.goal_listbox.insert(tk.END, goal_text)
            self.goal_entry.delete(0, tk.END)
    def add_subject(self):
        subject_text = self.subject_entry.get()
        if subject_text:
            self.subjects.append(subject_text)
            self.subject_listbox.insert(tk.END, subject_text)
            self.subject_entry.delete(0, tk.END)
    def show_goal_section(self):
        self.task_frame.pack_forget()
        self.goal_frame.pack(fill='both', expand=True)
    def show_subject_section(self):
        self.goal_frame.pack_forget()
        self.subject_frame.pack(fill='both', expand=True)
    def show_report_section(self):
        self.subject_frame.pack_forget()
        self.generate_report()
        self.report_frame.pack(fill='both', expand=True)
    def generate_report(self):
        num_tasks = len(self.tasks)
        num_goals = len(self.goals)
        num_subjects = len(self.subjects)
        labels = ['Tasks', 'Goals', 'Subjects']
        data = [num_tasks, num_goals, num_subjects]
        self.report_figure.clear()
        plt.bar(labels, data)
        plt.xlabel('Categories')
        plt.ylabel('Count')
        plt.title('Progress Report')
        plt.show()
        self.report_canvas.draw()
    def on_closing(self):
        if messagebox.askokcancel("Quit", "Do you want to quit?"):
            self.destroy()
if __name__ == '__main__':
    app = StudyPlannerApp()
