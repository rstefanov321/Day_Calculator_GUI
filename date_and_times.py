import datetime
from datetime import date
from tkinter import *
import time
from tkinter import ttk

_DAYS_IN_MONTH = [-1, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]


class Clock(Label):
    """ A real time clock, showing the time and the date """

    def __init__(self, parent=None, seconds=True, colon=False):

        Label.__init__(self, parent)

        self.display_seconds = seconds
        if self.display_seconds:
            self.time = time.strftime("%I:%M:%S %p")
        else:
            self.time = time.strftime("%I:%M:%S %p").lstrip("0")
        self.display_time = self.time
        self.configure(text=self.display_time)

        if colon:
            self.blink_colon()

        self.after(200, self.tick)

    def blink_colon(self):
        if ":" in self.display_time:
            self.display_time = self.display_time.replace(":", " ")
        else:
            self.display_time = self.display_time.replace(" ", ":", 1)
        self.config(text=self.display_time)
        self.after(1000, self.blink_colon())

    def tick(self):
        """ Updates the display clock every 200 miliseconds"""
        if self.display_seconds:
            new_time = time.strftime("%I:%M:%S %p")
        else:
            new_time = time.strftime("%I:%M:%S %p").lstrip("0")
        if new_time != self.time:
            self.time = new_time
            self.display_time = self.time
            self.config(text=self.display_time)
        self.after(200, self.tick)


mainWindow = Tk()

mainWindow.title("Date and time calculator")
mainWindow.geometry("1040x680+250+50")
mainWindow["padx"] = 8
mainWindow["pady"] = 8

# =================== Inner title =======================
label = Label(mainWindow, text="Times of opening the program (local and UTC): ")
label.grid(row=0, column=0, columnspan=3, sticky="ew")

mainWindow.columnconfigure(0, weight=10)
mainWindow.columnconfigure(1, weight=10)
mainWindow.columnconfigure(2, weight=10)

mainWindow.rowconfigure(0, weight=1)
mainWindow.rowconfigure(1, weight=0)
mainWindow.rowconfigure(2, weight=2)
mainWindow.rowconfigure(3, weight=0)
mainWindow.rowconfigure(4, weight=1)
mainWindow.rowconfigure(5, weight=2)
mainWindow.rowconfigure(6, weight=2)
mainWindow.rowconfigure(7, weight=2)
mainWindow.rowconfigure(8, weight=3)
mainWindow.rowconfigure(9, weight=2)

# =================== Labels for the times of opening the program =======================
fromLabel = Label(mainWindow, text="Local Time: ")
fromLabel.grid(row=1, column=0, sticky="ew")

toLabel = Label(mainWindow, text="UTC Time: ")
toLabel.grid(row=1, column=2, sticky="ew")

# =================== Time NOW =======================
now = datetime.datetime.now()
current_time = now.strftime("%y-%m-%d %H:%M:%S")
nowLabel = Label(mainWindow, text=current_time)
nowLabel.grid(row=2, column=0, sticky="nsew")
nowLabel.config(border=3, relief="raised", font=("arial", 14))
nowLabel["pady"] = 8

utc = datetime.datetime.utcnow()
utc_time = utc.strftime("%y-%m-%d %H:%M:%S")
utcLabel2 = Label(mainWindow, text=utc_time)
utcLabel2.grid(row=2, column=2, sticky="nsew")
utcLabel2.config(border=3, relief="raised", font=("arial", 14))
utcLabel2["pady"] = 8

# ########################################   "BEGIN" FRAME   ############################################################

# =================== Date Frame BEGIN =======================
dateFrame = LabelFrame(mainWindow, text="Date FROM: ")
dateFrame.grid(row=4, column=0, columnspan=3, sticky="nsew")

# =================== Label for the BEGIN times =======================

yearlabel = Label(dateFrame, text="year:")
monthlabel = Label(dateFrame, text="month:")
daylabel = Label(dateFrame, text="day:")

yearlabel.grid(row=0, column=0)
monthlabel.grid(row=0, column=2)
daylabel.grid(row=0, column=4)

# =================== Combo boxes for the BEGIN times =======================
# creating the list of the years to choose from (can be altered anytime)
years_list = []
for i in range(1990, 2201):
    years_list.append(i)

_DAYS_IN_MONTH = [-1, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]


