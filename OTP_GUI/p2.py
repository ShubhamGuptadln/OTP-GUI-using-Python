from tkinter import *
from tkinter import messagebox

from twilio.rest import Client
import random
import time


class otp_verifier(Tk):
    def __init__(self):
        super().__init__()
        self.geometry("1000x580+200+80")
        self.configure(bg="#FFFFFF")  # background White
        self.resizable(False, False)
        self.n = str(self.OTP())
        self.client = Client("ACe1a0e7ed2c1495ec617d07143569ea41", "d1e706fa13f96c6c9c293e5c23dd93ec")
        self.client.messages.create(to="+91-6387251870",
                                    from_="+13342342546",
                                    body=self.n
                                    )
        self.minuteString = StringVar()
        self.secondString = StringVar()

        ### Set strings to default value
        self.minuteString.set("1")
        self.secondString.set("00")



    def Labels(self):
        self.c = Canvas(self, bg="#808080", width=400, height=280)
        self.c.place(x=290, y=120)

        self.minuteTextbox = Entry(self, width=2, bg="#808080", font=("Calibri", 20, ""),
                                   textvariable=self.minuteString)
        self.secondTextbox = Entry(self, width=2, bg="#808080", font=("Calibri", 20, ""),
                                   textvariable=self.secondString)

        ### Center textboxes

        self.minuteTextbox.place(x=460, y=270)
        self.secondTextbox.place(x=500, y=270)

        self.upper_frame = Frame(self, bg="#468284", width=1500, height=130)
        self.upper_frame.place(x=0, y=0)

        self.picture = PhotoImage(file="password1.png")
        self.k = Label(self.upper_frame, image=self.picture, bg="#468284").place(x=190, y=35)

        self.j = Label(self.upper_frame, text="Verify OTP", font="TimesNewRoman 38 bold", bg="#468284",
                       fg="white").place(x=290, y=35)

    def Entry(self):
        self.User_Name = Text(self, font="calibri 20", borderwidth=2, wrap=WORD, width=23, height=1)
        self.User_Name.place(x=330, y=200)

    def OTP(self):
        return random.randrange(10000, 100000)

    def Buttons(self):
        self.submitButtonImage = PhotoImage(file="submit.png")
        self.submitButton = Button(self, image=self.submitButtonImage,  command = lambda:[self.checkOTP(), self.runTimer()], border = 0 )
        self.submitButton.place(x=440, y=330)

        self.resendOTPImage = PhotoImage(file="resendotp.png")
        self.resendButton = Button(self, image=self.resendOTPImage, command=self.resendOTP, border=0)
        self.resendButton.place(x=420, y=430)

    def resendOTP(self):
        self.n=str(self.OTP())
        self.client = Client("ACe1a0e7ed2c1495ec617d07143569ea41", "d1e706fa13f96c6c9c293e5c23dd93ec")
        self.client.messages.create(to="+91-6387251870",
                                    from_="+13342342546",
                                    body=self.n
                                    )

    def checkOTP(self):
        try:
            self.userInput = int(self.User_Name.get(1.0, "end-1c"))
            if self.userInput == int(self.n):
                messagebox.showinfo("showinfo", "Verification Successful")
                self.n = "done"

            else:
                messagebox.showinfo("showinfo", "Wrong OTP")

        except:
            messagebox.showinfo("showinfo", "INVALID OTP")

    def runTimer(self):

        self.clockTime = int(self.minuteString.get()) * 60 + int(self.secondString.get())

        while (self.clockTime > -1):

            totalMinutes, totalSeconds = divmod(self.clockTime, 60)

            self.minuteString.set("{0:2d}".format(totalMinutes))
            self.secondString.set("{0:2d}".format(totalSeconds))

            ### Update the interface
            self.update()
            time.sleep(1)

            ### Let the user know if the timer has expired
            if (self.clockTime == 0):
                messagebox.showinfo("", "Your time has expired!")

            self.clockTime -= 1


if __name__ == "__main__":
    window = otp_verifier()
    window.Labels()
    window.Entry()
    window.OTP()
    window.update()
    window.Buttons()
    window.update()

    window.mainloop()
