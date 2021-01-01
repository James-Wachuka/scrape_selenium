waiting_func('tag name', 'iframe')
iframe = driver.find_element_by_tag_name('iframe')
driver.switch_to.frame(iframe)
