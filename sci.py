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
webpage['中山大学'] = 'https://apps.webofknowledge.com/Search.do?product=WOS&SID=6FCnNVBk842X7ddED9p&search_mode=GeneralSearch&prID=3c94ac33-9fd0-4f43-b019-f1ad0436b3d0'

ff.get(webpage['中山大学'])

download_arrow = ff.find_element_by_class_name('saveToButton').find_element_by_class_name('select2-selection__arrow')
download_arrow.click()
download_select = ff.find_element_by_class_name(
    'select2-results'
).find_element_by_xpath('//ul[@id="select2-saveToMenu-results"]/li[text()="Save to Other File Formats"]')

total_num = 54376
skip_page = 99

for x in range(total_num // 500 + 1):
    if x < skip_page:
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