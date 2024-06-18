import sys
import cv2, time, math, re
import pyautogui
# import pytesseract.pytesseract
import win32gui, win32ui, win32con, win32api
from PIL import Image
from ctypes import windll
import numpy as np
# import matplotlib.pylab as plt
from pynput.mouse import Button, Controller
from pywinauto.application import Application
import random
import pywinauto.mouse as mouse
import pywinauto.keyboard as keyboard
from pytesseract import *

# pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract'


def img2str(image, plus = None):
    if plus is None:
        plus = 3
    gray        = cv2.imread(image, cv2.IMREAD_GRAYSCALE)
    resize_img  = cv2.resize(gray, dsize=(0, 0), fx=plus, fy=plus, interpolation=cv2.INTER_LINEAR)
    img_blurred = cv2.GaussianBlur(resize_img, ksize=(3, 3), sigmaX=0)
    img_thresh  = cv2.threshold(img_blurred, 0, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)[1]
    text = pytesseract.image_to_string(img_thresh, config='-l kor')
    return text


def img2int(image, plus = None):
    if plus is None:
        plus = 3

    gray        = cv2.imread(image, cv2.IMREAD_GRAYSCALE)
    resize_img  = cv2.resize(gray, dsize=(0, 0), fx=plus, fy=plus, interpolation=cv2.INTER_LINEAR)
    img_blurred = cv2.GaussianBlur(resize_img, ksize=(3, 3), sigmaX=0)
    img_thresh  = cv2.threshold(img_blurred, 0, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)[1]

    text = pytesseract.image_to_string(img_thresh, config='--psm 7')
    res_text = text.replace("g","9").replace("d","4").replace("?","7").replace("i","1").replace("f","7").replace("ㆍ", "6")
    res_text = res_text.replace("|","1").replace(":","8").replace("J","9").replace("I","1").replace("l","1").replace("V","7")
    res_text = res_text.replace("t","7").replace("e","2").replace("b","6")

    return res_text


def getWindowList():
    def callback(hwnd, hwnd_list: list):
        title = win32gui.GetWindowText(hwnd)
        if win32gui.IsWindowEnabled(hwnd) and win32gui.IsWindowVisible(hwnd) and title:
            hwnd_list.append((title, hwnd))
        return True
    output = []
    win32gui.EnumWindows(callback, output)
    print("\n".join("{: 9d} {}".format(h, t) for t, h in output))
    return output


def find_handle(app_name):
    thelist = []
    def findit(hwnd,ctx):
        if app_name in (win32gui.GetWindowText(hwnd)).lower(): # check the title

            thelist.append(hwnd)

    win32gui.EnumWindows(findit,None)

    return thelist


def handle_click(handle):
    left, top, right, bot = win32gui.GetWindowRect(handle)
    w = right - left
    h = bot - top
    pos_x = left + w/2
    pos_y = top + h/2

    mouse_click(handle,pos_x,pos_y)


#앱 캡쳐
def capture_app(hwnd):

    # hwnd = win32gui.FindWindow(None, player)
    # hwnd = find_handle(player)[0]
    left, top, right, bot = win32gui.GetWindowRect(hwnd)
    w = right - left
    h = bot - top
    posx = left
    posy = top
    hwndDC = win32gui.GetWindowDC(hwnd)
    mfcDC = win32ui.CreateDCFromHandle(hwndDC)
    saveDC = mfcDC.CreateCompatibleDC()

    saveBitMap = win32ui.CreateBitmap()
    saveBitMap.CreateCompatibleBitmap(mfcDC, w, h)

    saveDC.SelectObject(saveBitMap)

    result = windll.user32.PrintWindow(hwnd, saveDC.GetSafeHdc(), 0)

    bmpinfo = saveBitMap.GetInfo()
    bmpstr = saveBitMap.GetBitmapBits(True)

    im = Image.frombuffer(
        'RGB',
        (bmpinfo['bmWidth'], bmpinfo['bmHeight']),
        bmpstr, 'raw', 'BGRX', 0, 1)

    win32gui.DeleteObject(saveBitMap.GetHandle())
    saveDC.DeleteDC()
    mfcDC.DeleteDC()
    win32gui.ReleaseDC(hwnd, hwndDC)
    # win32gui.ShowWindow(hwnd, 5)
    # win32gui.SetForegroundWindow(hwnd)

    if result == 1:
        # im.save('screenshot.png')
        screenshot_cv2 = cv2.cvtColor(np.array(im), cv2.COLOR_RGB2BGR)
        return screenshot_cv2, posx, posy


def capture_app_split(hwnd, image, image_name , plus_x, plus_y):

    # hwnd = win32gui.FindWindow(None, player)
    # hwnd = find_handle(player)[0]
    match_x, match_y = match_img_org(hwnd, image)

    match_img_size = (Image.open(image)).size

    start_x = match_x-int(match_img_size[0]/2)
    start_y = match_y-int(match_img_size[1]/2)

    screenshot  = Image.open('.\\screenshot.png')

    split_img   = screenshot.crop((start_x,start_y,start_x+plus_x,start_y+plus_y))
    split_img.save('%s.png' % image_name)


