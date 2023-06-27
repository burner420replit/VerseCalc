import tkinter as tk
from tkinter import *

def calculate():
    # Retrieve input values
    hp = float(entry1.get())        #formula (no ascension): (basestat + iv + ev) *(male/shiny/mutation) * (level*0.04)
    hpiv = float(entry2.get())      #for high hp pokemon like blissey it can be slightly off
    hpev = float(entry3.get())
    level = float(entry4.get())     #level is used in the stat calculation
##    #atk
    atk = float(entry5.get())       #formula (no ascension): (basestat + iv + ev) * (male/shiny/mutation) * ((level * 2/5)+2)
    atkiv = float(entry6.get())
    atkev = float(entry7.get())
    #def
    Def = float(entry8.get())       #all the other stats (basiclly non HP) use the same formula as ATK
    Defiv = float(entry9.get())
    Defev = float(entry10.get())
    #SpAtk
    SpAtk = float(entry11.get())
    SpAtkIv = float(entry12.get())
    SpAtkEv = float(entry13.get())
    #SpDef
    Spdef = float(entry14.get())
    SpDefev = float(entry15.get())
    SpDefiv = float(entry16.get())
    #speed
    Speed = float(entry17.get())
    SpeedIV = float(entry18.get())
    SpeedEV = float(entry19.get())
    
    
    
    # Retrieve checkbox states
    use_male = checkbox_var1.get()
    use_shiny = checkbox_var2.get()
    use_mutated = checkbox_var3.get()
    use_rare = checkbox_var4.get()
    
    # Perform calculation based on checkbox states
    result_hp = 0
    result_atk = 0
    result_def = 0
    result_SpAtk = 0
    result_SpDef = 0
    result_Speed = 0
    
    if use_male:
        result_hp = (hp + hpiv + hpev) * 1.1 * (level * 0.04)
        result_atk = (atk + atkiv + atkev) * 1.1 * ((level * 2/5) + 2)
        result_def = (Def + Defiv + Defev) * 1.1 * ((level * 2/5) + 2)
        result_SpAtk = (SpAtk + SpAtkIv + SpAtkEv) * 1.1 * ((level * 2/5) + 2)
        result_SpDef = (Spdef + SpDefiv + SpDefev) * 1.1 * ((level * 2/5) + 2)
        result_Speed = (Speed + SpeedIV + SpeedEV) * 1.1 * ((level * 2/5) + 2)
    if use_male and use_shiny:
        result_hp = (hp + hpiv + hpev) * (1.2) * (level * 0.04)
        result_atk = (atk + atkiv + atkev) * (1.2) * ((level * 2/5) + 2)
        result_def = (Def + Defiv + Defev) * (1.2) * ((level * 2/5) + 2)
        result_SpAtk = (SpAtk + SpAtkIv + SpAtkEv) * (1.2) * ((level * 2/5) + 2)
        result_SpDef = (Spdef + SpDefiv + SpDefev) * (1.2) * ((level * 2/5) + 2)
        result_Speed = (Speed + SpeedIV + SpeedEV) * (1.2) * ((level * 2/5) + 2)
    if use_mutated and use_shiny:
        result_hp = (hp + hpiv + hpev) * (1.4) * (level * 0.04)
        result_atk = (atk + atkiv + atkev) * (1.4) * ((level * 2/5) + 2)
        result_def = (Def + Defiv + Defev) * (1.4) * ((level * 2/5) + 2)
        result_SpAtk = (SpAtk + SpAtkIv + SpAtkEv) * (1.4) * ((level * 2/5) + 2)
        result_SpDef = (Spdef + SpDefiv + SpDefev) * (1.4) * ((level * 2/5) + 2)
        result_Speed = (Speed + SpeedIV + SpeedEV) * (1.4) * ((level * 2/5) + 2)
    if use_male and use_mutated:
        result_hp = (hp + hpiv + hpev) * 1.4 * (level * 0.04)
        result_atk = (atk + atkiv + atkev) * 1.4 * ((level * 2/5) + 2)
        result_def = (Def + Defiv + Defev) * 1.4 * ((level * 2/5) + 2)
        result_SpAtk = (SpAtk + SpAtkIv + SpAtkEv) * 1.4 * ((level * 2/5) + 2)
        result_SpDef = (Spdef + SpDefiv + SpDefev) * 1.4* ((level * 2/5) + 2)
        result_Speed = (Speed + SpeedIV + SpeedEV) * 1.4 * ((level * 2/5) + 2)
    if use_male and use_shiny and use_mutated:
        result_hp = (hp + hpiv + hpev) * (1.5) * (level * 0.04)
        result_atk = (atk + atkiv + atkev) * (1.5) * ((level * 2/5) + 2)
        result_def = (Def + Defiv + Defev) * (1.5) * ((level * 2/5) + 2)
        result_SpAtk = (SpAtk + SpAtkIv + SpAtkEv) * (1.5) * ((level * 2/5) + 2)
        result_SpDef = (Spdef + SpDefiv + SpDefev) * (1.5) * ((level * 2/5) + 2)
        result_Speed = (Speed + SpeedIV + SpeedEV) * (1.5) * ((level * 2/5) + 2)

    if use_rare:
        result_hp = (hp + (hpiv*1.5) + hpev) * (level * 0.04)
        result_atk = (atk + (atkiv * 1.5) + atkev) * ((level * 2/5) + 2)
        result_def = (Def + (Defiv * 1.5) + Defev)* ((level * 2/5) + 2)
        result_SpAtk = (SpAtk + (SpAtkIv * 1.5) + SpAtkEv) * ((level * 2/5) + 2)
        result_SpDef = (Spdef + (SpDefiv * 1.5) + SpDefev) * ((level * 2/5) + 2)
        result_Speed = (Speed + (SpeedIV * 1.5) + SpeedEV) * ((level * 2/5) + 2)
    if use_rare and use_male:
        result_hp = (hp + (hpiv*1.5) + hpev) * 1.1 * (level * 0.04)
        result_atk = (atk + (atkiv * 1.5) + atkev) * 1.1 *((level * 2/5) + 2)
        result_def = (Def + (Defiv * 1.5) + Defev) * 1.1 * ((level * 2/5) + 2)
        result_SpAtk = (SpAtk + (SpAtkIv * 1.5) + SpAtkEv) * 1.1 * ((level * 2/5) + 2)
        result_SpDef = (Spdef + (SpDefiv * 1.5) + SpDefev) * 1.1 * ((level * 2/5) + 2)
        result_Speed = (Speed + (SpeedIV * 1.5) + SpeedEV) * 1.1 * ((level * 2/5) + 2)
    if use_rare and use_shiny:
        result_hp = (hp + (hpiv*1.5) + hpev) * 1.1 * (level * 0.04)
        result_atk = (atk + (atkiv * 1.5) + atkev) * 1.1 *((level * 2/5) + 2)
        result_def = (Def + (Defiv * 1.5) + Defev) * 1.1 * ((level * 2/5) + 2)
        result_SpAtk = (SpAtk + (SpAtkIv * 1.5) + SpAtkEv) * 1.1 * ((level * 2/5) + 2)
        result_SpDef = (Spdef + (SpDefiv * 1.5) + SpDefev) * 1.1 * ((level * 2/5) + 2)
        result_Speed = (Speed + (SpeedIV * 1.5) + SpeedEV) * 1.1 * ((level * 2/5) + 2)

    if use_rare and use_male and use_shiny:
        result_hp = (hp + (hpiv*1.5) + hpev) * (1.2) * (level * 0.04)
        result_atk = (atk + (atkiv * 1.5) + atkev) * (1.2) *((level * 2/5) + 2)
        result_def = (Def + (Defiv * 1.5) + Defev) * (1.2) * ((level * 2/5) + 2)
        result_SpAtk = (SpAtk + (SpAtkIv * 1.5) + SpAtkEv) * (1.2) * ((level * 2/5) + 2)
        result_SpDef = (Spdef + (SpDefiv * 1.5) + SpDefev) * (1.2) * ((level * 2/5) + 2)
        result_Speed = (Speed + (SpeedIV * 1.5) + SpeedEV) * (1.2) * ((level * 2/5) + 2)
    if use_rare and use_mutated and use_shiny:
        result_hp = (hp + (hpiv*1.5) + hpev) * (1.4) * (level * 0.04)
        result_atk = (atk + (atkiv * 1.5) + atkev) * (1.4) *((level * 2/5) + 2)
        result_def = (Def + (Defiv * 1.5) + Defev) * (1.4) * ((level * 2/5) + 2)
        result_SpAtk = (SpAtk + (SpAtkIv * 1.5) + SpAtkEv) * (1.4) * ((level * 2/5) + 2)
        result_SpDef = (Spdef + (SpDefiv * 1.5) + SpDefev) * (1.4) * ((level * 2/5) + 2)
        result_Speed = (Speed + (SpeedIV * 1.5) + SpeedEV) * (1.4) * ((level * 2/5) + 2)

    if use_rare and use_mutated and use_shiny:
        result_hp = (hp + (hpiv*1.5) + hpev) * (1.4) * (level * 0.04)
        result_atk = (atk + (atkiv * 1.5) + atkev) * (1.4) *((level * 2/5) + 2)
        result_def = (Def + (Defiv * 1.5) + Defev) * (1.4) * ((level * 2/5) + 2)
        result_SpAtk = (SpAtk + (SpAtkIv * 1.5) + SpAtkEv) * (1.4) * ((level * 2/5) + 2)
        result_SpDef = (Spdef + (SpDefiv * 1.5) + SpDefev) * (1.4) * ((level * 2/5) + 2)
        result_Speed = (Speed + (SpeedIV * 1.5) + SpeedEV) * (1.4) * ((level * 2/5) + 2)

    
    if use_rare and use_male and use_shiny and use_mutated:
        result_hp = (hp + (hpiv*1.5) + hpev) * (1.5) * (level * 0.04)
        result_atk = (atk + (atkiv * 1.5) + atkev) * (1.5) *((level * 2/5) + 2)
        result_def = (Def + (Defiv * 1.5) + Defev) * (1.5) * ((level * 2/5) + 2)
        result_SpAtk = (SpAtk + (SpAtkIv * 1.5) + SpAtkEv) * (1.5) * ((level * 2/5) + 2)
        result_SpDef = (Spdef + (SpDefiv * 1.5) + SpDefev) * (1.5) * ((level * 2/5) + 2)
        result_Speed = (Speed + (SpeedIV * 1.5) + SpeedEV) * (1.5) * ((level * 2/5) + 2)
    elif not use_male and not use_shiny and not use_mutated and not use_rare:
        result_hp = (hp + hpiv + hpev) * ((level * 0.04))
        result_atk = (atk + atkiv + atkev) * ((level * 2/5) + 2)
        result_def = (Def + Defiv + Defev) * ((level * 2/5) + 2)
        result_SpAtk = (SpAtk + SpAtkIv + SpAtkEv) * ((level * 2/5) + 2)
        result_SpDef = (Spdef + SpDefiv + SpDefev) * ((level * 2/5) + 2)
        result_Speed = (Speed + SpeedIV + SpeedEV) * ((level * 2/5) + 2)

    resulthp_label.config(text="Hp: " + str(result_hp))
    resultatk_label.config(text="Attack: " + str(result_atk))
    resultDef_label.config(text="Defense: " + str(result_def))
    resultSpAtk_label.config(text="Special Attack: " + str(result_SpAtk))
    resultSpDef_label.config(text="Special Defense: " + str(result_SpDef))
    resultSpeed_label.config(text="Speed: " + str(result_Speed))

