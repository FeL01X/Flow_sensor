import customtkinter as ctk

# Theme-Einstellungen
ctk.set_appearance_mode("dark")  # "light" oder "dark"
ctk.set_default_color_theme("blue")  # Themes: "blue", "green", "dark-blue"

# Fenster erstellen
app = ctk.CTk()
app.title("Sensor GUI")
app.geometry("600x400")

# Funktion für Button
def hallo():
    label.configure(text="Connection to sensor...")
    print("Searching for sensor")

# Label
label = ctk.CTkLabel(master=app, text="Willkommen!", font=("Arial", 18))
label.pack(pady=10)

# Checkbox
checkbox_1 = ctk.CTkCheckBox(app, text="checkbox 1")
checkbox_1.pack(pady=15)

# Button
button = ctk.CTkButton(master=app, text="Klick mich", command=hallo)
button.pack(pady=5)

# GUI starten
app.mainloop()
