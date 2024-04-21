from tkinter import *
root = Tk()
root.title("Fibonacci")
root.geometry("400x400")
label_series = Label(root, text="Fibonacci serires: ")
label_sum = Label(root, text="Sum: ")
entry = Entry(root)
def Fibonacci():
    num = int(entry.get())
    counter = 1
    sum = 0
    sum2 = 0
    first_no = 0
    second_no = 1
    while(counter <= num):
        label_series["text"] += str(sum) + " "
        label_sum["text"] = "fibonacci sum: " + str(sum2) 
        counter = counter + 1
        first_no = second_no
        second_no = sum
        sum = first_no + second_no
        sum2 = sum + sum2
entry.pack()
btn = Button(root, text="Show fibonacci series", command=Fibonacci)
btn.pack()
label_series.pack()
label_sum.pack()
root.mainloop()