def pick_days(e):
    """decides if the year is a leap one and to output 29 days in Feb"""
    if int(mo_combo.get()) == 2 and int(yr_combo.get()) % 4 == 0:
        day_combo.current(0)
        return day_combo.config(value=list(range(1, 30)))

    else:
        day_combo.current(0)
        return day_combo.config(value=list(range(1, _DAYS_IN_MONTH[int(mo_combo.get())] + 1)))


# create a combo box for the year
yr_combo = ttk.Combobox(dateFrame, value=years_list)
yr_combo.current(0)
yr_combo.grid(row=0, column=1, sticky="ew")

# create a combo box for the month
months = list(range(1, 13))
mo_combo = ttk.Combobox(dateFrame, value=months)
mo_combo.current(0)
mo_combo.grid(row=0, column=3, sticky="ew")

# create a combo box for the day
day_combo = ttk.Combobox(dateFrame, value=list(range(1, _DAYS_IN_MONTH[1] + 1)))
day_combo.current(0)
day_combo.grid(row=0, column=5, sticky="ew")

# bind the combo boxes
yr_combo.bind("<<ComboboxSelected>>", pick_days)
mo_combo.bind("<<ComboboxSelected>>", pick_days)


# ==================== CHOICE BUTTON "FROM" ==============================
def choice_update():
    """Gets the values for the year, month and day of the combo boxes"""
    choice_label.config(
        text="The date you chose is {0}-{1}-{2}".format(yr_combo.get(), mo_combo.get(), day_combo.get()),
        bg="red")


choice_button = Button(dateFrame, text="CLICK TO UPDATE", relief="groove", command=choice_update)
choice_button.grid(row=1, column=6, sticky="ew")
choice_button["padx"] = 15

# ==================== CHOICE LABEL "END" ==============================
# The label shows the chosen date
choice_label = Label(dateFrame)
choice_label.grid(row=1, column=7, sticky="nsew")

# ########################################    END FRAME   ############################################################

# =================== Date Frame END =======================
dateFrame = LabelFrame(mainWindow, text="Date TO: ")
dateFrame.grid(row=5, column=0, columnspan=3, sticky="nsew")

yearlabel = Label(dateFrame, text="year:")
monthlabel = Label(dateFrame, text="month:")
daylabel = Label(dateFrame, text="day:")

yearlabel.grid(row=0, column=0)
monthlabel.grid(row=0, column=2)
daylabel.grid(row=0, column=4)


# =================== Combo boxes for the END date =======================
def pick_days(e):
    if int(mo_combo_end.get()) == 2 and int(yr_combo_end.get()) % 4 == 0:
        day_combo_end.current(0)
        return day_combo_end.config(value=list(range(1, 30)))
    else:
        day_combo_end.current(0)
        return day_combo_end.config(value=list(range(1, _DAYS_IN_MONTH[int(mo_combo_end.get())] + 1)))


# Create a combo box for the END year
yr_combo_end = ttk.Combobox(dateFrame, value=years_list)
yr_combo_end.current(0)
yr_combo_end.grid(row=0, column=1, sticky="ew")

# Create a combo box for the END month
months = list(range(1, 13))
mo_combo_end = ttk.Combobox(dateFrame, value=months)
mo_combo_end.current(0)
mo_combo_end.grid(row=0, column=3, sticky="ew")

# Create a combo box for the END day
day_combo_end = ttk.Combobox(dateFrame, value=list(range(1, _DAYS_IN_MONTH[1] + 1)))
day_combo_end.current(0)
day_combo_end.grid(row=0, column=5, sticky="ew")

# bind the combo boxes
yr_combo_end.bind("<<ComboboxSelected>>", pick_days)
mo_combo_end.bind("<<ComboboxSelected>>", pick_days)


# ==================== CHOICE BUTTON "END" ==============================
def choice_update_end():
    """Gets the values for the year, month and day of the combo boxes from the END frame"""
    choice_label_end.config(
        text="The date you chose is {0}-{1}-{2}".format(yr_combo_end.get(), mo_combo_end.get(), day_combo_end.get()),
        bg="red")


choice_button_end = Button(dateFrame, text="CLICK TO UPDATE", relief="groove", command=choice_update_end)
choice_button_end.grid(row=1, column=6, sticky="ew")
choice_button_end["padx"] = 15

