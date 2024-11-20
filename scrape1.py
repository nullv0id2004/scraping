from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Set up Chrome options
chrome_options = Options()
chrome_options.add_argument("--headless")  # Run headless Chrome

# Initialize the WebDriver
driver = webdriver.Chrome()

# Open the webpage
driver.get('https://internshala.com/internships/computer-science-internship/stipend-10000/')  # Replace with the actual URL

# Function to extract text from elements safely
def get_text(element):
    return element.text.strip() if element else ""

data = []

# Define a wait object
wait = WebDriverWait(driver, 10)

while True:
    # Find all the job postings
    job_postings = driver.find_elements(By.CLASS_NAME, 'individual_internship')
    
    for i, job in enumerate(job_postings):
        try:
            # Re-locate the job element to avoid stale reference
            job = wait.until(EC.presence_of_all_elements_located((By.CLASS_NAME, 'individual_internship')))[i]

            # Extract job role
            job_role = get_text(job.find_element(By.CLASS_NAME, 'job-internship-name'))

            # Extract company name
            company_name = get_text(job.find_element(By.CLASS_NAME, 'company-name'))

            # Extract location
            location = get_text(job.find_element(By.CLASS_NAME, 'locations').find_element(By.TAG_NAME, 'a'))

            # Extract stipend
            stipend = get_text(job.find_element(By.CLASS_NAME, 'stipend'))

            # # Get the detail page URL from the data-href attribute
            # detail_page_url = job.get_attribute('data-href')
            # full_detail_page_url = 'https://internshala.com' + detail_page_url  # Replace BASE_URL with the actual base URL if necessary

            # # Navigate to the detail page
            # driver.get(full_detail_page_url)

            # # Wait for the detail page to load
            # wait.until(EC.presence_of_element_located((By.CLASS_NAME, 'internship_meta')))

            # # Extract "Who can apply"
            # who_can_apply = [get_text(li) for li in driver.find_elements(By.CSS_SELECTOR, 'div:contains("Who can apply") + ul li')]

            # # Extract "Other requirements"
            # other_requirements = [get_text(li) for li in driver.find_elements(By.CSS_SELECTOR, 'div:contains("Other requirements") + ul li')]

            data.append({
                'job_role': job_role,
                'company_name': company_name,
                'location': location,
                'stipend': stipend,
                # 'who_can_apply': who_can_apply,
                # 'other_requirements': other_requirements
            })

            # Go back to the main page
            # driver.back()

            # Wait for the main page to load
            wait.until(EC.presence_of_element_located((By.CLASS_NAME, 'individual_internship')))

        except Exception as e:
            print(f"Error: {e}")

    # Optionally, handle pagination here to move to the next page if there are more job postings

    break  # Exit the loop if no more pages to scrape

# Print the extracted data
for item in data:
    print(item)

# Close the driver
driver.quit()
