from selenium.webdriver import Firefox
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
import time

new_num = input("Please enter new number for caller ID ");

driver = Firefox()
driver.get("https://voip.ms/login")
email = driver.find_elements_by_xpath('//input[@id="username"]')[1]
email.send_keys('pcs-wireless@hotmail.com')
password = driver.find_elements_by_xpath('//input[@id="password"]')[1]
password.send_keys('Developer44$')

login_btn = driver.find_elements_by_xpath('//input[@class="btn btn-ghost btn-big"]')[1]
login_btn.click()


time.sleep(10);

#wait = WebDriverWait(driver, 10);
#wait.until(EC.visbtibility_of_element_located((By.XPATH, '//a[contains(@href,"/m/managesubaccount.php")]'))).click()
btn = driver.find_element_by_link_text("Sub Accounts")
hover = ActionChains(driver).move_to_element(btn)
hover.perform()

subbtn = driver.find_element_by_link_text("Manage Sub Accounts")
subbtn.click();
time.sleep(10)
#element = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, '//a[contains(@href,"editsub.php?action=edit&id=266419")')))
#element.click()
el = driver.find_elements_by_class_name("edit-icon")[1];
el.click();
time.sleep(5)
el1 = driver.find_element_by_name("callerid");
el1.clear()
el1.send_keys(new_num);

update = driver.find_element_by_id("button");
driver.execute_script("arguments[0].click();", update)
time.sleep(5);
driver.close();
