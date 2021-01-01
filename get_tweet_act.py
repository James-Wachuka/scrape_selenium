path = []
while True:
    scrape.waiting_func('css selector', "a[aria-label='View Tweet activity']")
    last_height = driver.execute_script("return document.body.scrollHeight")
    traffic_path = driver.find_elements_by_css_selector("a[aria-label='View Tweet activity']")
    path.extend([traffic.get_attribute('href') for traffic in traffic_path])
    driver.execute_script("window.scrollTo(0, {})".format(last_height+500))
    time.sleep(3)
    new_height = driver.execute_script("return document.body.scrollHeight")
    if last_height == new_height:
        break