# Create the main window
window = tk.Tk()
window.title("Calculator")


label4 = tk.Label(window, text="Level:", width=5).grid(row=0, column=0)
entry4 = tk.Entry(window, width=5)
entry4.grid(row=0,column=1)
# Create input fields
#hp
label1 = tk.Label(window, text="Base Hp:", width=10).grid(row=1, column=0)
entry1 = tk.Entry(window, width=5)
entry1.grid(row=1,column=1)
#hp iv
label2 = tk.Label(window, text="Iv:", width=5).grid(row=1, column=2)
entry2 = tk.Entry(window, width=5)
entry2.grid(row=1, column=3)
#hp ev
label3 = tk.Label(window, text="Ev:", width=5).grid(row=1, column=4)
entry3 = tk.Entry(window, width = 5)
entry3.grid(row=1, column=5)

label5 = tk.Label(window, text="Base Atk:", width=10).grid(row=2, column=0)
entry5 = tk.Entry(window, width=5)
entry5.grid(row=2,column=1)
#atk iv
label6 = tk.Label(window, text="Iv:", width=5).grid(row=2, column=2)
entry6 = tk.Entry(window, width=5)
entry6.grid(row=2, column=3)
#atk ev
label7 = tk.Label(window, text="Ev:", width=5).grid(row=2, column=4)
entry7 = tk.Entry(window, width = 5)
entry7.grid(row=2, column=5)

