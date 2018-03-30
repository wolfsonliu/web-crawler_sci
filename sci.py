import os
import time
import random
from selenium import webdriver


profile = webdriver.FirefoxProfile()

profile.set_preference('browser.download.folderList', 2)
profile.set_preference('browser.download.dir', os.getcwd())
profile.set_preference('browser.download.manager.showWhenStarting', False)
profile.set_preference('browser.helperApps.neverAsk.saveToDisk', 'text/txt')
ff = webdriver.Firefox(firefox_profile=profile, executable_path=r'./geckodriver.exe')


webpage = dict()
webpage['北京大学'] = 'https://apps.webofknowledge.com/Search.do?product=WOS&SID=5Cdom3WBCS7G41fHvX1&search_mode=GeneralSearch&prID=4b0fcdd9-6b27-4142-b544-67264e1d8944'
webpage['清华大学'] = 'https://apps.webofknowledge.com/Search.do?product=WOS&SID=5BsFncBaEMbEhhl7cYk&search_mode=GeneralSearch&prID=11a1efee-cdf1-43b3-9679-5ae0596d2b03'
webpage['中国人民大学'] = 'https://apps.webofknowledge.com/Search.do?product=WOS&SID=8A3QDqb3Qf1ufgXIwn8&search_mode=GeneralSearch&prID=b043d613-c44a-4a5c-90a9-78ab3e0401f1'
webpage['北京理工大学'] = 'https://apps.webofknowledge.com/Search.do?product=WOS&SID=8A3QDqb3Qf1ufgXIwn8&search_mode=GeneralSearch&prID=d07c3abf-50cc-44ec-b159-d557a9bb25c4'
webpage['北京航天航空大学'] = 'https://apps.webofknowledge.com/Search.do?product=WOS&SID=8A3QDqb3Qf1ufgXIwn8&search_mode=GeneralSearch&prID=a9768b71-3178-4205-a7b4-6db2898f31ac'

ff.get(webpage['清华大学'])
download_arrow = ff.find_element_by_class_name('saveToButton').find_element_by_class_name('select2-selection__arrow')
download_arrow.click()
download_select = ff.find_element_by_class_name(
    'select2-results'
).find_element_by_xpath('//ul[@id="select2-saveToMenu-results"]/li[text()="Save to Other File Formats"]')

total_num = 91319

for x in range(total_num // 500 + 1):
    if x < 66:
        continue
    elif x == total_num // 500:
        start = x * 500 + 1
        end = total_num
    else:
        start = x * 500 + 1
        end = start + 500 - 1
    print(x)
    select = ff.find_element_by_id('select2-saveToMenu-container')
    select.click()

    check_radio = ff.find_element_by_id('records-range-radio-button').find_element_by_id('numberOfRecordsRange')
    check_radio.click()
    check_record = ff.find_element_by_id('records-range-inputs')
    check_from = check_record.find_element_by_id('markFrom')
    ff.execute_script('arguments[0].value = arguments[1]', check_from, start)
    check_to = check_record.find_element_by_id('markTo')
    ff.execute_script('arguments[0].value = arguments[1]', check_to, end)

    # 选择输出内容
    record_content = ff.find_element_by_class_name(
        'quickoutput-content'
    )
    record_content_span = record_content.find_element_by_class_name('selection').find_element_by_class_name('select2-selection')
    record_content_span.click()
    record_content_select = ff.find_element_by_class_name(
        'select2-results'
    ).find_element_by_xpath('//ul[@id="select2-bib_fields-results"]/li[text()="Full Record and Cited References"]')
    record_content_select.click()

    # 选择输出文件
    file_format = ff.find_element_by_class_name(
        'quick-output-detail'
    )
    file_format_span = file_format.find_element_by_class_name('selection').find_element_by_class_name('select2-selection')
    file_format_span.click()
    file_format_select = ff.find_element_by_class_name(
        'select2-results'
    ).find_element_by_xpath('//ul[@id="select2-saveOptions-results"]/li[text()="Tab-delimited (Win, UTF-8)"]')
    file_format_select.click()

    submit = ff.find_element_by_class_name('quickoutput-action').find_element_by_class_name('standard-button')
    submit.click()
    time.sleep(17)
    close = ff.find_element_by_class_name('quickoutput-cancel-action')
    close.click()
    time.sleep(random.uniform(0, 2))