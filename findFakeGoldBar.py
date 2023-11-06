from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.alert import Alert


def getResult(driver):
    result = driver.find_element(By.CLASS_NAME, "result").find_element(By.ID, "reset")
    return result.text


def leftBowlInput(box, number, driver):
    left = "left_" + str(box)
    driver.find_element(By.ID, left).send_keys(number)


def rightBowlInput(box, number, driver):
    right = "right_" + str(box)
    driver.find_element(By.ID, right).send_keys(number)


def clickWeigh(driver):
    driver.find_element(By.ID, "weigh").click()
    WebDriverWait(driver, 10).until(lambda wait: getResult(driver) != "?")


def clickReset(driver):
    resetButton = driver.find_elements(By.ID, "reset")
    resetButton[1].click()


def printWeighings(driver):
    infoClass = driver.find_element(By.CLASS_NAME, "game-info")
    weighingsList = infoClass.find_elements(By.TAG_NAME, "li")
    for weighings in weighingsList:
        print(weighings.text)


def clickFakeCoin(number, driver):
    fakeBar = "coin_" + str(number)
    driver.find_element(By.ID, fakeBar).click()
    WebDriverWait(driver, 10).until(EC.alert_is_present())
    alert = Alert(driver)
    assert "Yay! You find it!" in alert.text
    print (alert.text)
    alert.dismiss()

def setUp():
    # Start a Selenium WebDriver instance (you'll need the appropriate WebDriver installed).
    driver = webdriver.Chrome()
    # Navigate to the web page.
    driver.get("http://sdetchallenge.fetch.com/")
    assert "React App" in driver.title
    return driver

def compareWeights(num1, num2, driver):
    leftBowlInput(0, num1, driver)
    rightBowlInput(0, num2, driver)
    clickWeigh(driver)
    return getResult(driver)

def findFakeInGroup(num1, num2, num3, result, driver):
    if result == "=":
        print("Bar #" + str(num3)+ " is fake.")
        clickFakeCoin(num3, driver)
    elif result == "<":
        print("Bar #" + str(num1)+ " is fake.")
        clickFakeCoin(num1, driver)
    else:
        print("Bar #" + str(num2)+ " is fake.")
        clickFakeCoin(num2, driver)

# Navigate to the web page.
def findFakeGoldIndex():
    driver = setUp()
    try:
        for i in range(0, 3):
            leftBowlInput(i, i, driver)
            rightBowlInput(i, i + 3, driver)
        
        clickWeigh(driver)
        result = getResult(driver)
        clickReset(driver)

        if result == "=":  # if [0,1,2] and [3,4,5] are equal, then we know [6,7,8] houses the fake
            result = compareWeights(6, 7, driver)
            findFakeInGroup(6, 7, 8, result, driver)
        
        elif result == ">":  # if [0,1,2] > [3,4,5], then we know [3,4,5] houses the fake
            result = compareWeights(3, 4, driver)
            findFakeInGroup(3, 4, 5, result, driver)
        
        else:  # if [0,1,2] < [3,4,5], then we know [0,1,2] houses the fake
            result = compareWeights(0, 1, driver)
            findFakeInGroup(0, 1, 2, result, driver)

        print("Weighings:")
        printWeighings(driver)

    finally:
        # To close the WebDriver after the test is finished.
        driver.quit()