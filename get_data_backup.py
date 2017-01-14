import time
from Launch.GetDriver import GetDriver

driver = GetDriver().get_driver()   # 注意类实例化要加括号（）
# driver.get('http://neihanshequ.com')

time.sleep(2)
first_window = driver.current_window_handle
print(first_window)

for hit in range(1, 2):
    loadMore = driver.find_element_by_id('loadMore').click()
    time.sleep(2)

# li_num = 21
# if li_num <= 20:
#     li = driver.find_elements_by_tag_name('h1')
# else:
li = driver.find_elements_by_xpath(".//*[@id='detail-list']/li[*]/div/div[2]/a/div")

for l in li:
    print(len(li))
    print(l.text)
    l.click()
    time.sleep(2)

    all_windows = driver.window_handles
    print(all_windows)
    try:
        for handle in all_windows:
            if handle != first_window:
                print(handle)
                driver.switch_to_window(handle)
                time.sleep(2)
                answer_one = driver.find_elements_by_xpath(".//p[@class='indent']")
                for num in answer_one[0:2]:
                    print(len(answer_one))
                    print(num.text)

                time.sleep(3)
                driver.close()

        # 切换回第一个窗口
        for handle in all_windows:
            if handle == first_window:
                driver.switch_to_window(handle)

    except Exception as e:
        print(e)
        # 切换回第一个窗口
        for handle in all_windows:
            if handle == first_window:
                driver.switch_to_window(handle)
