import pytesseract
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
from PIL import Image

'''
基本设置
'''
driver = webdriver.Edge(r'C:\Users\PC\ppp\Scripts\msedgedriver.exe')
cookies = {
    'BIDUPSID': '0149403893FB17D9868DDC00E811FCE7',
    'PSTM': '1615095665',
    'BAIDUID': '0149403893FB17D9C00F7D3EFEEAD014:FG=1',
    'delPer': '0',
    'PSINO': '2',
    'H_PS_PSSID': '33257_33273_31660_33594_33570_33591_26350_33265',
    'BA_HECTOR': '040g2l8k2g0l218k311g48prj0r',
    'BDORZ': 'B490B5EBF6F3CD402E515D22BCDA1598',
    'BAIDUID_BFESS': '0149403893FB17D9C00F7D3EFEEAD014:FG=1',
    'HOSUPPORT': '1',
    'HOSUPPORT_BFESS': '1',
    'pplogid': '6942ne4CqAM25cfC4EssHF4KPYKQwU5eZfkq2hxkeydl8lc3jlmZya3gKkwSeRGtnrmryRCGksGhdH6vvVel%2FMHsiFWkNBqc0k%2B5oLijPesWvVA%3D',
    'pplogid_BFESS': '6942ne4CqAM25cfC4EssHF4KPYKQwU5eZfkq2hxkeydl8lc3jlmZya3gKkwSeRGtnrmryRCGksGhdH6vvVel%2FMHsiFWkNBqc0k%2B5oLijPesWvVA%3D',
    'UBI': 'fi_PncwhpxZ%7ETaJcwoQzv%7Etk1GbYFHnDEF1qmAF2zK6dHasFcbPclSCm%7En-w%7ENK7VbkDIllyhZUKHBMdm5g',
    'UBI_BFESS': 'fi_PncwhpxZ%7ETaJcwoQzv%7Etk1GbYFHnDEF1qmAF2zK6dHasFcbPclSCm%7En-w%7ENK7VbkDIllyhZUKHBMdm5g',
    'logTraceID': 'dc5efb79487f49534f9e47dfe497392b33c9992e86bd78d6f0',
}
headers = {
    'Connection': 'keep-alive',
    'Pragma': 'no-cache',
    'Cache-Control': 'no-cache',
    'sec-ch-ua': '"Chromium";v="88", "Google Chrome";v="88", ";Not A Brand";v="99"',
    'DNT': '1',
    'sec-ch-ua-mobile': '?0',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.190 Safari/537.36',
    'Accept': '*/*',
    'Sec-Fetch-Site': 'same-site',
    'Sec-Fetch-Mode': 'no-cors',
    'Sec-Fetch-Dest': 'script',
    #'Referer': 'https://www.baidu.com/s?rsv_idx=1&wd=31%E7%9C%81%E6%96%B0%E5%A2%9E%E7%A1%AE%E8%AF%8A13%E4%BE%8B+%E5%9D%87%E4%B8%BA%E5%A2%83%E5%A4%96%E8%BE%93%E5%85%A5&fenlei=256&ie=utf-8&rsv_cq=np.random.choice+%E4%B8%8D%E9%87%8D%E5%A4%8D&rsv_dl=0_right_fyb_pchot_20811_01&rsv_pq=c0b53cdc0005af92&oq=np.random.choice+%E4%B8%8D%E9%87%8D%E5%A4%8D&rsv_t=2452p17G6e88Hpj%2FkNppuwT%2FFjr8KeLJKT4KqqeSLqr7MhD7HbIYjtM9KVc&rsf=84b938b812815a59afcce7cc4e641b1d_1_15_8&rqid=c0b53cdc0005af92',
    'Accept-Language': 'zh-CN,zh;q=0.9',
}
url=r'https://www.beian.gov.cn/portal/registerSystemInfo'
screenshot_loc=r"D:\lqbz\Code\Screenshot.png"
'''
函数
'''
# 读取写在WEB.txt的待查验网站
def ReadTxt(txt):
    f=open(txt)
    return f.readlines()
