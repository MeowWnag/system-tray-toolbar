# 系統列圖示應用程式

這個Python程式是一個系統列圖示應用程式，它可以開啟網站和應用程式，並且有離開的選項。

## 程式碼解釋

首先，我們匯入需要的模組：

```python
import pystray
from pystray import MenuItem as item
from PIL import Image
import webbrowser
import subprocess
```

然後，我們定義兩個函數，一個是用來開啟網站的，另一個是用來開啟應用程式的：

```python
def open_website(icon):
    webbrowser.open('https://youtu.be/dQw4w9WgXcQ?si=DyW9I3U5ojTOsDuh')

def open_application(icon):
    subprocess.Popen(["notepad.exe"])
```

接著，我們建立一個選單，選單中有三個選項：開啟網站、開啟應用程式和離開：

```python
menu = (item('開啟網站', open_website),
        item('開啟應用程式', open_application),
        item('離開', lambda icon, item: icon.stop()))
```

然後，我們載入一個圖示，並建立一個系統列圖示：

```python
image = Image.open("D:\\Users\\charles\\下載\\高師.png")
icon = pystray.Icon("name", image, "title", menu)
```

最後，我們啟動系統列圖示：

```python
icon.run()
```

## 如何使用

1. 確保你的電腦已經安裝了Python和相關的模組（pystray、PIL、webbrowser和subprocess）。
2. 下載並執行這個程式。
3. 在系統列中，你會看到一個新的圖示。
4. 點擊這個圖示，會出現一個選單，你可以選擇開啟網站、開啟應用程式或者離開。

## 注意事項

- 這個程式是在Windows系統中開發的，如果你在其他系統中使用，可能需要做一些調整。
- 開啟應用程式的函數中，我們示範的是開啟記事本，你可以根據需要修改這個函數。
- 載入圖示的路徑需要根據你的圖示的實際路徑來修改。如果找不到圖示，程式將無法運行。
