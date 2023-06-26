import tkinter as tk
from tkinter import messagebox
from tkcalendar import Calendar
import matplotlib.pyplot as plt
import time

class StudyPlanner:
    def __init__(self, root):
        self.root = root
        self.root.title("Study Planner")

        self.tasks = []
        self.goals = []

        self.task_label = tk.Label(root, text="Task:")
        self.task_label.pack()

        self.task_entry = tk.Entry(root)
        self.task_entry.pack()

        self.schedule_label = tk.Label(root, text="Schedule:")
        self.schedule_label.pack()

        self.schedule_entry = tk.Entry(root)
        self.schedule_entry.pack()

        self.add_button = tk.Button(root, text="Add Task", command=self.add_task)
        self.add_button.pack()

        self.tasks_listbox = tk.Listbox(root)
        self.tasks_listbox.pack()

        self.remove_button = tk.Button(root, text="Remove Task", command=self.remove_task)
        self.remove_button.pack()

        self.goal_label = tk.Label(root, text="Goal:")
        self.goal_label.pack()

        self.goal_entry = tk.Entry(root)
        self.goal_entry.pack()

        self.goal_time_label = tk.Label(root, text="Goal Reminder Time:")
        self.goal_time_label.pack()

        self.goal_time_entry = tk.Entry(root)
        self.goal_time_entry.pack()

        self.set_goal_button = tk.Button(root, text="Set Goal Reminder", command=self.set_goal_reminder)
        self.set_goal_button.pack()

        self.calendar_button = tk.Button(root, text="Set Goal Date", command=self.open_calendar)
        self.calendar_button.pack()

        self.plot_button = tk.Button(root, text="Plot Tasks", command=self.plot_tasks)
        self.plot_button.pack()

        self.start_time = None
        self.timer_label = tk.Label(root, text="00:00:00", font=("Arial", 18))
        self.timer_label.pack()

        self.start_button = tk.Button(root, text="Start Timer", command=self.start_timer)
        self.start_button.pack()
        self.stop_button = tk.Button(root, text="Stop Timer", command=self.stop_timer, state=tk.DISABLED)
        self.stop_button.pack()

        self.timer_running = False

        self.selected_date = None

    def add_task(self):
        task = self.task_entry.get()
        schedule = self.schedule_entry.get()
        if task and schedule:
            self.tasks.append((task, schedule))
            self.tasks_listbox.insert(tk.END, f"{task} - {schedule}")
            self.task_entry.delete(0, tk.END)
            self.schedule_entry.delete(0, tk.END)
        else:
            messagebox.showwarning("Incomplete Input", "Please enter both task and schedule.")

    def remove_task(self):
        selected_index = self.tasks_listbox.curselection()
        if selected_index:
            self.tasks_listbox.delete(selected_index)
            del self.tasks[selected_index[0]]
        else:
            messagebox.showwarning("No Task Selected", "Please select a task to remove.")

    def set_goal_reminder(self):
        goal = self.goal_entry.get()
        goal_time = self.goal_time_entry.get()
        if goal and goal_time and self.selected_date:
            self.goals.append((goal, self.selected_date, goal_time))
            messagebox.showinfo("Goal Reminder Set", f"The goal reminder for '{goal}' has been set for {self.selected_date} at {goal_time}.")
            self.goal_entry.delete(0, tk.END)
            self.goal_time_entry.delete(0, tk.END)
            self.selected_date = None

        else:
            messagebox.showwarning("Incomplete Input", "Please enter both goal, goal date, and reminder time.")

    def open_calendar(self):
        top = tk.Toplevel(self.root)
        cal = Calendar(top, selectmode="day", date_pattern="yyyy-mm-dd")
        cal.pack()
        confirm_button = tk.Button(top, text="Select Date", command=lambda: self.select_date(top, cal.get_date()))
        confirm_button.pack()

    def select_date(self, top, date):
        self.selected_date = date
        top.destroy()

    def plot_tasks(self):
        if self.tasks:
            task_names = [task[0] for task in self.tasks]
            task_schedules = [task[1] for task in self.tasks]
            plt.bar(task_names, task_schedules)
            plt.xlabel('Tasks')
            plt.ylabel('Schedule')
            plt.title('Study Tasks')
            plt.xticks(rotation=45)
            plt.tight_layout()
            plt.show()
        else:
            messagebox.showwarning("No Tasks", "There are no tasks to plot.")

    def start_timer(self):
        if not self.timer_running:
            self.start_time = time.time()
            self.timer_running = True
            self.update_timer()

            self.start_button.config(state=tk.DISABLED)
            self.stop_button.config(state=tk.NORMAL)

    def stop_timer(self):
        if self.timer_running:
            self.timer_running = False

            self.start_button.config(state=tk.NORMAL)
            self.stop_button.config(state=tk.DISABLED)

    def update_timer(self):
        if self.timer_running:
            elapsed_time = int(time.time() - self.start_time)
            hours = elapsed_time // 3600
            minutes = (elapsed_time % 3600) // 60
            seconds = elapsed_time % 60
            timer_str = f"{hours:02d}:{minutes:02d}:{seconds:02d}"
            self.timer_label.config(text=timer_str)
            self.root.after(1000, self.update_timer)

if __name__ == "__main__":
    root = tk.Tk()
    planner = StudyPlanner(root)
    root.mainloop()
