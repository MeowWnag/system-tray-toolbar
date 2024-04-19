import pystray
from pystray import MenuItem as item
from PIL import Image
import webbrowser  # 匯入 webbrowser 模組
import subprocess  # 匯入 subprocess 模組

# 定義開啟網站的函數
def open_website(icon):
    webbrowser.open('https://youtu.be/dQw4w9WgXcQ?si=DyW9I3U5ojTOsDuh')

# 定義開啟應用程式的函數
def open_application(icon):
    # 示範開啟記事本應用程式
    subprocess.Popen(["notepad.exe"])

# 建立選單項目
menu = (item('開啟網站', open_website),
        item('開啟應用程式', open_application),
        item('離開', lambda icon, item: icon.stop()))

# 載入圖示
image = Image.open("在這裡放置圖片的路徑")

# 建立系統列圖示
icon = pystray.Icon("name", image, "title", menu)

# 啟動系統列圖示
icon.run()
