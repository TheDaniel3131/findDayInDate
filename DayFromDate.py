import tkinter as tk
from tkinter import font as tkfont
from tkinter import messagebox


def calculate_day_of_week():
    try:
        day = int(day_entry.get())
        month = int(month_entry.get())
        year = int(year_entry.get())

        # Validate the input values
        if not (1 <= day <= 31) or not (1 <= month <= 12) or year < 1:
            raise ValueError("Invalid input")

        # Adjust the month and year if necessary
        if month < 3:
            month += 12
            year -= 1

        # Calculate the day of the week
        q = day
        m = month
        j = year // 100
        k = year % 100

        h = (q + 13 * (m + 1) // 5 + k + k // 4 + j // 4 + 5 * j) % 7

        # Map the result to the corresponding day of the week
        days_of_week = ["Saturday", "Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]
        day_of_week = days_of_week[h]

        # Update the label with the result
        result_label.config(text="\n The day of the week for {}/{}/{} is: {}".format(day, month, year, day_of_week))

    except ValueError:
        messagebox.showerror("Error", "Incorrect Input. Please Check If You Enter Correctly For Day, Month, And Year!")


# Create the Tkinter window
window = tk.Tk()

# Hide the window initially to prevent flickering
window.withdraw()

# Set the window title
window.title("Find The Day In Any Date")

# Set the window size
window.geometry("350x300")

# Disable window resizing
window.resizable(False, False)

# Set the icon for the window (replace 'day_logo.ico' with the actual filename)
window.iconbitmap("day_logo.ico")

# Center the window on the screen
window.eval('tk::PlaceWindow . center')

# Show the window after it has been centered
window.deiconify()

# Get the screen width and height
screen_width = window.winfo_screenwidth()
screen_height = window.winfo_screenheight()

# Calculate the x and y coordinates for centering the window
x = (screen_width - window.winfo_reqwidth()) // 2
y = (screen_height - window.winfo_reqheight()) // 2

# Set the window position
window.geometry(f"+{x}+{y}")

# Set the font style for the labels and buttons
font_style = tkfont.Font(family="Arial", size=12)

# Create a label for spacing
spacing_label = tk.Label(window, text="\n", font=font_style)
spacing_label.pack()

# Create labels and entry fields for day, month, and year
day_label = tk.Label(window, text="Day:", font=font_style)
day_label.pack()
day_entry = tk.Entry(window, font=font_style)
day_entry.pack()

month_label = tk.Label(window, text="Month:", font=font_style)
month_label.pack()
month_entry = tk.Entry(window, font=font_style)
month_entry.pack()

year_label = tk.Label(window, text="Year:", font=font_style)
year_label.pack()
year_entry = tk.Entry(window, font=font_style)
year_entry.pack()

# Add spacing between the entry and button
spacing_label = tk.Label(window, text="", font=tkfont.Font(family="Arial", size=8))
spacing_label.pack()

# Create a button to calculate the day of the week
calculate_button = tk.Button(window, text="Calculate", font=font_style, command=calculate_day_of_week)
calculate_button.pack()

# Create a label to display the result
result_label = tk.Label(window, text="", font=font_style)
result_label.pack()

# Create a label for spacing
spacing_label3 = tk.Label(window, text="\n", font=font_style)
spacing_label3.pack()

# Start the Tkinter event loop
window.mainloop()