def capture_app_crop(hwnd, image_name, x, y , w, h):
    capture_app(hwnd)
    screenshot  = Image.open('.\\screenshot.png')

    split_img   = screenshot.crop((x,y,x+w,y+h))
    split_img.save('%s.png' % image_name)



# 윈도우 전체 캡처
def capture_win(image):
    try:
        capture = pyautogui.screenshot()
        capture.save('screenshot.png')
        screenshot = cv2.imread('screenshot.png', cv2.IMREAD_COLOR)
        template = cv2.imread(image, cv2.IMREAD_COLOR)
        match_pos = match_center_loc(screenshot, template, 0, 0)
        return match_pos
    except BaseException as e:
        print('center_win 에러')
        pass


def match_img_org(handle, image):
    screenshot, x, y = capture_app(handle)
    # screenshot = cv2.imread(
    #     'screenshot.png', cv2.IMREAD_COLOR)
    template = cv2.imread(image, cv2.IMREAD_COLOR)
    match_pos = match_center_loc_org(screenshot, template, x, y)
    return match_pos


def match_img(handle, image, per=0):

    screenshot, x, y = capture_app(handle)
    # screenshot = cv2.imread(
    #     'screenshot.png', cv2.IMREAD_COLOR)
    print(image)
    template = cv2.imread(image, cv2.IMREAD_COLOR)
    match_pos = match_center_loc(screenshot, template, x, y, per)

    return match_pos


def match_img_list(handle, image):

    screenshot, x, y = capture_app(handle)
    
    template = cv2.imread(image, cv2.IMREAD_COLOR)
    # match_list = find_green_loc_list(screenshot, x, y)
    match_list = match_center_loc_list(screenshot, template, x, y)

    return match_list

def match_coord(handle, x, y):
    all_x, all_y = capture_app(handle)
    res_x = all_x+x
    res_y = all_y+y

    return res_x, res_y





def match_center_loc_org(screen, template, x, y):
    try:
        posx = x
        posy = y
        res = cv2.matchTemplate(screen, template, cv2.TM_CCOEFF_NORMED)

        min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(res)
        # print("유사도 : "+str(max_val)+" / " + str(match_per))

        top_left = max_loc[0]+posx, max_loc[1]+posy
        top_left_org = max_loc[0], max_loc[1]
        h, w = template.shape[:2]
        x, y = int(top_left[0] + w/2), int(top_left[1] + h/2)
        x_org, y_org = int(top_left_org[0] + w/2), int(top_left_org[1] + h/2)
            # print("앱 좌표 : %s, %s" % (x_org,y_org))


        if x_org and y_org:
            return x_org, y_org
    except BaseException as e:
        print(e)
        print('center_loc 에러')
        pass

def match_center_loc(screen, template, x, y, per=0):
    x_org = None
    y_org = None
    try:
        posx = x
        posy = y
        res = cv2.matchTemplate(screen, template, cv2.TM_CCOEFF_NORMED)

        match_per = 0.91
        if per >= 0.01:
            match_per = per

        min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(res)
        # print("유사도 : "+str(max_val)+" / " + str(match_per))

        if max_val > match_per:
            top_left = max_loc[0]+posx, max_loc[1]+posy
            top_left_org = max_loc[0], max_loc[1]
            h, w = template.shape[:2]
            x, y = int(top_left[0] + w/2), int(top_left[1] + h/2)
            x_org, y_org = int(top_left_org[0] + w/2), int(top_left_org[1] + h/2)
            # print("앱 좌표 : %s, %s" % (x_org,y_org))


        if x_org and y_org:
            return x_org, y_org
    except:
        print('center_loc 에러')
        pass

def find_green_loc_list(screen, x, y):
    hsv_image = cv2.cvtColor(screen, cv2.COLOR_BGR2HSV)
    # 초록색 범위 정의 (HSV 값)
    lower_green = np.array([35, 40, 40])  # lower bound of green color
    upper_green = np.array([85, 255, 255])  # upper bound of green color

    # 초록색 범위에 해당하는 마스크 생성
    mask = cv2.inRange(hsv_image, lower_green, upper_green)

    # 원본 이미지에서 초록색 부분을 추출
    # green_areas = cv2.bitwise_and(screen, screen, mask=mask)

    # 초록색 부분을 찾아 좌표 추출
    contours, _ = cv2.findContours(mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

    # 초록색 영역의 중심 좌표 계산
    match_list = []
    for contour in contours:
        M = cv2.moments(contour)
        if M["m00"] != 0:
            cx = int(M["m10"] / M["m00"])
            cy = int(M["m01"] / M["m00"])
            match_list.append([cx, cy])

    # 너무 가까운 좌표 제거
    def is_far_enough(p1, p2, min_distance):
        distance = np.sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)
        return distance > min_distance

    min_distance = 10
    filtered_match_list = []

    for point in match_list:
        if all(is_far_enough(point, filtered_point, min_distance) for filtered_point in filtered_match_list):
            filtered_match_list.append(point)

    return filtered_match_list

