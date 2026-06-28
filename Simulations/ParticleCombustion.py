# Let's create a particle exploder

import random # random particles
import tkinter as tk


# initialising our window
window = tk.Tk()
window.geometry("600x600")
window.title("Particle Combustion")
canvas = tk.Canvas(window, background="black")  # The drawing board for these particles
canvas.pack(fill=tk.BOTH, expand=True)          # Canvas fills our window

system = [] # the list of particles
g = 0.2 # how fast do the particles fall?

def explosion(count=200):
    spawn_x = canvas.winfo_width()//2 # particles spawn at the centre
    spawn_y = canvas.winfo_height()//2 # particles spawn at the centre
    for iterations in range(count):
       v_x = random.uniform(-15,15) # speed of particles (x-axis)
       v_y = random.uniform(-15,15) # speed of particles (y-axis)

       radius = random.uniform(2,6) # size/shape of the particle
       
       # Particle colors
       color = random.choice([
           "red",
           "orange",
           "yellow",
           "white",
           "cyan"
       ])
       life = random.randint(20,40) # How long does the particle stay on screen?
       
       # Updating positions
       x_i = spawn_x - radius
       y_i = spawn_y - radius
       x_f = spawn_x + radius
       y_f = spawn_y + radius

       # Finally creating the particle
       particle_id = canvas.create_oval(
           x_i, y_i, x_f, y_f,
           fill=color,
           outline=color
       )

       # Appending our particle to the system list

       particle_data = {
           "particle": particle_id,
           "x": x_i,
           "y": y_i,
           "v_x": v_x,
           "v_y": v_y,
           "radius": radius,
           "color": color,
           "life": life
       }
       system.append(particle_data)

def animation():
    for particle in system:
        particle["v_y"] += g # falling

        particle["x"] += particle["v_x"] # horizontal movement
        particle["y"] += particle["v_y"] # vertical movement

        canvas.move(
            particle["particle"],
            particle["v_x"],
            particle["v_y"]
        )

        particle["life"] -= 1 # reducing the "lifespan"

    for particle in reversed(system):
        # Checking if the particle's "life" has ran out or if it has left the window's boundaries
        if (
            particle["life"] <= 0
            or particle["x"] + particle["radius"] < 0
            or particle["x"] - particle["radius"] > canvas.winfo_width()
            or particle["y"] + particle["radius"] < 0
            or particle["y"] - particle["radius"] > canvas.winfo_height()
        ):
            system.remove(particle)
            canvas.delete(particle["particle"])

    window.after(20, animation) # Next frame


# Making our button
explode = tk.Button(
    window,
    text="Explode!",
    bg="lightgray",
    command=explosion
)
explode.pack()

animation()
window.mainloop()
