import tkinter as tk
import json
import os

FILE = "tasks.json"
tasks = []

if os.path.exists(FILE):
    try:
        with open(FILE, "r", encoding="utf-8") as f:
            tasks = json.load(f)
    except:
        tasks = []


def save():
    with open(FILE, "w", encoding="utf-8") as f:
        json.dump(tasks, f, ensure_ascii=False)


def show():
    box.delete(0, tk.END)
    for task in tasks:
        mark = "✓" if task["done"] else "○"
        box.insert(tk.END, mark + " " + task["text"])
    status.config(text="Всего задач: " + str(len(tasks)))


def add():
    text = entry.get().strip()
    if text:
        tasks.append({"text": text, "done": False})
        entry.delete(0, tk.END)
        save()
        show()


def complete():
    selected = box.curselection()
    if selected:
        tasks[selected[0]]["done"] = True
        save()
        show()


def delete():
    selected = box.curselection()
    if selected:
        tasks.pop(selected[0])
        save()
        show()


root = tk.Tk()
root.title("Мои задачи")
root.geometry("400x450")

tk.Label(
    root, text="Мой список задач",
    font=("Arial", 20, "bold")
).pack(pady=15)

entry = tk.Entry(root, font=("Arial", 14))
entry.pack(padx=20, fill="x")

tk.Button(
    root, text="Добавить задачу",
    command=add
).pack(pady=5)

box = tk.Listbox(root, font=("Arial", 13))
box.pack(padx=20, pady=10, fill="both", expand=True)

tk.Button(
    root, text="Выполнено ✓",
    command=complete
).pack(pady=3)

tk.Button(
    root, text="Удалить задачу",
    command=delete
).pack(pady=3)

status = tk.Label(root, text="")
status.pack(pady=10)

show()
root.mainloop()
