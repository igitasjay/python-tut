import tkinter as tk

# Create the main window
root = tk.Tk()
root.title("Hello, Tkinter!")

# Create a label widget
label = tk.Label(root, text="Hello, World!")
label.pack()

# Create a button to close the window
button = tk.Button(root, text="Close", command=root.quit)
button.pack()

# Start the Tkinter event loop
root.mainloop()
