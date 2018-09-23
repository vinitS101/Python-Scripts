import webbrowser, sys

sys.argv

#check for command line arguments

if len(sys.argv) > 1:
    address = '+'.join(sys.argv[1:])

#open browser at yt
webbrowser.open('https://www.youtube.com/results?search_query=' + address)


