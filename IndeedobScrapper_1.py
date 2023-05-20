from csv import writer
import csv
from tkinter.messagebox import NO
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
    field_name = ["Job Title" , "Company Name" , "Location"]

    with open("job.csv","w" , newline="")as f:
        csv_writer = csv.writer(f, delimiter=",")
        csv_writer.writerow(field_name)

        for jobSearchResult in jobSearchResults:
            print()
            title = jobSearchResult.find("h2" , class_="jobTitle")
            if title == None:
                continue
            for item in title:
                job_title = item.find("span")
                if job_title == None:
                    pass
                else:
                    print(job_title.text)
            companyName = jobSearchResult.find("a" , class_="companyOverviewLink" )
            if companyName == None:
                pass
            else:
                print(companyName.text)

            companyLocation = jobSearchResult.find("div" , class_="companyLocation")
            if companyLocation == None:
                pass
            else:
                print(companyLocation.text)
            if job_title != None and companyName != None and companyLocation != None:
                csv_writer.writerow([job_title.text , companyName.text , companyLocation.text])
            elif job_title == None:
                csv_writer.writerow([None , companyName.text , companyLocation.text])
            elif companyName == None:
                csv_writer.writerow([job_title.text , None , companyLocation.text])
            elif companyLocation == None:
                csv_writer.writerow([job_title.text , companyName.text , None])
            else:
                csv_writer.writerow([])
           
except Exception as e:
    print(e)

