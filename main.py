import tkinter as tk
from tkinter import messagebox

def convert_lbs_to_kg(lbs):
    return lbs * 0.453592

def convert_kg_to_lbs(kg):
    return kg / 0.453592

def convert_feet_to_cm(feet):
    return feet * 30.48

def convert_cm_to_feet(cm):
    return cm / 30.48

def calculate_bmi():
    try:
        weight_value = float(weight_var.get())
        height_value = float(height_var.get())

        if weight_unit_var.get() == 'lbs':
            weight_value = convert_lbs_to_kg(weight_value)
        if height_unit_var.get() == 'ft':
            height_value = convert_feet_to_cm(height_value)

        bmi = weight_value / ((height_value / 100) ** 2)

        if bmi < 18.5:
            messagebox.showinfo('BMI', f'Your BMI is: {bmi:.2f}. You are underweight.')
        elif bmi >= 18.5 and bmi < 25:
            messagebox.showinfo('BMI', f'Your BMI is: {bmi:.2f}. You have a normal weight.')
        elif bmi >= 25 and bmi < 30:
            messagebox.showinfo('BMI', f'Your BMI is: {bmi:.2f}. You are overweight.')
        else:
            messagebox.showinfo('BMI', f'Your BMI is: {bmi:.2f}. You are obese.')

    except ValueError:
        messagebox.showerror('Error', 'Please enter valid numeric values for weight and height.')

app = tk.Tk()
app.title('BMI Calculator')
app.geometry('400x250')
app.config(bg='#000')

font1 = ('Arial', 12)
font2 = ('Arial', 10)

frame = tk.Frame(app, bg='#000')
frame.pack(padx=10, pady=10)

weight_label = tk.Label(frame, text='Weight:', font=font1, bg='#000', fg='#fff')
weight_label.grid(row=0, column=0, padx=5, pady=5, sticky='w')

weight_var = tk.StringVar()
weight_entry = tk.Entry(frame, textvariable=weight_var, font=font1, width=10)
weight_entry.grid(row=0, column=1, padx=5, pady=5)

weight_unit_var = tk.StringVar(value='kg')
weight_unit_dropdown = tk.OptionMenu(frame, weight_unit_var, 'kg', 'lbs')
weight_unit_dropdown.config(font=font2, bg='green')  # Change the color to green
weight_unit_dropdown.grid(row=0, column=2, padx=5, pady=5)

height_label = tk.Label(frame, text='Height:', font=font1, bg='#000', fg='#fff')
height_label.grid(row=1, column=0, padx=5, pady=5, sticky='w')

height_var = tk.StringVar()
height_entry = tk.Entry(frame, textvariable=height_var, font=font1, width=10)
height_entry.grid(row=1, column=1, padx=5, pady=5)

height_unit_var = tk.StringVar(value='cm')
height_unit_dropdown = tk.OptionMenu(frame, height_unit_var, 'cm', 'ft')
height_unit_dropdown.config(font=font2)
height_unit_dropdown.grid(row=1, column=2, padx=5, pady=5)

calculate_button = tk.Button(frame, text='Calculate BMI', command=calculate_bmi, font=font1, bg='green')  # Change the color to green
calculate_button.grid(row=2, columnspan=3, pady=10)

app.mainloop()