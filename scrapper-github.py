import requests
from bs4 import BeautifulSoup
import csv

# Collect the github page
page = requests.get('https://github.com/trending')
# Create a BeautifulSoup object
soup = BeautifulSoup(page.text, 'html.parser')

# Get the repo list
repo_list =  soup.find_all("article", {"class": "Box-row"})

# Open writer with name
file_name = "github_trending_today.csv"
# set newline to be '' so that that new rows are appended without skipping any
f = csv.writer(open(file_name, 'w', newline=''))

# write a new row as a header
f.writerow(['Developer', 'Repo Name', 'Programming Language','Number of Stars'])

# Extract Developer name, repository name, Programming Language, Stars
for repo in repo_list:
    try:
        full_repo_name = repo.find(class_="h3 lh-condensed").text.split('/')
        developer = full_repo_name[0].strip()
        repo_name = full_repo_name[1].strip()
        programming_language = repo.find_all('span',{'itemprop':'programmingLanguage'})[0].text
        stars = repo.find(class_='octicon octicon-star').parent.text.strip()

        # add the information as a row into the csv table
        f.writerow([developer, repo_name, programming_language, stars])
    except Exception as e:
        print(e)
        