def match_center_loc_list(screen, template, x, y):
    def is_far_enough(p1, p2, min_distance):
        distance = np.sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)
        return distance > min_distance

    posx = x
    posy = y
    res = cv2.matchTemplate(screen, template, cv2.TM_CCOEFF_NORMED)

    threshold = 0.8
    loc = np.where(res >= threshold)

    y_list = loc[0]
    x_list = loc[1]

    match_list = []

    h, w = template.shape[:2]

    for loc_x, loc_y in zip(x_list, y_list):
        top_left = loc_x+posx, loc_y+posy
        top_left_org = loc_x, loc_y
        x, y = int(top_left[0] + w/2), int(top_left[1] + h/2)
        x_org, y_org = int(top_left_org[0] + w/2), int(top_left_org[1] + h/2)
        # print("앱 좌표 : %s, %s" % (x_org,y_org))
        match_list.append([x_org,y_org])

    min_distance = 10
    filtered_match_list = []

    for point in match_list:
        if all(is_far_enough(point, filtered_point, min_distance) for filtered_point in filtered_match_list):
            filtered_match_list.append(point)

    return filtered_match_list

def get_child_windows(parent):
    if not parent:
        return
    hwndChildList = []
    win32gui.EnumChildWindows(parent, lambda hwnd, param: param.append([hwnd,win32gui.GetWindowText(hwnd),win32gui.GetClassName(hwnd)]), hwndChildList)

    return hwndChildList




def mouse_click(handle, x, y, movex=None, movey=None):
    hwnd   = win32gui.FindWindowEx(handle, None, None, None)
    # win32gui.SetForegroundWindow(handle)
    param   = win32api.MAKELONG(x,y)

    if movex is None or movey is None:
        # pyautogui.click(x,y)
        win32gui.PostMessage(hwnd, win32con.WM_LBUTTONDOWN, win32con.MK_LBUTTON, param)
        time.sleep(0.1)
        win32gui.PostMessage(hwnd, win32con.WM_LBUTTONUP, None, param)
    else:
        move_param  = win32api.MAKELONG(movex, movey)

        win32gui.SendMessage(hwnd, win32con.WM_LBUTTONDOWN, win32con.MK_LBUTTON, param)
        time.sleep(2)
        win32gui.SendMessage(hwnd, win32con.WM_MOUSEMOVE, win32con.MK_LBUTTON, move_param)
        time.sleep(2)
        win32gui.SendMessage(hwnd, win32con.WM_LBUTTONUP, None, move_param)

def mouse_click_fast(handle, x, y, movex=None, movey=None):
    hwnd   = win32gui.FindWindowEx(handle, None, None, None)
    # win32gui.SetForegroundWindow(handle)
    param   = win32api.MAKELONG(x,y)

    if movex is None or movey is None:
        # pyautogui.click(x,y)
        win32gui.PostMessage(hwnd, win32con.WM_LBUTTONDOWN, win32con.MK_LBUTTON, param)
        time.sleep(0.02)
        win32gui.PostMessage(hwnd, win32con.WM_LBUTTONUP, None, param)
    else:
        move_param  = win32api.MAKELONG(movex, movey)

        win32gui.SendMessage(hwnd, win32con.WM_LBUTTONDOWN, win32con.MK_LBUTTON, param)
        time.sleep(2)
        win32gui.SendMessage(hwnd, win32con.WM_MOUSEMOVE, win32con.MK_LBUTTON, move_param)
        time.sleep(2)
        win32gui.SendMessage(hwnd, win32con.WM_LBUTTONUP, None, move_param)





def coord_click(handle, x, y):
    coord = match_coord(handle, x, y)
    # print("클릭 좌표 : %s, %s " % coord)
    if coord:
        mouse_click(handle, coord[0], coord[1])




def capture_click(handle, image, per=0):

    image_coord = match_img(handle, image, per)
    if image_coord:
        # print("클릭 좌표 : %s, %s " % image_coord)
        mouse_click(handle, image_coord[0], image_coord[1])
        return True
    else:
        return False

def capture_click_m(handle, image, per=0):

    image_coord = match_img(handle, image, per)
    if image_coord:
        # print("클릭 좌표 : %s, %s " % image_coord)
        mouse_click(handle, image_coord[0], image_coord[1]-20)
        return True
    else:
        return False


def capture_click_list(handle, image):
    image_coord_list = match_img_list(handle, image)
    for image_coord in image_coord_list:
        if image_coord:
            # print("클릭 좌표 : %s, %s " % image_coord)
            pyautogui.click(image_coord[0],image_coord[1])
            # mouse_click(handle, image_coord[0], image_coord[1])


def click(x,y):
    pyautogui.click(x,y)


def send_esc_key(hwnd):
    win32api.keybd_event(win32con.VK_ESCAPE, 0, 0, 0)
    time.sleep(0.1)  # 필요에 따라 대기 시간 조절
    win32api.keybd_event(win32con.VK_ESCAPE, 0, win32con.KEYEVENTF_KEYUP, 0)
