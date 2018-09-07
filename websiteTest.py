from selenium import webdriver

browser = webdriver.Chrome()
browser.get('http://10.163.18.33/itm/bbtest-gehaltszuschlag.html')

salaryInput = browser.find_element_by_id('gehalt')
ageInput = browser.find_element_by_id('alter')
resultParagraph = browser.find_element_by_id('ergebnis')
calculateButton = browser.find_element_by_tag_name('button')

noMoneyResult = 'Ergebnis: Zuschlag 0 €'
muchMoneyResult = 'Ergebnis: Zuschlag 100 €'
missingEntryResult = 'Ergebnis: MISSING_ENTRY'


def testSite(alter, gehalt, result):
    salaryInput.clear()
    ageInput.clear()
    salaryInput.send_keys(gehalt)
    ageInput.send_keys(alter)
    calculateButton.click()
    if resultParagraph.text == result:
        return True
    else:
        return False



def testMuchMoney(): 
    res = True
    res = res and testSite(30,0,muchMoneyResult)
    res = res and testSite(30,2499,muchMoneyResult)
    res = res and testSite(50,0,muchMoneyResult)
    res = res and testSite(50,2499,muchMoneyResult)
    if res:
        print(muchMoneyResult + ' bestanden!')
    else:
        print(muchMoneyResult + ' nicht bestanden!')

def testNoMoney(): 
    res = True
    res = res and testSite(29,1500,noMoneyResult)
    res = res and testSite(30,2501,noMoneyResult)
    res = res and testSite(50,2501,noMoneyResult)
    if res:
        print(noMoneyResult + ' bestanden!')
    else:
        print(noMoneyResult + ' nicht bestanden!')

def testMissingEntry(): 
    res = True
    res = res and testSite('','', missingEntryResult)
    res = res and testSite(30,'', missingEntryResult)
    res = res and testSite('',2400, missingEntryResult)

    if res:
        print(missingEntryResult + ' bestanden!')
    else:
        print(missingEntryResult + ' nicht bestanden!')


testMuchMoney()
testNoMoney()
testMissingEntry()

