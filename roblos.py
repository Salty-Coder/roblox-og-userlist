import time
from colorama import init, Fore, Back, Style
init(convert=True)
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.common.exceptions import NoSuchElementException   


options = Options()
options.add_argument('--headless')
options.add_argument('--disable-gpu')  # Last I checked this was necessary.
options.add_argument("--log-level=3") # Fatal



try:
    f = open('chromedriver.exe')
    f.close()
except FileNotFoundError:
    print('Chromedriver not found...')
    time.sleep(5)
    exit()




clear = str(input("Clear User List (Y/N)?: "))
startnum = int(input("Start ID: "))
maxnum = int(input("Max ID: "))
delay = float(input("Delay: "))

num = startnum or 1

if clear == "Y":
    open("Users.txt", "w").close()
  


driver = webdriver.Chrome("chromedriver.exe", options=options)

f = open('Users.txt', 'a+')  


valid = 0
deleted = 0
failed = 0

while num <= maxnum:
    time.sleep(delay)
    driver.get("https://www.roblox.com/users/" + str(num) + "/profile")

    try:
        name = driver.find_element_by_xpath('//*[@id="container-main"]/div[2]/div[2]/div/div[1]/div/div[2]/div[2]/div[1]/div[1]/h2').text
        named = True
        valid = valid + 1
        print("[" + Fore.YELLOW + "#" + Fore.RESET + "] " + Fore.GREEN + str(num) + " = Success!" + Fore.RESET)
    except NoSuchElementException:
        try:
            driver.find_element_by_xpath('//*[@id="container-main"]/div[2]/div/div/div[1]/h4')
            named = False
            deleted = deleted + 1
            print("[" + Fore.YELLOW + "#" + Fore.RESET + "] " + Fore.YELLOW + str(num) + " = Deleted." + Fore.RESET)
        except NoSuchElementException:
            named = False
            failed = failed + 1
            print("[" + Fore.YELLOW + "#" + Fore.RESET + "] " + Fore.RED + str(num) + " = Failed." + Fore.RESET)

    num = num + 1
    if name and named == True: f.write(name + "\n")
    f.flush()

print("[" + Fore.BLUE + "#" + Fore.RESET + "] " + Fore.CYAN + "Valid - " + str(valid) + Fore.RESET)
print("[" + Fore.BLUE + "#" + Fore.RESET + "] " + Fore.CYAN + "Deleted - " + str(deleted) + Fore.RESET)
print("[" + Fore.BLUE + "#" + Fore.RESET + "] " + Fore.CYAN + "Failed - " + str(failed) + Fore.RESET)
print("[" + Fore.BLUE + "#" + Fore.RESET + "] " + Fore.CYAN + "Total - " + str(valid + deleted + failed) + Fore.RESET)


driver.quit()
f.close()