import requests
import re

# function to get the scroll text from the Eldorian library API
def get_scrollfromeldorianlibrary():
    response = requests.get("https://raw.githubusercontent.com/microsoft/CopilotAdventures/main/Data/scrolls.txt")
    if response.status_code == 200:
        return response.text
    else:
        return None

# now get the scroll text from the Eldorian library and extract the scroll text using regular expression to filter text surrounded by the symbols {* and *}
# output the extract text in formatted form
def extract_scrolltext():
    scrolltext = get_scrollfromeldorianlibrary()
    if scrolltext is None:
        print("Unable to get scroll from Eldorian library")
    else:
     
        print(f"Original Scroll text: {scrolltext}")
   
        # use regular expression to extract text surrounded by {* and *}
        matches = re.findall(r'\{\*(.*?)\*\}', scrolltext, re.DOTALL)
        for match in matches:
            print(match)
         
        print("Number of extracted secrets found: " + str(len(matches)))
        
       

extract_scrolltext()