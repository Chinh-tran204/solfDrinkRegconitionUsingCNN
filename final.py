from tkinter import *
from tkinter import ttk
from PIL import ImageTk, Image
import numpy as np
from keras.models import load_model
import numpy as np
import matplotlib.pyplot as plt
from keras.utils.image_utils import load_img, img_to_array


from tkinter.messagebox import showinfo


model100 = load_model('solfDrinkReg_cnn.h5')

result = ["NONE","PEPSI", "COCA COLA", "7UP", "MIRINDA", "REVIVE", "STING"]
picDir = "D:\Study only\On school\Hoc_ki_II_nam3\AI\FINAL\python_code\\testImg"
    

def openResultWindow(result_string):
    imgDisplay = ImageTk.PhotoImage(file= picDir)
    # Toplevel object which will
    # be treated as a new window
    resultWindow = Toplevel(root)
 
    # sets the title of the
    # Toplevel widget
    resultWindow.title("OBJECT")
 
    # sets the geometry of toplevel
    resultWindow.geometry("400x400")
    x_pos = root.winfo_x()
    y_pos = root.winfo_y()
    
    resultWindow.geometry("+%d+%d" %(x_pos+200,y_pos+180))
    labelImgff = Label(resultWindow, image = imgDisplay, bg="white")
    labelImgff.grid(row=0, column=0)
    labelImgff.place(x=200, y=200, anchor= CENTER)
    
    # A Label widget to show in toplevel
    Label(resultWindow,
          text =result_string,
              font="Arial 15 bold").pack()
    resultWindow.mainloop()


def drinkChanged(event):
    # Lay gia tri combox
    drinkName = selected_drink.get()
    global picDir
    
	# load lai gia tri pic Dir
    if (drinkName == "PEPSI"):
        picDir = "D:\Study only\On school\Hoc_ki_II_nam3\AI\FINAL\python_code\\testImg\pepsi.png"
    if (drinkName == "COCA COLA"):
        picDir = "D:\Study only\On school\Hoc_ki_II_nam3\AI\FINAL\python_code\\testImg\coca.png"
    if (drinkName == "7UP"):
        picDir = "D:\Study only\On school\Hoc_ki_II_nam3\AI\FINAL\python_code\\testImg\sevenUp.png"
    if (drinkName == "MIRINDA"):
        picDir = "D:\Study only\On school\Hoc_ki_II_nam3\AI\FINAL\python_code\\testImg\mirinda.png"
    if (drinkName == "REVIVE"):
        picDir = "D:\Study only\On school\Hoc_ki_II_nam3\AI\FINAL\python_code\\testImg\\revive.png"
    if (drinkName == "STING"):
        picDir = "D:\Study only\On school\Hoc_ki_II_nam3\AI\FINAL\python_code\\testImg\sting.png"
    showinfo(
        title='Result',
        message=f'You selected {selected_drink.get()}!'
    )



def regconition(picDirection):

	img = load_img(picDirection,target_size= (256,256))
	img = img_to_array(img)
	img = img.reshape(1,256,256,3)
	img = img.astype('float32')
	img = img/255
	result_index = np.argmax(model100.predict(img), axis = -1)
	result_str = "This is: " + result[result_index[0]]
	return result_str


# BUTTON FUNC
def main_program():
    result_str = regconition(picDir)
    openResultWindow(result_str)

################################################## TUỲ CHỈNH GIAO DIỆN #################################################
### Tạo cửa sổ giao diện chính với kích cỡ 1280x720
root = Tk()
root.title("SOLF DRINK REG UI")
root.geometry("1280x720")



# Tao ra combobox
selected_drink = StringVar()
drinks = ttk.Combobox(root, textvariable=selected_drink)
drinks['value'] = ["PEPSI", "COCA COLA", "7UP", "MIRINDA", "REVIVE", "STING"]
# chi cho doc gia tri tu combobox
drinks['state'] = 'readonly'
# setup vi tri comboBox
drinks.pack(fill=X, padx=5, pady=110)
drinks.bind('<<ComboboxSelected>>', drinkChanged)



#Setup vị trí logo trường (góc trái dưới)
lgtruong = ImageTk.PhotoImage(Image.open("layout\logotruong.png"))
lblgtruong = Label(image= lgtruong)
lblgtruong.place(x = 20, y = 570)


#Setup vị trí tên của khoa (góc phỉa dưới)
textl2 = Label(root, text="Faculty Of Mechanical Engineering", font="Arial 15 bold", fg="darkblue")
textl3 = Label(root, text="Mechatronics Engineering", font="Arial 15 bold", fg="darkblue")
textl2.place(x = 1100, y = 650,anchor = CENTER)
textl3.place(x = 1100, y = 680,anchor = CENTER)




#Setup vị trí tên đề tài (trên cùng ở giữa màn hình)
textl4 = Label(root, text="SOLF DRINK REGCONITION USING CNN", font="Arial 23 bold", fg="red")
textl4.place(x = 640, y = 30,anchor = CENTER)

#Setup vị trí thôgn tin đi kèm (ngay dưới tên đề tài)
myLabel5 = Label(root, text="Subject: AI -Artificial Intelligence", font="Arial 15 bold")
myLabel6 = Label(root, text="Instructors: PGS. Nguyen Truong Thinh", font="Arial 15 bold")
myLabel5.place(x = 640, y = 60,anchor = CENTER)
myLabel6.place(x = 640, y = 90,anchor = CENTER)


#Setup sign ()
myLabel7 = Label(root, text="Author:", font="Arial 15 bold", fg="darkblue")
myLabel8 = Label(root, text="TRẦN HỮU CHÍNH - 20146480", font="Arial 15 bold")
myLabel7.place(x = 800, y = 150)
myLabel8.place(x = 900, y = 150)




################################################## SETUP BTN TƯƠNG TÁC #####################################################
#Start Reg button
btnLaunch = Button(root,text="START",font="Arial 30 bold", fg="red", command=main_program)
btnLaunch.place(x = 1000, y =280, anchor = CENTER)


#Stop Button
btnStop = Button(root,text="QUIT",font="Arial 30 bold", fg="red", command=root.destroy)
btnStop.place(x = 1000, y =380, anchor = CENTER)


#Combo box list


# Gọi vòng lặp sự kiện chính để các hành động có thể diễn ra trên màn hình máy tính của người dùng
root.mainloop()

