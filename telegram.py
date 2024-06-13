import image_lib
import win32gui, win32ui, win32con, win32api
import time

#여기에 앱이름 적어주면됩니다.
appname = "LDPlayer-1"

hwnd = win32gui.FindWindow(None, appname)


test = image_lib.match_img(hwnd, ".\\coin_img\\test.png", 0.92)
image_lib.mouse_click(test[0], test[1])
exit()
mouse_p = None

while True:
	#실행중인지 확인 50 넘으면 재시작
	check = 0
	while True:

		_11 = image_lib.match_img(hwnd, ".\\coin_img\\11.jpg", 0.92)
		_1 = image_lib.match_img(hwnd, ".\\coin_img\\1.jpg", 0.92)
		_3 = image_lib.match_img(hwnd, ".\\coin_img\\3.jpg", 0.92)
		_21 = image_lib.match_img(hwnd, ".\\coin_img\\21.jpg", 0.92)

		if _11:
			print("오른쪽아래")
			mouse_p = [_11[0]-10, _11[1]-50]
			break

		elif _1:
			print("왼쪽아래")
			mouse_p = [_1[0]+50, _1[1]-10]
			break

		elif _3:
			print("왼쪽위")
			mouse_p = [_3[0]+50, _3[1]+10]
			break

		elif _21:
			print("오른쪽위")
			mouse_p = [_21[0]-50, _21[1]+10]
			break

		else:
			check += 1
			print(check)


			fight2 = image_lib.match_img(hwnd, ".\\coin_img\\fight2.jpg", 0.95)

			if fight2:
				time.sleep(1)
				image_lib.mouse_click(hwnd, fight2[0], fight2[1])
				time.sleep(4)

			fight = image_lib.match_img(hwnd, ".\\coin_img\\fight.jpg", 0.95)

			if fight:
				time.sleep(1)
				image_lib.mouse_click(hwnd, fight[0], fight[1])
				time.sleep(4)

			a = image_lib.match_img(hwnd, ".\\coin_img\\a.jpg")

			if a:
				image_lib.mouse_click(hwnd, a[0], a[1])
				time.sleep(1)
			b = image_lib.match_img(hwnd, ".\\coin_img\\b.jpg")

			if b:
				image_lib.mouse_click(hwnd, b[0], b[1])
				time.sleep(1)

			if mouse_p:

				image_lib.mouse_click(hwnd, mouse_p[0], mouse_p[1])
				image_lib.mouse_click(hwnd, mouse_p[0], mouse_p[1])

			if check > 50:
				#재시작
				image_lib.capture_click(hwnd, ".\\coin_img\\x.jpg")
				time.sleep(3)
				image_lib.capture_click(hwnd, ".\\coin_img\\x2.jpg")
				time.sleep(3)
				image_lib.capture_click(hwnd, ".\\coin_img\\start.jpg")
				time.sleep(3)
				image_lib.capture_click(hwnd, ".\\coin_img\\start2.jpg")
				time.sleep(3)
				check = 0

	# 이거 숫자 조절 또는 mouse_click 함수에서 sleep 조절
	for i in range(38):
		if mouse_p:
			image_lib.mouse_click(hwnd, mouse_p[0], mouse_p[1])
	print("다시")