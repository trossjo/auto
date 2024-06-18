import image_lib
import win32gui, win32ui, win32con, win32api
import time

#여기에 앱이름 적어주면됩니다.
appname = "LDPlayer-1"

hwnd = win32gui.FindWindow(None, appname)

while True:
	print("시작")
	b1 = image_lib.match_img_list(hwnd, ".\\coin_img\\b1.jpg")
	if b1:
		print("b1있음", len(b1))
		for _b1 in b1:
			image_lib.mouse_click_fast(hwnd, _b1[0], _b1[1])
			print(_b1)

	b2 = image_lib.match_img_list(hwnd, ".\\coin_img\\b2.jpg")
	if b2:
		print("b2있음", len(b2))
		for _b2 in b2:
			image_lib.mouse_click_fast(hwnd, _b2[0], _b2[1])

	b3 = image_lib.match_img_list(hwnd, ".\\coin_img\\b3.jpg")
	if b3:
		print("b3있음", len(b3))
		for _b3 in b3:
			image_lib.mouse_click_fast(hwnd, _b3[0], _b3[1])

	b4 = image_lib.match_img_list(hwnd, ".\\coin_img\\b4.jpg")
	if b4:
		print("b4있음", len(b4))
		for _b4 in b4:
			image_lib.mouse_click_fast(hwnd, _b4[0], _b4[1])

	b5 = image_lib.match_img_list(hwnd, ".\\coin_img\\b5.jpg")
	if b5:
		print("b5있음", len(b5))
		for _b5 in b5:
			image_lib.mouse_click_fast(hwnd, _b5[0], _b5[1])

	b6 = image_lib.match_img_list(hwnd, ".\\coin_img\\b6.jpg")
	if b6:
		print("b6있음", len(b6))
		for _b6 in b6:
			image_lib.mouse_click_fast(hwnd, _b6[0], _b6[1])
	b7 = image_lib.match_img_list(hwnd, ".\\coin_img\\b7.jpg")
	if b7:
		print("b6있음", len(b7))
		for _b7 in b7:
			image_lib.mouse_click_fast(hwnd, _b7[0], _b7[1])