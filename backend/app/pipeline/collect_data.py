import requests
from bs4 import BeautifulSoup
import pandas as pd

from logger.logging_utils import print_progress_bar, start_timing, finish_timing, log


def collect_data(city, field):

    # Create dataframe
    data = pd.DataFrame(columns=["Title", "Link", "Offer ID", "Employer", "Job Location", "Salary", "When Posted"])

    data = _identify_all_job_postings(data, city, field)

    data = _get_description_of_all_job_postings(data)

    return data


def _identify_all_job_postings(data, city, field):

    start = start_timing("IDENTIFYING ALL JOB POSTINGS")

    # Find all job postings
    page_num = 1
    while True:

        # Get the page
        response = requests.get(f"https://www.profesia.sk/praca/{city}/{field}/?page_num={page_num}")
        response.raise_for_status()  # Raise error if request failed
        soup = BeautifulSoup(response.text, "html.parser")

        # If page doesnt have any job postings finish the loop
        job_postings = soup.find_all("li", class_="list-row")
        if job_postings == []:
            break

        # Print progress info
        log(f"PAGE NUMBER: {page_num}", delete_last_line=True)

        # Extract all job postings from the page
        for job_posting in job_postings:
            
            # If the entry doesnt have an h2 it is not a job posting
            # Go to the next entry
            if not job_posting.find("h2"): 
                continue

            # Extract data from the job posting
            title = job_posting.find("h2").find("a").find("span").get_text(strip=True)
            link = job_posting.find("h2").find("a").get("href")
            offer_id = job_posting.find("h2").find("a").get("id")
            employer = job_posting.find("span", class_="employer").get_text(strip=True)
            job_location = job_posting.find("span", class_="job-location").get_text(strip=True)
            when_posted = job_posting.find("div", class_="list-footer").find("div").find("div", class_="list-footer-right").find("span").find("strong").get_text(strip=True)

            try:
                salary = job_posting.find("span", class_="label-group").find("a", attrs={"data-dimension7": "Salary label"}).find("span").get_text(strip=True)
            except AttributeError:
                salary = None

            # Add job posting data to the dataframe
            data.loc[len(data)] = [title, link, offer_id, employer, job_location, salary, when_posted]

        page_num +=1

    finish_timing(start, progress_bar=True)

    return data


def _get_description_of_all_job_postings(data):

    start = start_timing("VISITING EVERY JOB POSTING'S PAGE AND EXTRACTING DESCRIPTION")

    # Add new column
    data["Description"] = None

    # Go to every posting's page and extract job description
    for index, row in data.iterrows():
        
        # Print progress info
        print_progress_bar(index+1, len(data))

        # Go to the page
        response = requests.get(f"https://www.profesia.sk{row["Link"]}")
        response.raise_for_status()  # Raise error if request failed
        soup = BeautifulSoup(response.text, "html.parser")

        # Extract description
        description = soup.find("div", id="content").find("div", class_="container").find("div", class_="row").find("main", id="detail").find("div", class_="card-content")
        description = description.get_text(" ", strip=True)
        
        # Add it to the dataframe
        data.loc[index, "Description"] = description

    finish_timing(start, progress_bar=True)

    return data
