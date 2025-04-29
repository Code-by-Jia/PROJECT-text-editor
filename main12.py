import tkinter as tk

def calculate_interest():
    try:
        p = float(principal_entry.get())
        t = float(time_entry.get())
        r = float(rate_entry.get())

        si = (p * r * t) / 100
        ci = p * ((1 + r / 100) ** t) - p

        simple_result.config(text=f"Simple Interest: {si:.2f}")
        compound_result.config(text=f"Compound Interest: {ci:.2f}")
    except ValueError:
        simple_result.config(text="Enter valid numbers")
        compound_result.config(text="")


root = tk.Tk()
root.title("Interest Calculator")

tk.Label(root, text="Principal Amount:").grid(row=0, column=0, padx=5, pady=5)
principal_entry = tk.Entry(root)
principal_entry.grid(row=0, column=1)

tk.Label(root, text="Time (years):").grid(row=1, column=0, padx=5, pady=5)
time_entry = tk.Entry(root)
time_entry.grid(row=1, column=1)

tk.Label(root, text="Rate (%):").grid(row=2, column=0, padx=5, pady=5)
rate_entry = tk.Entry(root)
rate_entry.grid(row=2, column=1)

tk.Button(root, text="Calculate", command=calculate_interest).grid(row=3, columnspan=2, pady=10)

simple_result = tk.Label(root, text="")
simple_result.grid(row=4, columnspan=2)

compound_result = tk.Label(root, text="")
compound_result.grid(row=5, columnspan=2)

root.mainloop()