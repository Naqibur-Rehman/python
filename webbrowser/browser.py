import webbrowser
#
# webbrowser.open("www.google.com")
#
# help(webbrowser)

chrome = webbrowser.get('google-chrome %s')
chrome.open_new_tab("www.google.com")
