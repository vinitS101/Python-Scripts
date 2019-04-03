# Small script to automate google searches
import webbrowser, sys

sys.argv

#check for command line arguments

if len(sys.argv) > 1:
    address = '+'.join(sys.argv[1:])

#open browser at google search
webbrowser.open('https://www.google.co.in/search?q=' + address)


