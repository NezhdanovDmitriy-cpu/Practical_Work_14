"""Практическое занятие № 14, вариант 11: форма регистрации Tkinter."""

import re
import tkinter as tk
from tkinter import messagebox


class ContactForm(tk.Tk):
    """Окно регистрации по образцу Contact Us."""

    def __init__(self):
        super().__init__()
        self.title("Contact Us — Вариант 11")
        self.geometry("450x590")
        self.resizable(False, False)
        self.configure(bg="#f2f2f2")

        panel = tk.Frame(self, bg="#a0a0a0", padx=42, pady=24)
        panel.pack(padx=35, pady=18, fill="both", expand=True)

        heading = tk.Label(
            panel, text="Contact Us", bg="#383838", fg="white",
            font=("Arial", 21, "bold"), pady=10
        )
        heading.pack(fill="x", pady=(0, 15))

        self.entries = {}
        fields = [
            ("First Name", False),
            ("Last Name", False),
            ("Email", False),
            ("Website", False),
            ("Password", True),
            ("Password Confirmation", True),
        ]
        for label, secret in fields:
            tk.Label(
                panel, text=label, bg="#a0a0a0", fg="#171717",
                font=("Arial", 11), anchor="w"
            ).pack(fill="x", pady=(7, 2))
            entry = tk.Entry(panel, font=("Arial", 11), show="*" if secret else "")
            entry.pack(fill="x", ipady=4)
            self.entries[label] = entry

        tk.Button(
            panel, text="Sign Up", command=self.submit,
            font=("Arial", 11), padx=12, pady=3
        ).pack(anchor="w", pady=(17, 0))
        self.entries["First Name"].focus_set()

    def submit(self):
        """Проверить введённые данные без передачи их в сеть."""
        values = {key: entry.get().strip() for key, entry in self.entries.items()}
        if not all(values.values()):
            messagebox.showwarning("Ошибка", "Заполните все поля.")
            return
        if not re.fullmatch(r"[^\s@]+@[^\s@]+\.[^\s@]+", values["Email"]):
            messagebox.showwarning("Ошибка", "Введите корректный Email.")
            return
        if not re.fullmatch(r"https?://\S+\.\S+|(?:www\.)?\S+\.\S+", values["Website"]):
            messagebox.showwarning("Ошибка", "Введите адрес сайта, например example.com.")
            return
        if not 8 <= len(values["Password"]) <= 10:
            messagebox.showwarning("Ошибка", "Пароль должен содержать 8–10 символов.")
            return
        if values["Password"] != values["Password Confirmation"]:
            messagebox.showwarning("Ошибка", "Пароли не совпадают.")
            return
        messagebox.showinfo("Успешно", "Форма заполнена правильно! Данные не отправляются.")


if __name__ == "__main__":
    app = ContactForm()
    app.mainloop()
