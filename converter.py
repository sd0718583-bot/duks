import tkinter as tk
from tkinter import messagebox

# Есептеу функциясы
def esepteu():
    san = entry.get()

    # Қате тексеру
    if san == "":
        messagebox.showerror("Қате", "Сан енгізіңіз!")
        return

    try:
        san = float(san)
    except:
        messagebox.showerror("Қате", "Сан енгізіңіз!")
        return

    # Есептеу
    kvadrat = san ** 2
    kub = san ** 3

    # Нәтижені жаңарту
    result_label.config(
        text=f"Квадраты: {kvadrat}\nКубы: {kub}"
    )

# Терезе
window = tk.Tk()
window.title("Санның квадраты және кубы")  # атауы бар
window.geometry("320x230")

# Жазу
tk.Label(window, text="Санды енгізіңіз:", font=("Arial", 12)).pack(pady=5)

# Entry
entry = tk.Entry(window, font=("Arial", 12), justify="center")
entry.pack(pady=5)

# Батырма (бірнеше рет басуға болады)
tk.Button(window, text="Есептеу", command=esepteu).pack(pady=10)

# Нәтиже
result_label = tk.Label(window, text="Нәтиже:", font=("Arial", 12))
result_label.pack(pady=10)

# Бағдарлама жабылғанша жұмыс істейді
window.mainloop()