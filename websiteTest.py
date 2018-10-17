from selenium import webdriver

#Webbrowser startet und Website aufrufen.
browser = webdriver.Chrome()
browser.get('http://10.163.18.33/itm/bbtest-gehaltszuschlag.html')

#HTML nach IDs suchen und in eine Variable packen
salaryInput = browser.find_element_by_id('gehalt')
ageInput = browser.find_element_by_id('alter')
resultParagraph = browser.find_element_by_id('ergebnis')
calculateButton = browser.find_element_by_tag_name('button')

#mögliche Ergebnis Ausgaben zum Vergleichen deklarieren und initialiseren
noMoneyResult = 'Ergebnis: Zuschlag 0 €'
muchMoneyResult = 'Ergebnis: Zuschlag 100 €'
missingEntryResult = 'Ergebnis: MISSING_ENTRY'


#Allgemeine Methode zum Testen der Seite
def testSite(age, salary, result):
    salaryInput.clear()
    ageInput.clear()
    salaryInput.send_keys(salary)
    ageInput.send_keys(age)
    calculateButton.click()
    if resultParagraph.text == result:
        return True
    else:
        return False

# Testet die Grenzwerte für den Fall, dass es einen Zuschlag geben soll.
def testMuchMoney(): 
    res = testSite(30,0,muchMoneyResult)\
    and testSite(30,2499,muchMoneyResult) \
    and testSite(50,0,muchMoneyResult)\
    and testSite(50,2499,muchMoneyResult)
    
    if res:
        print('Test '+ muchMoneyResult + ' bestanden!')
    else:
        print('Test '+ muchMoneyResult + ' nicht bestanden!')

# Testet die Grenzwerte für den Fall, dass es keinen Zuschlag geben soll.
def testNoMoney(): 
    res = testSite(29,1500,noMoneyResult)\
    and testSite(30,2501,noMoneyResult)\
    and testSite(50,2501,noMoneyResult)
    
    if res:
        print('Test '+ noMoneyResult + ' bestanden!')
    else:
        print('Test '+ noMoneyResult + ' nicht bestanden!')

# Testet die Fälle in denen ein Eintrag fehlt.
def testMissingEntry(): 
    res = testSite('','', missingEntryResult)\
    and testSite(30,'', missingEntryResult)\
    and testSite('',2400, missingEntryResult)

    if res:
        print('Test '+ missingEntryResult + ' bestanden!')
    else:
        print('Test '+ missingEntryResult + ' nicht bestanden!')

#
testMuchMoney()
testNoMoney()
testMissingEntry()