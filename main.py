# Import necessary modules
import tkinter as tk
from tkinter import ttk

# Create the main window
root = tk.Tk()
root.title("My Python Application")

# Create a tab control
tab_control = ttk.Notebook(root)

# Create tabs
tab1 = ttk.Frame(tab_control)
tab2 = ttk.Frame(tab_control)
tab3 = ttk.Frame(tab_control)

tab_control.add(tab1, text='Tab 1')
tab_control.add(tab2, text='Tab 2')
tab_control.add(tab3, text='Tab 3')
tab_control.pack(expand=1, fill='both')

# Add content to the tabs
# Tab 1
label1 = ttk.Label(tab1, text="This is the first tab.")
label1.pack(padx=20, pady=20)

# Tab 2
label2 = ttk.Label(tab2, text="This is the second tab.")
label2.pack(padx=20, pady=20)

# Tab 3
label3 = ttk.Label(tab3, text="This is the third tab.")
label3.pack(padx=20, pady=20)

# Run the main loop
root.mainloop()
