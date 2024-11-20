from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import json
import pandas as pd
import csv
import time
driver = webdriver.Chrome()

driver.get("https://internshala.com/internships/computer-science-internship/stipend-10000/page-11/")
print(driver.title)
close = driver.find_element(By.ID, 'close_popup')
close.click()
job_postings = driver.find_elements(By.CLASS_NAME, 'individual_internship')
data = []

for job in job_postings:
    try:
        # Extract job role
        job_role = job.find_element(By.CLASS_NAME, 'job-internship-name').text.strip()

        # Extract company name
        company_name = job.find_element(By.CLASS_NAME, 'company-name').text.strip()

        # Extract location
        location = job.find_element(By.CLASS_NAME, 'locations').find_element(By.TAG_NAME, 'a').text.strip()

        # Extract stipend
        stipend = job.find_element(By.CLASS_NAME, 'stipend').text.strip()

        # Print the extracted details
        print(f"Job Role: {job_role}")
        print(f"Company Name: {company_name}")
        print(f"Location: {location}")
        print(f"Stipend: {stipend}")
        print('-' * 40)
        data.append({
            'job_role': job_role,
            'company_name': company_name,
            'location': location,
            'stipend': stipend,
        })

    except Exception as e:
        print(f"Error: {e}")


for item in data:
    print(item)

df = pd.DataFrame(data)

with open("sample.json", "a") as outfile:
    json.dump(data, outfile)

df.to_csv('internshalaBig.csv', mode = 'a' ,index=False)

# with open('internshala1.csv', 'a') as f:
#     writer = csv.writer(f)
#     writer.writerow(data)
# Close the driver
driver.quit()