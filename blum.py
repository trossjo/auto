import image_lib
import win32gui, win32ui, win32con, win32api
import time

#여기에 앱이름 적어주면됩니다.
appname = "LDPlayer-1"

hwnd = win32gui.FindWindow(None, appname)

mouse_p = None

while True:
	print("시작")
	b1 = image_lib.match_img(hwnd, ".\\coin_img\\b1.jpg",0.7)
	if b1:
		print("b1있음")
		image_lib.mouse_click(hwnd, b1[0], b1[1])

	b2 = image_lib.match_img(hwnd, ".\\coin_img\\b2.jpg",0.7)
	if b2:
		print("b2있음")
		image_lib.mouse_click(hwnd, b2[0], b2[1])

	b3 = image_lib.match_img(hwnd, ".\\coin_img\\b3.jpg",0.7)
	if b3:
		print("b3있음")
		image_lib.mouse_click(hwnd, b3[0], b3[1])
	
	b4 = image_lib.match_img(hwnd, ".\\coin_img\\b4.jpg",0.7)
	if b4:
		print("b4있음")
		image_lib.mouse_click(hwnd, b4[0], b4[1])

	b5 = image_lib.match_img(hwnd, ".\\coin_img\\b5.jpg",0.7)
	if b5:
		print("b5있음")
		image_lib.mouse_click(hwnd, b5[0], b5[1])
	
	b6 = image_lib.match_img(hwnd, ".\\coin_img\\b6.jpg",0.7)
	if b6:
		print("b6있음")
		image_lib.mouse_click(hwnd, b6[0], b6[1])