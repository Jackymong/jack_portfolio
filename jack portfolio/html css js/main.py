from bs4 import BeautifulSoup
import requests

# with open('home.html', 'r') as html_file:
#     content = html_file.read()
#     # print(content)

#     soup = BeautifulSoup(content, 'lxml')
#     # tags = soup.find('h5')
#     tags = soup.find_all('h5')
#     # print(tags)
#     for tag in tags:
#         print(tag.text)

html_text = requests.get('https://www.timesjobs.com/candidate/job-search.html?searchType=personalizedSearch&from=submit&searchTextSrc=&searchTextText=&txtKeywords=&txtLocation=Enter+Location&cboWorkExp1=-1').text
# print(html_text)
soup = BeautifulSoup(html_text,'lxml')
jobs = soup.find('li', class_= 'clearfix job-bx wht-shd-bx')
company_name = jobs.find('h3', class_ = 'joblist-comp-name').text.replace(' ','').split()[1:]
print(company_name)