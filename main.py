import tkinter as tk

def main():
    root = tk.Tk()
    root.title("WinLock")

    # Устанавливаем окно на весь экран
    root.attributes('-fullscreen', True)

    # Создаем надпись
    label = tk.Label(root, text="Enter the key and press ctrl+c", font=("Arial", 24))
    label.pack(expand=True)

    # Создаем поле ввода
    entry = tk.Entry(root, font=("Arial", 24))
    entry.pack(expand=True)

    # Запускаем главный цикл tkinter
    root.mainloop()

if __name__ == "__main__":
    main()
