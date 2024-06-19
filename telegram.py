import image_lib
import win32gui, win32ui, win32con, win32api
import time

#여기에 앱이름 적어주면됩니다.
appname = "LDPlayer-1"

hwnd = win32gui.FindWindow(None, appname)


check = 0
while True:
	check += 1
	print(check)

	싸움 = image_lib.match_img(hwnd, ".\\coin_img\\fight.jpg")
	if 싸움:
		check = 0
		매크로종료 = image_lib.match_img(hwnd, ".\\coin_img\\macro_stop.jpg")
		if 매크로종료:
			image_lib.mouse_click(hwnd, 매크로종료[0], 매크로종료[1])
		time.sleep(1)
		image_lib.mouse_click(hwnd, 싸움[0], 싸움[1])
		매크로시작 = image_lib.match_img(hwnd, ".\\coin_img\\macro_start.jpg")
		if 매크로시작:
			image_lib.mouse_click(hwnd, 매크로시작[0], 매크로시작[1]-20)

	새게임 = image_lib.match_img(hwnd, ".\\coin_img\\fight2.jpg")
	if 새게임:
		check = 0
		매크로종료 = image_lib.match_img(hwnd, ".\\coin_img\\macro_stop.jpg")
		if 매크로종료:
			image_lib.mouse_click(hwnd, 매크로종료[0], 매크로종료[1])
		time.sleep(1)
		image_lib.mouse_click(hwnd, 새게임[0], 새게임[1])
		매크로시작 = image_lib.match_img(hwnd, ".\\coin_img\\macro_start.jpg")
		if 매크로시작:
			image_lib.mouse_click(hwnd, 매크로시작[0], 매크로시작[1]-20)

	싸움탭 = image_lib.capture_click(hwnd, ".\\coin_img\\f_tab.jpg",0.98)
	if 싸움탭:
		매크로종료 = image_lib.match_img(hwnd, ".\\coin_img\\macro_stop.jpg")
		if 매크로종료:
			image_lib.mouse_click(hwnd, 매크로종료[0], 매크로종료[1])
			time.sleep(1)
			image_lib.mouse_click(hwnd, 싸움탭[0], 싸움탭[1])

	텔레그램 = image_lib.capture_click(hwnd, ".\\coin_img\\tel.jpg")
	if 싸움탭:
		매크로종료 = image_lib.match_img(hwnd, ".\\coin_img\\macro_stop.jpg")
		if 매크로종료:
			image_lib.mouse_click(hwnd, 매크로종료[0], 매크로종료[1])
			time.sleep(1)
			image_lib.mouse_click(hwnd, 텔레그램[0], 텔레그램[1]-5)

	텔레그램채팅 = image_lib.capture_click(hwnd, ".\\coin_img\\tel_chat.jpg")
	if 싸움탭:
		매크로종료 = image_lib.match_img(hwnd, ".\\coin_img\\macro_stop.jpg")
		if 매크로종료:
			image_lib.mouse_click(hwnd, 매크로종료[0], 매크로종료[1]-20)
			time.sleep(1)
			image_lib.mouse_click(hwnd, 텔레그램채팅[0], 텔레그램채팅[1])

	텔레그램채팅2 = image_lib.capture_click(hwnd, ".\\coin_img\\tel_chat2.jpg")
	if 싸움탭:
		매크로종료 = image_lib.match_img(hwnd, ".\\coin_img\\macro_stop.jpg")
		if 매크로종료:
			image_lib.mouse_click(hwnd, 매크로종료[0], 매크로종료[1])
			time.sleep(1)
			image_lib.mouse_click(hwnd, 텔레그램채팅2[0], 텔레그램채팅2[1])

	if check > 35:
		check = 0
		매크로종료 = image_lib.match_img(hwnd, ".\\coin_img\\macro_stop.jpg")
		if 매크로종료:
			image_lib.mouse_click(hwnd, 매크로종료[0], 매크로종료[1])
		time.sleep(3)
		게임종료 = image_lib.match_img(hwnd, ".\\coin_img\\x.jpg")
		if 게임종료:
			image_lib.mouse_click(hwnd, 게임종료[0], 게임종료[1])
		time.sleep(3)
		게임종료2 = image_lib.match_img(hwnd, ".\\coin_img\\x2.jpg")
		if 게임종료2:
			image_lib.mouse_click(hwnd, 게임종료2[0], 게임종료2[1]-25)
		time.sleep(3)

	time.sleep(1)