import time
from selenium import webdriver
from Launch.GetDriver import GetDriver
from pymongo import MongoClient
conn = MongoClient("localhost", 27017)
db = conn.Sina
# try:
driver = webdriver.PhantomJS("I:/phantomjs/bin/phantomjs.exe")
# driver = GetDriver().get_driver()   # 注意类实例化要加括号（）
driver.get('http://neihanshequ.com')

time.sleep(2)
first_window = driver.current_window_handle

for hit in range(1, 1500):
    loadMore = driver.find_element_by_id('loadMore').click()
    # time.sleep()

li = driver.find_elements_by_xpath(".//*[@id='detail-list']/li[*]/div/div[2]/a/div")

for l in li:
    question = l.text
    print(len(li))
    print(l.text)
    l.click()
    time.sleep(5)

    all_windows = driver.window_handles
    try:
        for handle in all_windows:
            if handle != first_window:
                driver.switch_to_window(handle)
                # time.sleep(2)
                answers = driver.find_elements_by_xpath(".//p[@class='indent']")
                # for num in answers[0]:
                answer_one = answers[0].text
                answer_two = answers[1].text
                db.spiderdata.insert({"question": question, "answer_one": answer_one, "answer_two": answer_two})
                print(answer_one)
                print(answer_two)
                # time.sleep(3)
                driver.close()

        # 切换回第一个窗口
        for handle in all_windows:
            if handle == first_window:
                driver.switch_to_window(handle)

    except Exception as e:
        print(e)
        driver.save_screenshot('screen.png')
        # 切换回第一个窗口
        for handle in all_windows:
            if handle == first_window:
                driver.switch_to_window(handle)

# except Exception as e:
#     print(e)
#     driver.save_screenshot('screen.png')
