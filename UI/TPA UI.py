import tkinter as tk
import tkinter.font as tkFont
from PIL import ImageTk, Image
import joblib
import numpy as np


from tkcalendar import Calendar, DateEntry

# class App:
#     def __init__(self, root):
        
root = tk.Tk()
#setting title
root.title("Tourism Pattern Analysis")
#setting window size
width=602
height=547
screenwidth = root.winfo_screenwidth()
screenheight = root.winfo_screenheight()
alignstr = '%dx%d+%d+%d' % (width, height, (screenwidth - width) / 2, (screenheight - height) / 2)
root.geometry(alignstr)
root.resizable(width=False, height=False)

GLabel_853=tk.Label(root)
GLabel_853["bg"] = "#306fa0"
ft = tkFont.Font(family='calibri',size=18)
GLabel_853["font"] = ft
GLabel_853["fg"] = "#ffffff"
GLabel_853["justify"] = "center"
GLabel_853["text"] = "TOURISM PATTERN ANALYSIS"
GLabel_853.place(x=10,y=10,width=581,height=42)

GLabel_706=tk.Label(root)
GLabel_706["bg"] = "#4e95ca"
ft = tkFont.Font(family='calibri',size=10)
GLabel_706["font"] = ft
GLabel_706["fg"] = "#ffffff"
GLabel_706["justify"] = "center"
GLabel_706["text"] = "Predict Monthly Visitors based on Weather condition (Seasons) and Location Search Counts"
GLabel_706.place(x=10,y=50,width=581,height=30)

GLabel_361=tk.Label(root)
ft = tkFont.Font(family='calibri',size=10)
GLabel_361["font"] = ft
GLabel_361["fg"] = "#000000"
GLabel_361["justify"] = "center"
GLabel_361["text"] = "Please Enter the month's predicted Weather Forecast"
GLabel_361.place(x=5,y=300,width=323,height=45)

# GLabel_135=tk.Label(root)
# GLabel_135["bg"] = "#296089"
# ft = tkFont.Font(family='calibri',size=10)
# GLabel_135["font"] = ft
# GLabel_135["fg"] = "#ffffff"
# GLabel_135["justify"] = "center"
# GLabel_135["text"] = "Tourism Img"
# GLabel_135.place(x=200,y=88,width=174,height=152)


img = Image.open("tanzania-mount-kilimanjaro.jpg")
#img = img.resize((261, 197))

img = img.resize((190, 145))
test = ImageTk.PhotoImage(img)

label1 = tk.Label(image=test)
label1.image = test

# Position image
label1.place(x=200, y=88)


# GLabel_342=tk.Label(root)
# ft = tkFont.Font(family='calibri',size=10)
# GLabel_342["font"] = ft
# GLabel_342["fg"] = "#306fa0"
# GLabel_342["justify"] = "center"
# GLabel_342["text"] = "Select date"
# GLabel_342.place(x=10,y=250,width=87,height=30)

# GLineEdit_974=tk.Entry(root)
# GLineEdit_974["borderwidth"] = "1px"
# ft = tkFont.Font(family='calibri',size=10)
# GLineEdit_974["font"] = ft
# GLineEdit_974["fg"] = "#333333"
# GLineEdit_974["justify"] = "center"
# GLineEdit_974["text"] = "Date here"
# GLineEdit_974.place(x=90,y=250,width=86,height=30)


# sel = tk.StringVar() #
# cal = DateEntry( width= 16, background= "#4E95CA", foreground= "white",
#                 x=50, y=250, date_pattern="dd-mm-y", textvariable=sel)
# cal.pack(padx=200, ipadx=300, pady=255)



GLabel_421=tk.Label(root)
ft = tkFont.Font(family='calibri',size=10)
GLabel_421["font"] = ft
GLabel_421["fg"] = "#296089"
GLabel_421["justify"] = "center"
GLabel_421["text"] = "Last month's Search Interest count"
GLabel_421.place(x=3,y=250,width=227,height=50)