#defence
label8 = tk.Label(window, text="Base def:", width=10).grid(row=3, column=0)
entry8 = tk.Entry(window, width=5)
entry8.grid(row=3,column=1)
#def iv
label9 = tk.Label(window, text="Iv:", width=5).grid(row=3, column=2)
entry9 = tk.Entry(window, width=5)
entry9.grid(row=3, column=3)
#def ev
label10 = tk.Label(window, text="Ev:", width=5).grid(row=3, column=4)
entry10 = tk.Entry(window, width = 5)
entry10.grid(row=3, column=5)

#spatk
label11 = tk.Label(window, text="Base SpAtk:", width=10).grid(row=4, column=0)
entry11 = tk.Entry(window, width=5)
entry11.grid(row=4,column=1)
#SpAtk iv
label12 = tk.Label(window, text="Iv:", width=5).grid(row=4, column=2)
entry12 = tk.Entry(window, width=5)
entry12.grid(row=4, column=3)
#SpAtk ev
label13 = tk.Label(window, text="Ev:", width=5).grid(row=4, column=4)
entry13 = tk.Entry(window, width = 5)
entry13.grid(row=4, column=5)

#SpDef
label14 = tk.Label(window, text="Base SpDef:", width=10).grid(row=5, column=0)
entry14 = tk.Entry(window, width=5)
entry14.grid(row=5,column=1)
#SpDef iv
label15 = tk.Label(window, text="Iv:", width=5).grid(row=5, column=2)
entry15 = tk.Entry(window, width=5)
entry15.grid(row=5, column=3)
#SpDef ev
label16 = tk.Label(window, text="Ev:", width=5).grid(row=5, column=4)
entry16 = tk.Entry(window, width = 5)
entry16.grid(row=5, column=5)

