import tkinter
import numpy as np
import cv2
from PIL import Image
from PIL import ImageTk

window = tkinter.Tk()
c = tkinter.Canvas(window, width=600, height=600)
c.pack()

# vc = cv2.VideoCapture(0)

# if vc.isOpened():
#     is_capturing, frame = vc.read()
#     frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
# else:
#     is_capturing = False
    
# vc.release()

frame = cv2.imread('old.jpg')
frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
img = Image.fromarray(frame)
img = ImageTk.PhotoImage(img)

c.create_image((0, 0), anchor = tkinker.NW, image=img)
# while is_capturing:
#     try:
#         is_capturing, frame = vc.read()
#         frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
#         webcam_preview.set_data(frame)
#         plt.draw()
#         display.clear_output(wait=True)
#         display.display(plt.gcf())
#         oldframe = frame
#         plt.pause(0.1)
#     except KeyboardInterrupt:
#         vc.release()



window.mainloop()