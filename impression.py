detail = driver.find_element_by_tag_name('body')
impression = detail.find_element_by_class_name('ep-MetricTopContainer')
print(impression.text)
