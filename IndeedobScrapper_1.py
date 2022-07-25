import requests
from bs4 import BeautifulSoup

try:

    url = "https://au.indeed.com/data-analyst-jobs-in-Australia"

    page = requests.get(url)
    print(page)
    # with open ("index.html" , "w") as f:
    #     f.write(page)
    
    # with open ("index.html" , "r") as f:
    #     data = f.read(page)

    soup  = BeautifulSoup(page.content , "html.parser")
    # print(soup)


    jobSearchResults = soup.find( "ul" , class_="jobsearch-ResultsList css-0")
    # print(jobSearchResults.prettify())

    for jobSearchResult in jobSearchResults:
        title = jobSearchResult.find("h2" , class_="jobTitle")
        # print( " Title Type : ",type(title))
        # print(title)
        if title == None:
            continue
        for item in title:
            job_title = item.find("span")
            if job_title == None:
                continue
            print(job_title.text)


except Exception as e:
    print("*****************Exception Start*********************")
    print(e)
    print("*****************Exception End***********************")



# jobTitle-d0a667165ee3fe93
# jobTitle-3de097e1a6a0a233

# jobTitle jobTitle-newJob css-bdjp2m eu4oa1w0
# jobTitle css-1h4a4n5 eu4oa1w0

# <span id="jobTitle-451bc6816c540b4d" title="Reporting and Data Analyst">Reporting and Data Analyst</span>