import image_lib
import win32gui, win32ui, win32con, win32api
import time

#여기에 앱이름 적어주면됩니다.
appname = "LDPlayer-1"

hwnd = win32gui.FindWindow(None, appname)

def mouse_click_list(handle, img, per):
	target_list = image_lib.match_img_list(handle, img, per)
	if len(target_list) > 0:
		print(img , len(target_list))
		for _target in target_list:
			image_lib.mouse_click_fast(handle, _target[0], _target[1]-10)

while True:
	print("시작")
	# mouse_click_list(hwnd, ".\\coin_img\\b1.jpg",0.8)
	# mouse_click_list(hwnd, ".\\coin_img\\b2.jpg",0.8)
	mouse_click_list(hwnd, ".\\coin_img\\b3.jpg",0.9)
	mouse_click_list(hwnd, ".\\coin_img\\b4.jpg",0.8)
	mouse_click_list(hwnd, ".\\coin_img\\b5.jpg",0.9)
	mouse_click_list(hwnd, ".\\coin_img\\b6.jpg",0.9)
	mouse_click_list(hwnd, ".\\coin_img\\b7.jpg",0.9)