# 验证码识别
def VerifyCode(pic):
    location = pic.location
    size = pic.size

    rangle = (1.5 * int(location['x']), 1.5 * int(location['y']), 1.5 * int(location['x'] + size['width']),
              1.5 * int(location['y'] + size['height']))         # 1.5为显示比例

    CodePng = Image.open(screenshot_loc)
    image = CodePng.crop(rangle)
    # image = demo(image).test()
    code = pytesseract.image_to_string(image, config='--psm 7')  # 识别率比较低
    return(code)
#爬取查找网站的基本情况和所有者基本情况
def infos():
    driver.switch_to.window(driver.window_handles[-1])
    driver.current_window_handle
    table1=driver.find_element_by_xpath('/html/body/div[1]/div[3]/div[3]/div[1]/table')
    table2=driver.find_element_by_xpath('/html/body/div[1]/div[3]/div[3]/div[2]/table')
    rows1=table1.find_elements_by_tag_name('tr')
    rows2 = table2.find_elements_by_tag_name('tr')
    dic1={}
    dic2={}
    for row in rows1:
        dic1[row.find_element_by_xpath('td[1]').text]=row.find_element_by_xpath('td[2]').text
    for row in rows2:
        dic2[row.find_element_by_xpath('td[1]').text] = row.find_element_by_xpath('td[2]').text
    with open('infos.txt','a+') as f:
        f.write('\n')
        f.write(website)
        f.write("网站基本情况:\n")
        f.write(str(dic1.items())+'\n')
        f.write("网站所有者基本情况:\n")
        f.write(str(dic2.items())+'\n')
        f.flush()


    driver.back()

'''
selenium
验证码进行粗糙的识别，仍需要人工进行二次识别
'''
driver.get(url)                                                                       # 启动selenium
driver.maximize_window()
i = 0
for website in ReadTxt(r'WEB.txt'):                                                   # 对txt文档中所有website遍历
    website = website.split('//')[1]
    driver.current_window_handle

    driver.find_element_by_xpath(r'//*[@id="myTab"]/li[2]').click()                   # 按照网站域名查找
    time.sleep(1)
    driver.find_element_by_xpath(r"//*[@id='domainform']/div/div[2]/div/img").click() # 刷新验证码
    driver.find_element_by_xpath(r'//*[@id="domain"]').clear()
    driver.find_element_by_xpath(r'//*[@id="domain"]').send_keys(website)             # 输入域名
    time.sleep(1)

    # 验证码识别+输入
    Screenshot = driver.save_screenshot(screenshot_loc)                               # 网页截图
    pic = driver.find_element_by_xpath(r"//*[@id='domainform']/div/div[2]/div/img")   # 在网页上定位验证码
    code=VerifyCode(pic)                                                              # 识别验证码
    driver.find_element_by_xpath(r'//*[@id="ver2"]').clear()
    driver.find_element_by_xpath(r'//*[@id="ver2"]').send_keys(code)                  # 输入验证码
    time.sleep(1)

    # 判断验证码是否识别成功，识别错误手动输入
    # 按照网站上是否判出现“验证码错误”断验证码是否输入正确
    ver = driver.find_element_by_xpath('//*[@id="domainerror"]').get_attribute('style')
    if ver == 'color: red; display: none;':                                                      # 未出现“验证码错误”提示
        print('e')
        driver.find_element_by_xpath('//*[@id="domainform"]/div/div[3]/div/button').click()
    else:                                                                                        # 出现“验证码错误”提示
        WebDriverWait(driver, 10).until(                                                         # 等待人工输入验证码
            EC.invisibility_of_element(driver.find_element_by_xpath("//*[@id='domainerror']")))
        print('f')
        driver.find_element_by_xpath('//*[@id="domainform"]/div/div[3]/div/button').click()
    time.sleep(2)

    # 如果网站显示“没有查到数据”，记录出错网站到Notfound
    try:
        if EC.invisibility_of_element(driver.find_element_by_xpath("//*[@id='a_wzmc']")):
            print(website)
            with open('NotFound', 'a+') as file:
                file.write(website)
            continue
    except Exception as e:
        pass

    # 爬取查找网站的基本情况和所有者基本情况，保存到infos.txt
    infos()

file.close()
driver.close()