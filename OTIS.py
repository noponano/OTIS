import tkinter as tk
import time
import serial
import threading
import continuous_threading


#ser = serial.Serial('COM8',9600)
ser=serial.Serial('/dev/ttyACM0',115200)
val1 = 0

index = []
def update():
    T.destroy()

def readserial():
    global val1
    ser_bytes = ser.readline()
    ser_bytes = ser_bytes.decode("utf-8")
    print(ser_bytes.rstrip())
    val1 = ser_bytes
    index_T=val1.index('T')
    index_A=val1.index('A')
    index_B=val1.index('B')
    Target=val1[index_T+1:index_A]
    Absolute=val1[index_A+1:index_B]
    Balance=val1[index_B+1:]
    
    T = tk.Label(root,text="                                         ",bg="black",fg="red",font=("7 Segment none just",120)).place(x=700,y=0)
    T = tk.Label(root,text=Target,bg="black",fg="red",font=("7 Segment none just",120)).place(x=700,y=0)
    A = tk.Label(root,text="                                         ",bg="black",fg="red",font=("7 Segment none just",120)).place(x=700,y=400)
    A = tk.Label(root,text=Absolute,bg="black",fg="red",font=("7 Segment none just",120)).place(x=700,y=400)
    B = tk.Label(root,text="                                         ",bg="black",fg="red",font=("7 Segment none just",120)).place(x=700,y=800)
    B = tk.Label(root,text=Balance,bg="black",fg="red",font=("7 Segment none just",120)).place(x=700,y=800)
    
    time.sleep(0.5)

t1 = continuous_threading.PeriodicThread(0.5, readserial)

std_size_w, std_size_h = "2500","1500"

root = tk.Tk()
root.geometry(f"{std_size_w}x{std_size_h}")
root.minsize(width = (int(std_size_w)), height = ((int(std_size_h))-300))
root.configure(background="black")

# tab2 = LabelFrame(tab_setup)
# tab_setup.add(tab2, text = "OTIS")
# 
# tab_setup.pack(expand=1, fill = "both", padx = 10, pady = 10)


# canvas1 = Canvas(tab2, width = 2500, height = 2500, bg = "black") 
# canvas1.pack()

w = tk.Label(root,text="Target",bg="black",fg="red",font=("7 Segment none just",120)).place(x=0,y=0)
w1 = tk.Label(root,text="Actual",bg="black",fg="red",font=("7 Segment none just",120)).place(x=0,y=400)
w2 = tk.Label(root,text="Balance",bg="black",fg="red",font=("7 Segment none just",120)).place(x=0,y=800)
t1.start()
#t1.join()

root.mainloop()