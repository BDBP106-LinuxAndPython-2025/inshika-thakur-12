#!/usr/bin/python3

"""Write a function enzyme_activity(name,subs_conc) that accepts the name of the enzyme and substrate concentration as
parameters. This will have an inner function called michelis_menten(Vmax,Km) that computes the reaction rate

v =V max × [S]/Km + [S]"""


def enzyme_activity(name, subs_conc):
    def michelis_menten(Vmax, Km):
        v = (Vmax * subs_conc) / (Km + subs_conc)
        return v

    return f"Enzyme: {name}, Substrate Concentration: {subs_conc}, Reaction Rate Function Ready"
enzyme = enzyme_activity("Amylase", 5)
rate = (5 * 5) / (2 + 5)  # Example: Vmax=5, Km=2
print(rate)