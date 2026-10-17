from tkinter import *
from tkinter import ttk
root = Tk()

# declaring dummy variables for now
func = None
moles = None
projMotion = None
dimAnalysis = None
constantAcc = None

root.title("Physims")
root.geometry("600x400")

# root malleability
root.columnconfigure(0, weight = 1)
root.rowconfigure(1, weight = 1)

# Header
header = ttk.Frame(root)
header.grid(column=0, row=0, sticky = (N,E,W,S))
header.columnconfigure(0, weight=1)
Physims = ttk.Label(header, text="Physims")
Physims.grid(column=0, row=0)

# mainframe
mainframe = ttk.Frame(root)
mainframe.grid(column=0, row=1, sticky = (N,E,W,S))
mainframe.columnconfigure(0, weight = 1)
mainframe.rowconfigure(0, weight = 1)
mainframe.columnconfigure(1, weight = 1)
mainframe.rowconfigure(1, weight = 1)

# Projectile Motion frame
proj = ttk.Frame(mainframe)
proj.grid(column=0, row=0)
ttk.Label(proj, text="Placeholder image for projectile motion").grid(column=0, row=0)
ttk.Button(proj, text="Projectile Motion", command=projMotion).grid(column=0, row=1)

# Graphing constant acceleration frame
constacc = ttk.Frame(mainframe)
constacc.grid(column=1, row=0)
ttk.Label(constacc, text="Placeholder image for constant acceleration").grid(column=0, row=0)
ttk.Button(constacc, text="Graphing constant acceleration", command=constantAcc).grid(column=0, row=1)

# Graphing functions frame
funct = ttk.Frame(mainframe)
funct.grid(column=0, row=1)
ttk.Label(funct, text="Placeholder image for graphing functions").grid(column=0, row=0)
ttk.Button(funct, text="Graphing functions", command=func).grid(column=0, row=1)

# Moles calculator frame
molar = ttk.Frame(mainframe)
molar.grid(column=1, row=1)
ttk.Label(molar, text="Placeholder image for moles calculator").grid(column=0, row=0)
ttk.Button(molar, text="Moles Calculator", command=moles).grid(column=0, row=1)


# navigation frame
navi = ttk.Frame(root)


# mainframe malleability
mainframe.columnconfigure(0, weight = 1)
mainframe.rowconfigure(0, weight = 1)

root.mainloop()