# ==================== CHOICE LABEL "END" ==============================
# The label shows the chosen date
choice_label_end = Label(dateFrame)
choice_label_end.grid(row=1, column=7, sticky="nsew")

# ==================== Creating the frame outputting the result ==============================
result_frame = LabelFrame(mainWindow, text="Days between the dates: ")
result_frame.grid(row=6, column=0, columnspan=3, sticky="nsew")

result_label = Label(result_frame, text="And the days are: ")
result_label.grid(row=0, column=0)

final_label = Label(result_frame)
final_label.grid(row=0, column=1, sticky="nsew")
final_label.config(font=("arial", 35))


def time_calc():
    """ The function that calculates the days between two dates"""
    diff = abs((date(int(yr_combo.get()), int(mo_combo.get()), int(day_combo.get())) - date(int(yr_combo_end.get()), int(mo_combo_end.get()),
                                                                                            int(day_combo_end.get()))).days)
    final_label.config(text="{} days".format(diff), fg="green")


myButton = Button(result_frame, text="Calculate the time difference now!", command=time_calc)
myButton.grid(row=1, column=3, columnspan=2, sticky="ew")

# ################## HOW MANY DAYS HAVE YOU LIVED FOR? FRAME ######################################

life_frame = LabelFrame(mainWindow, text="How many days have you lived for?")
life_frame.grid(row=7, column=0, columnspan=3, sticky="nsew")


yearlabel = Label(life_frame, text="year:")
monthlabel = Label(life_frame, text="month:")
daylabel = Label(life_frame, text="day:")

yearlabel.grid(row=0, column=0)
monthlabel.grid(row=0, column=2)
daylabel.grid(row=0, column=4)


# =================== Combo boxes for the chosen BD =======================
def pick_days_bd(e):
    if int(mo_bd.get()) == 2 and int(yr_bd.get()) % 4 == 0:
        d_bd.current(0)
        return d_bd.config(value=list(range(1, 30)))
    else:
        d_bd.current(0)
        return d_bd.config(value=list(range(1, _DAYS_IN_MONTH[int(mo_bd.get())] + 1)))


# create a combo box for the year
yr_bd = ttk.Combobox(life_frame, value=years_list)
yr_bd.current(0)
yr_bd.grid(row=0, column=1, sticky="ew")

# Create a combo box for the month
months = list(range(1, 13))
mo_bd = ttk.Combobox(life_frame, value=months)
mo_bd.current(0)
mo_bd.grid(row=0, column=3, sticky="ew")

# Create a combo box for the day
d_bd = ttk.Combobox(life_frame, value=list(range(1, _DAYS_IN_MONTH[1] + 1)))
d_bd.current(0)
d_bd.grid(row=0, column=5, sticky="ew")

# bind the combo boxes
yr_bd.bind("<<ComboboxSelected>>", pick_days_bd)
mo_bd.bind("<<ComboboxSelected>>", pick_days_bd)


# ====== creating the button to automatically get the difference between the BD and today. =====

def bd_calc():
    """Calculates the days from the birthday until today"""
    diff = abs((date(int(yr_bd.get()), int(mo_bd.get()), int(d_bd.get())) - datetime.date.today()).days)
    bd_label.config(text="{} days".format(diff), fg="green")


result_label = Label(life_frame, text="And the days you've lived for are: ")
result_label.grid(row=3, column=0)

bd_label = Label(life_frame)
bd_label.grid(row=3, column=1, sticky="nsew")
bd_label.config(font=("arial", 15))

bdButton = Button(life_frame, text="Calculate the day difference now!", command=bd_calc)
bdButton.grid(row=2, column=6, sticky="ew")


# ============== Real Time clock ===================
clock1 = Clock(mainWindow)
clock1.grid(row=8, column=0, columnspan=2, sticky="nsew")
clock1.configure(bg='black', fg='white', font=("helvetica", 15))

w = Label(mainWindow, text=f"{datetime.datetime.now():%a, %b, %d, %Y}",
          fg="white", bg="black", font=("helvetica", 15))
w.grid(row=8, column=2, sticky="nsew")

# =================== Close button =======================
closeButton = Button(mainWindow, text="Close", command=mainWindow.destroy)
closeButton.grid(row=9, column=2, sticky="e")
closeButton["padx"] = 15

mainWindow.mainloop()


