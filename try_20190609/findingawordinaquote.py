import re

def Main ():
    line="This is about regular expressions"

    matchResult = re.match('is', line, re.M|re.I)
    print(matchResult)
    if matchResult:
        print("Match Found: "+matchResult.group())
    else:
        print("No Match was Found.")

    searchResult = re.search("is", line, re.M|re.I)
    if searchResult:
        print("Search Found: "+searchResult.group())
    else:
        print("Nothing found in search")

if __name__ == "__main__":
    Main()
