import customtkinter as ctk
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import numpy as np

# Theme-Einstellungen
ctk.set_appearance_mode("dark")  # "light" oder "dark"
ctk.set_default_color_theme("blue")  # Themes: "blue", "green", "dark-blue"

################################################################################
# CheckboxFrame
class MyCheckboxFrame(ctk.CTkFrame):
    def __init__(self, master, title, values):
        super().__init__(master)
        self.grid_columnconfigure(0,weight=1)
        self.title = title
        self.values = values
        self.checkboxes = []

        self.title = ctk.CTkLabel(self, text=self.title, fg_color="gray30", corner_radius=6)
        self.title.grid(row=0, column=0, padx=10, pady=(10, 0), sticky="ew")

        for i, value in enumerate(self.values):
            checkbox = ctk.CTkCheckBox(self, text=value)
            checkbox.grid(row=i+1, column=0, padx=10, pady=(10, 0), sticky="w")
            self.checkboxes.append(checkbox)

    def get(self):
        checked_checkboxes = []
        for checkbox in self.checkboxes:
            if checkbox.get() == 1:
                checked_checkboxes.append(checkbox.cget("text"))
        return checked_checkboxes
################################################################################    
# ScrollableCheckboxFrame
class MyScrollableCheckboxFrame(ctk.CTkScrollableFrame):
    def __init__(self, master, title, values):
        super().__init__(master, label_text=title)
        self.grid_columnconfigure(0, weight=1)
        self.values = values
        self.checkboxes = []

        for i, value in enumerate(self.values):
            checkbox = ctk.CTkCheckBox(self, text=value)
            checkbox.grid(row=i, column=0, padx=10, pady=(10, 0), sticky="w")
            self.checkboxes.append(checkbox)

    def get(self):
        checked_checkboxes = []
        for checkbox in self.checkboxes:
            if checkbox.get() == 1:
                checked_checkboxes.append(checkbox.cget("text"))
        return checked_checkboxes
################################################################################    
# RadiobuttonFrame
class MyRadiobuttonFrame(ctk.CTkFrame):
    def __init__(self, master, title, values):
        super().__init__(master)
        self.grid_columnconfigure(0, weight=1)
        self.values = values
        self.title = title
        self.radiobuttons = []
        self.variable = ctk.StringVar(value="")

        self.title = ctk.CTkLabel(self, text=self.title, fg_color="gray30", corner_radius=6)
        self.title.grid(row=0, column=0, padx=10, pady=(10, 0), sticky="ew")

        for i, value in enumerate(self.values):
            radiobutton = ctk.CTkRadioButton(self, text=value, value=value, variable=self.variable)
            radiobutton.grid(row=i + 1, column=0, padx=10, pady=(10, 0), sticky="w")
            self.radiobuttons.append(radiobutton)

    def get(self):
        return self.variable.get()

    def set(self, value):
        self.variable.set(value)
################################################################################
class PlottingFrame(ctk.CTkFrame):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)

        self.label = ctk.CTkLabel(self, text="Sensor data")
        self.label.grid(row=0, column=0, padx=20, pady=(5, 0))

        # Matplotlib Figure erstellen
        self.fig, self.ax = plt.subplots(figsize=(12, 9))
        self.ax.set_title("Messwerte")
        self.ax.set_xlabel("Zeit")
        self.ax.set_ylabel("Wert")

        # Canvas in Tkinter einbetten
        self.canvas = FigureCanvasTkAgg(self.fig, master=self)
        self.canvas_widget = self.canvas.get_tk_widget()
        self.canvas_widget.grid(row=1, column=0, padx=10, pady=10)

    def update_plot(self, x_data, y_data):
        """Plot mit neuen Daten aktualisieren."""
        self.ax.clear()
        self.ax.plot(x_data, y_data, marker="o", color="cyan")
        self.ax.set_title("Messwerte")
        self.ax.set_xlabel("Zeit")
        self.ax.set_ylabel("Wert")
        self.canvas.draw()
################################################################################
# TabView
class MyTabView(ctk.CTkTabview):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)

        # create tabs
        self.add("tab 1")
        self.add("tab 2")

        # add widgets on tabs
        self.label = ctk.CTkLabel(master=self.tab("tab 1"))
        self.label.grid(row=0, column=0, padx=20, pady=10)
    

################################################################################
#
# USER - Interface
#
################################################################################
class Gui(ctk.CTk):
    def __init__(self):
        super().__init__()

        self.title("my GUI")
        self.geometry("900x500")
        self.grid_columnconfigure((0, 1), weight=1)
        self.grid_rowconfigure(0, weight=1)

        values = ["value 1", "value 2", "value 3", "value 4", "value 5", "value 6"]
        self.scrollable_checkbox_frame = MyScrollableCheckboxFrame(self, title="Values", values=values)
        self.scrollable_checkbox_frame.grid(row=0, column=0, padx=10, pady=(10, 0), sticky="nsew")

        self.radiobutton_frame = MyRadiobuttonFrame(self, "Options", ["option 1", "option 2", "option 3"])
        self.radiobutton_frame.grid(row=0, column=1, padx=10, pady=(10, 0), sticky="nsew")

        self.data_visualization = PlottingFrame(master=self)
        self.data_visualization.grid(row=1, column=0, padx=20, pady=(20, 0), sticky="nsew")

        self.button = ctk.CTkButton(self, text="Plot aktualisieren", command=self.button_callback)
        self.button.grid(row=2, column=0, padx=10, pady=10, sticky="ew", columnspan=2)

    def button_callback(self):
        print("checkbox_frame:", self.scrollable_checkbox_frame.get())
        print("radiobutton_frame:", self.radiobutton_frame.get())

        # Beispiel: neue "Messwerte" simulieren
        x = np.linspace(0, 10, 11)
        y = np.random.rand(11) * 10
        self.data_visualization.update_plot(x, y)

gui = Gui()
gui.mainloop()
