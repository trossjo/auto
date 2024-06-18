import image_lib
import win32gui, win32ui, win32con, win32api
import time

#여기에 앱이름 적어주면됩니다.
appname = "LDPlayer-1"

hwnd = win32gui.FindWindow(None, appname)

while True:
	print("시작")
	image_lib.capture_click(hwnd, ".\\coin_img\\b1.jpg",0.8)
	image_lib.capture_click(hwnd, ".\\coin_img\\b2.jpg",0.8)
	image_lib.capture_click(hwnd, ".\\coin_img\\b3.jpg",0.8)
	image_lib.capture_click(hwnd, ".\\coin_img\\b4.jpg",0.8)
	image_lib.capture_click(hwnd, ".\\coin_img\\b5.jpg",0.8)
	image_lib.capture_click(hwnd, ".\\coin_img\\b6.jpg",0.8)
	image_lib.capture_click(hwnd, ".\\coin_img\\b7.jpg",0.8)
