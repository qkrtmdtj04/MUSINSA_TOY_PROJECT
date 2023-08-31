from selenium import webdriver
from selenium.webdriver.common.by import By

import time



def musinsa(data,rank): # 1순위 2순위 3순위
    driver = webdriver.Chrome() # 크롬킴
    driver.get("https://www.musinsa.com/app/") # url 주소로 불러온다

    inputbox = driver.find_element(By.XPATH, '//*[@id="commonLayoutSearchForm"]')
    inputbox.click()
    inputbox.send_keys(data)



    time.sleep(5)
    inputbox = driver.find_element(By.XPATH,f'//*[@id="topCommonPc"]/header/div[2]/div/div[3]/section/ul/li[{rank}]/a') 
    inputbox.click()
    variable = driver.current_url
    
    title_xpath = driver.find_element(By.XPATH,f'//*[@id="page_product_detail"]/div[2]/div[3]/span') 
    title = title_xpath.text
    
    price_xpath = driver.find_element(By.XPATH,f'//*[@id="list_price"]') #//*[@id="list_price"]
    price = price_xpath.text
    
    star_xpath = driver.find_element(By.XPATH,f'//*[@id="product_order_info"]/div[1]/ul/li[6]/p[2]/a/span[2]')  
    star = star_xpath.text

    selling_xpath = driver.find_element(By.XPATH,f'//*[@id="sales_1y_qty"]')  
    selling = selling_xpath.text

    image_xpath = driver.find_element(By.CSS_SELECTOR,'#bigimg') #//*[@id="bigimg"]
    image = image_xpath.get_attribute('src')

    print(title)
    print(variable)
    print(price)
    print(image)
    print(selling)
    return title,variable,price,selling,image,star

#url 주소 
# 현석이랑 민준이가 둘이 크롤링 => 타이틀, 웹주소
# 디코봇
# 첫 -> 
# 힘들거같더라고요
# 그게 오늘 할일

