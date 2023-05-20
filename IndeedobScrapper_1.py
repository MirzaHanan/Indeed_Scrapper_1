# Importing necessary libraries
from csv import writer
import csv
from tkinter.messagebox import NO
import requests
from bs4 import BeautifulSoup

try:
    # URL of the webpage to scrape
    url = "https://au.indeed.com/data-analyst-jobs-in-Australia"

    # Sending a GET request to the webpage
    page = requests.get(url)
    print(page)

    # Creating a BeautifulSoup object to parse the HTML content
    soup = BeautifulSoup(page.content, "html.parser")

    # Finding the job search results section in the HTML
    jobSearchResults = soup.find("ul", class_="jobsearch-ResultsList css-0")

    # Field names for the CSV file
    field_name = ["Job Title", "Company Name", "Location"]

    # Opening the CSV file in write mode
    with open("job.csv", "w", newline="") as f:
        csv_writer = csv.writer(f, delimiter=",")
        csv_writer.writerow(field_name)

        # Iterating over each job search result
        for jobSearchResult in jobSearchResults:
            print()
            # Finding the job title within the result
            title = jobSearchResult.find("h2", class_="jobTitle")
            if title == None:
                continue
            for item in title:
                # Extracting the job title text
                job_title = item.find("span")
                if job_title == None:
                    pass
                else:
                    print(job_title.text)
            
            # Finding the company name within the result
            companyName = jobSearchResult.find("a", class_="companyOverviewLink")
            if companyName == None:
                pass
            else:
                print(companyName.text)

            # Finding the company location within the result
            companyLocation = jobSearchResult.find("div", class_="companyLocation")
            if companyLocation == None:
                pass
            else:
                print(companyLocation.text)

            # Writing the data to the CSV file
            if job_title != None and companyName != None and companyLocation != None:
                csv_writer.writerow([job_title.text, companyName.text, companyLocation.text])
            elif job_title == None:
                csv_writer.writerow([None, companyName.text, companyLocation.text])
            elif companyName == None:
                csv_writer.writerow([job_title.text, None, companyLocation.text])
            elif companyLocation == None:
                csv_writer.writerow([job_title.text, companyName.text, None])
            else:
                csv_writer.writerow([])

except Exception as e:
    print(e)