#Speed
label17 = tk.Label(window, text="Base Spe:", width=10).grid(row=6, column=0)
entry17 = tk.Entry(window, width=5)
entry17.grid(row=6,column=1)
#Speed iv
label18 = tk.Label(window, text="Iv:", width=5).grid(row=6, column=2)
entry18 = tk.Entry(window, width=5)
entry18.grid(row=6, column=3)
#Speed ev
label19 = tk.Label(window, text="Ev:", width=5).grid(row=6, column=4)
entry19 = tk.Entry(window, width = 5)
entry19.grid(row=6, column=5)



##Create checkboxes
checkbox_var1 = tk.BooleanVar()
checkbox1 = tk.Checkbutton(window, text="male", variable=checkbox_var1, onvalue=1, offvalue=0)
checkbox1.grid(row=7, column=0)

checkbox_var2 = tk.BooleanVar()
checkbox2 = tk.Checkbutton(window, text="shiny/shifter", variable=checkbox_var2, onvalue=1, offvalue=0)
checkbox2.grid(row=8, column=0)

checkbox_var3 = tk.BooleanVar()
checkbox3 = tk.Checkbutton(window, text="mutated", variable=checkbox_var3, onvalue=1, offvalue=0)
checkbox3.grid(row=9, column=0)

checkbox_var4 = tk.BooleanVar()
checkbox4 = tk.Checkbutton(window, text="rare", variable=checkbox_var4, onvalue=10, offvalue=0)
checkbox4.grid(row=10, column=0)

# Create calculate button
calculate_button = tk.Button(window, text="Calculate", command=calculate, width=10).grid(row=11, column=0)

# Create result label
resulthp_label = tk.Label(window, text="Hp: ")
resulthp_label.grid(row=12, column=0, columnspan=6)

resultatk_label = tk.Label(window, text="Atk: ")
resultatk_label.grid(row=13, column=0, columnspan=6)

resultDef_label = tk.Label(window, text="Def: ")
resultDef_label.grid(row=14, column=0, columnspan=6)

resultSpAtk_label = tk.Label(window, text="SpAtk: ")
resultSpAtk_label.grid(row=15, column=0, columnspan=6)

resultSpDef_label = tk.Label(window, text="SpDef: ")
resultSpDef_label.grid(row=16, column=0, columnspan=6)

resultSpeed_label = tk.Label(window, text="Speed: ")
resultSpeed_label.grid(row=17, column=0, columnspan=6)

# Run the main loop
window.mainloop()