GLineEdit_110=tk.Entry(root)
GLineEdit_110["borderwidth"] = "1px"
ft = tkFont.Font(family='calibri',size=10)
GLineEdit_110["font"] = ft
GLineEdit_110["fg"] = "#333333"
GLineEdit_110["justify"] = "center"
GLineEdit_110["text"] = "Entry"
GLineEdit_110.place(x=220,y=258,width=89,height=30)

GLabel_3=tk.Label(root)
ft = tkFont.Font(family='calibri',size=10)
GLabel_3["font"] = ft
GLabel_3["fg"] = "#296089"
GLabel_3["justify"] = "center"
GLabel_3["text"] = "Daily Mean Celsius"
GLabel_3.place(x=20,y=330,width=110,height=49)

GLineEdit_296=tk.Entry(root)
GLineEdit_296["borderwidth"] = "1px"
ft = tkFont.Font(family='calibri',size=10)
GLineEdit_296["font"] = ft
GLineEdit_296["fg"] = "#333333"
GLineEdit_296["justify"] = "center"
GLineEdit_296["text"] = "Daily mean"
GLineEdit_296.place(x=135,y=340,width=87,height=30)

GLabel_527=tk.Label(root)
ft = tkFont.Font(family='calibri',size=10)
GLabel_527["font"] = ft
GLabel_527["fg"] = "#296089"
GLabel_527["justify"] = "center"
GLabel_527["text"] = "Average Precipitation mm"
GLabel_527.place(x=310,y=330,width=176,height=52)

GLineEdit_310=tk.Entry(root)
GLineEdit_310["borderwidth"] = "1px"
ft = tkFont.Font(family='calibri',size=10)
GLineEdit_310["font"] = ft
GLineEdit_310["fg"] = "#333333"
GLineEdit_310["justify"] = "center"
GLineEdit_310["text"] = "Average ppt"
GLineEdit_310.place(x=480,y=340,width=89,height=30)


def GButton_545_command():
    
    searchInterest_val = GLineEdit_110.get()
    celsius_val = GLineEdit_296.get()
    ppt_val = GLineEdit_310.get()
    
    # print (searchInterest_val)
    # print (celsius_val)
    # print (ppt_val)
    
    #Load the Model
    # load the model from disk
    filename = '../TPA_model.sav'
    loaded_model = joblib.load(filename)
    
    # a = 128734
    # b = 22
    # c = 33
    
    #['search_interest','avg_ppt_mm','daily_mean_celsius']
    np_array = np.empty((0, 3), int) #4 columns or 0 rows
    
    # Append a row to the 2D numpy array
    np_array = np.append(np_array, np.array([[searchInterest_val, celsius_val, ppt_val]]), axis=0)
    
    predicted_val_dec = loaded_model.predict(np_array)
    predicted_val = round(predicted_val_dec[0])
    #predicted_val
    
    GLabel_694=tk.Label(root)
    GLabel_694["bg"] = "#62a0d0"
    ft = tkFont.Font(family='calibri',size=10)
    GLabel_694["font"] = ft
    GLabel_694["fg"] = "#ffffff"
    GLabel_694["justify"] = "center"
    GLabel_694["text"] = "Predicted Visitors\n" + str(predicted_val)
    GLabel_694.place(x=190,y=445,width=211,height=81)
    

GButton_545=tk.Button(root)
GButton_545["bg"] = "#306fa0"
ft = tkFont.Font(family='calibri',size=10)
GButton_545["font"] = ft
GButton_545["fg"] = "#f8f8f8"
GButton_545["justify"] = "center"
GButton_545["text"] = "Predict"
GButton_545.place(x=245,y=390,width=96,height=42)
GButton_545["command"] = GButton_545_command


# GLabel_694=tk.Label(root)
# GLabel_694["bg"] = "#62a0d0"
# ft = tkFont.Font(family='calibri',size=10)
# GLabel_694["font"] = ft
# GLabel_694["fg"] = "#ffffff"
# GLabel_694["justify"] = "center"
# GLabel_694["text"] = "Predicted Visitors For Month"
# GLabel_694.place(x=190,y=445,width=211,height=81)


root.mainloop()

# if __name__ == "__main__":
#     root = tk.Tk()
#     app = App(root)
#     root.mainloop()
