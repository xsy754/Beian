# Beian
**验证码识别只进行了灰化+pytesseract识别，现有降噪方法比较慢**

**基本设置处修改屏幕截图暂时存储位置，屏幕缩放设置，webdriver**

```
driver = webdriver.Edge(r'C:\Users\PC\ppp\Scripts\msedgedriver.exe')
screenshot_loc=r"D:\lqbz\Code\Screenshot.png"
scaling=1.5
```

**提示“没有查到数据”的网址数量较多，在WEB.txt中的测试网站占比大约80%...**

WEB.txt存储了待输入到网站的网址

infos.txt能够查验到信息的网址

NotFound网站提示“没有查到数据”的网址
