import customtkinter as ctk

# Theme-Einstellungen
ctk.set_appearance_mode("dark")  # "light" oder "dark"
ctk.set_default_color_theme("blue")  # Themes: "blue", "green", "dark-blue"

# Fenster erstellen
root = ctk.CTk()
root.title("Modernes GUI")
root.geometry("300x200")

# Funktion für Button
def hallo():
    label.configure(text="Hallo, moderne GUI!")

# Label
label = ctk.CTkLabel(master=root, text="Willkommen!", font=("Arial", 18))
label.pack(pady=10)

# Button
button = ctk.CTkButton(master=root, text="Klick mich", command=hallo)
button.pack(pady=5)

# GUI starten
root.mainloop()
