#! python3
# lucky.py - Opens several Google search results.

import requests, sys, webbrowser, bs4, pyperclip
try:
    print('Googling...')    # display text while downloading the Google page

    # Either the search arguments where given to the program as parameters
    # or it googles for the text in your clipboard
    if len(sys.argv) > 1:
        res = requests.get('http://google.com/search?q=' + ' '.join(sys.argv[1:]))
        res.raise_for_status()
    else:
        res = requests.get('http://google.com/search?q=' + pyperclip.paste())
        res.raise_for_status()    
    
    # Retrieve top search result links.
    soup = bs4.BeautifulSoup(res.text, 'html.parser')
    linksWithoutSubLinks = []
    for linkElems in soup.select('.r a'):
        if 'class' in linkElems.attrs:
            if 'sla' not in linkElems.attrs['class']:
                # In some cases the first few google results can have sublinks
                # I want to exlude them from my search results
                linksWithoutSubLinks.append(linkElems)
        else:
            linksWithoutSubLinks.append(linkElems)
    
    # I want a maxiumum of 10 Tabs open but a minimum of the found links
    numOpen = min(10, len(linksWithoutSubLinks))
    print('Opening Tabs...')
    for i in (range(numOpen)):
        webbrowser.open('http://google.com' + linksWithoutSubLinks[i].get('href'))

except KeyboardInterrupt:
    sys.exit()