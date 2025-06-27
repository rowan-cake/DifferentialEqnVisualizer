import tkinter as tk
import json
import subprocess

def run_animation():
    # Get values from inputs
    params = {
        "mass": entry_mass.get(),
        "damping": entry_damping.get(),
        "stiffness": entry_stiffness.get(),
        "x0": entry_x0.get(),
        "v0": entry_v0.get(),
        "forcing": entry_force.get()
    }

    # Write to config.json
    with open("config.json", "w") as f:
        json.dump(params, f)

    # Run manim
    subprocess.run(["manim", "-pql", "MassSpringAnimation.py", "MassSpring"])

# GUI setup
root = tk.Tk()
root.title("Mass-Spring System")

# Input fields
fields = {}
for label in ["mass", "damping", "stiffness", "x0", "v0", "forcing"]:
    tk.Label(root, text=label).pack()
    entry = tk.Entry(root)
    entry.pack()
    fields[label] = entry

entry_mass = fields["mass"]
entry_damping = fields["damping"]
entry_stiffness = fields["stiffness"]
entry_x0 = fields["x0"]
entry_v0 = fields["v0"]
entry_force = fields["forcing"]

# Run button
tk.Button(root, text="Render Animation", command=run_animation).pack()

root.mainloop()
