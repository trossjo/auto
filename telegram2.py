import image_lib
import win32gui, win32ui, win32con, win32api
import time

#여기에 앱이름 적어주면됩니다.
appname = "LDPlayer-2"

hwnd = win32gui.FindWindow(None, appname)


check = 0
while True:
	check += 1
	싸움 = image_lib.match_img(hwnd, ".\\coin_img\\fight.jpg")
	if 싸움:
		check = 0
		매크로종료 = image_lib.match_img(hwnd, ".\\coin_img\\macro_stop.jpg",0.98)
		if 매크로종료:
			image_lib.mouse_click(hwnd, 매크로종료[0], 매크로종료[1])

		image_lib.mouse_click(hwnd, 싸움[0], 싸움[1])
		time.sleep(1)
		매크로시작 = image_lib.match_img(hwnd, ".\\coin_img\\macro_start.jpg",0.98)
		if 매크로시작:
			image_lib.mouse_click(hwnd, 매크로시작[0], 매크로시작[1]-20)

	새게임 = image_lib.match_img(hwnd, ".\\coin_img\\fight2.jpg")
	if 새게임:
		check = 0
		매크로종료 = image_lib.match_img(hwnd, ".\\coin_img\\macro_stop.jpg",0.98)
		if 매크로종료:
			image_lib.mouse_click(hwnd, 매크로종료[0], 매크로종료[1])

		image_lib.mouse_click(hwnd, 새게임[0], 새게임[1])
		time.sleep(1)
		매크로시작 = image_lib.match_img(hwnd, ".\\coin_img\\macro_start.jpg",0.98)
		if 매크로시작:
			image_lib.mouse_click(hwnd, 매크로시작[0], 매크로시작[1]-20)

	싸움탭 = image_lib.capture_click(hwnd, ".\\coin_img\\f_tab.jpg",0.98)
	if 싸움탭:
		매크로종료 = image_lib.match_img(hwnd, ".\\coin_img\\macro_stop.jpg",0.98)
		if 매크로종료:
			image_lib.mouse_click(hwnd, 매크로종료[0], 매크로종료[1]-20)
			image_lib.mouse_click(hwnd, 싸움탭[0], 싸움탭[1])

	time.sleep(1)