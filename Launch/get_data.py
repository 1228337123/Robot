import time
from selenium import webdriver
from Launch.GetDriver import GetDriver
import pymongo
conn = pymongo.MongoClient("localhost", 27017)
db = conn.get_database('Sina').get_collection('spiderdata')

driver = webdriver.PhantomJS("I:/phantomjs/bin/phantomjs.exe")
# driver = GetDriver().get_driver()   # 注意类实例化要加括号（）
driver.get('http://neihanshequ.com')
time.sleep(2)
first_window = driver.current_window_handle

# index = 0
try:
    for hit in range(1, 30000):
        time.sleep(1)
        driver.implicitly_wait(5)
        if driver.find_element_by_id('loadMore'):
            driver.find_element_by_id('loadMore').click()

    li = driver.find_elements_by_xpath(".//*[@id='detail-list']/li[*]/div/div[2]/a/div")
    i = 0
    for l in li:  # [index+1:index+20]:
        i += 1
        print(i, len(li))
        question = l.text  # u"还有耳朵……"
        find = db.find_one({"question": question})
        # print(find)

        if find is None:
            print("question:", l.text)

            l.click()
            time.sleep(3)

            all_windows = driver.window_handles
            try:
                for handle in all_windows:
                    if handle != first_window:
                        driver.switch_to.window(handle)
                        # time.sleep(2)
                        answers = driver.find_elements_by_xpath(".//p[@class='indent']")
                        # for num in answers[0]:
                        if len(answers) > 2:
                            answer_one = answers[0].text
                            answer_two = answers[1].text
                            db.insert({"question": question, "answer_one": answer_one, "answer_two": answer_two})
                            print("answer_one:", answer_one)
                            print("answer_two:", answer_two)
                        # time.sleep(3)
                        driver.close()

                # 切换回第一个窗口
                for handle in all_windows:
                    if handle == first_window:
                        driver.switch_to.window(handle)

            except Exception as e:
                print(e)
                driver.save_screenshot('screen.png')
                # 切换回第一个窗口
                for handle in all_windows:
                    if handle == first_window:
                        driver.switch_to.window(handle)

except Exception as e:

    li = driver.find_elements_by_xpath(".//*[@id='detail-list']/li[*]/div/div[2]/a/div")
    i = 0
    for l in li:   # [index+1:index+20]:
        i += 1
        print(i, len(li))
        question = l.text   # u"还有耳朵……"
        find = db.find_one({"question": question})
        # print(find)

        if find is None:
            print("question:", l.text)

            l.click()
            time.sleep(3)

            all_windows = driver.window_handles
            try:
                for handle in all_windows:
                    if handle != first_window:
                        driver.switch_to.window(handle)
                        # time.sleep(2)
                        answers = driver.find_elements_by_xpath(".//p[@class='indent']")
                        # for num in answers[0]:
                        if len(answers) > 2:
                            answer_one = answers[0].text
                            answer_two = answers[1].text
                            db.insert({"question": question, "answer_one": answer_one, "answer_two": answer_two})
                            print("answer_one:", answer_one)
                            print("answer_two:", answer_two)
                        # time.sleep(3)
                        driver.close()

                # 切换回第一个窗口
                for handle in all_windows:
                    if handle == first_window:
                        driver.switch_to.window(handle)

            except Exception as e:
                print(e)
                driver.save_screenshot('screen.png')
                # 切换回第一个窗口
                for handle in all_windows:
                    if handle == first_window:
                        driver.switch_to.window(handle)
        # time.sleep(2)
        # driver.implicitly_wait(5)
        # if driver.find_element_by_id('loadMore'):
        # if driver.find_element_by_id('loadMore').click():
        #     index += 20