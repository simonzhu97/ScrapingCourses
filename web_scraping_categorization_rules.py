# -*- coding: utf-8 -*-
# author: Simon Zhu
# The data to be scraped is from UVA's unofficial course website "Lou's List",
# created by Professor Lou Bloomfield.
# The website is https://rabi.phys.virginia.edu/mySIS/CS2
# You are welcome to freely use the result of this small project.

# Import libraries
import requests
import urllib.request
import time
from bs4 import BeautifulSoup

# Set the URL you want to webscrape from
url = 'https://rabi.phys.virginia.edu/mySIS/CS2/'

# Connect to the URL
response = requests.get(url)

# Parse HTML and save to BeautifulSoup object¶
soup = BeautifulSoup(response.text, "html.parser")

# now from the Internet scrape the bijective relationship between a subject name and its mnemonic 
# (e.g: Computer Science to CS)
url_3 = "https://rabi.phys.virginia.edu/mySIS/CS2/page.php?Semester=1198&Type=Group&Group=CS"
res_3 = requests.get(url_3)
soup_3 = BeautifulSoup(res_3.text, "html.parser")

import re
department = soup_3.find("td",{"class":"UnitName"})
regex = re.compile('[^A-Z]')
mne_dict ={}
while department:
  mne = department.find_next("td",{"class":"CourseNum"})
  mne_text = mne.get_text()[1:5]
  mne_dict[department.get_text()] = regex.sub('',mne_text)
  department = mne.find_next("td",{"class":"UnitName"})

# a method that finds the subjects in each department
def find_subs(parser,d_dict,idx):
  subjects = parser.find_all('td',{"class":"UnitName"})
  out = []
  # add the corresponding mnemonic to the list
  for s in subjects: out.append(mne_dict[s.get_text()])
  d_dict[idx] = out

# a method that finds the departments under each categories and then furthermore 
# find the subjects
def find_departs(cat,cat_dict,cat_idx):
  # find all the departments in this category
  departs=cat.find_all('td',{"class":"IndexTable4"})
  d_dict = {}
  for depart in departs:
    idx = depart.get_text()
#     print(idx)
    if depart.a: url_2 = url + depart.a['href']
    res = requests.get(url_2)
    b_soup = BeautifulSoup(res.text, "html.parser")
    # jump to the corresponding url and then find all the subjects in that department
    find_subs(b_soup,d_dict,idx)
    cat_dict[cat_idx] = d_dict

# create the final dictionary that has all the information
num_cats = 7
cat = soup.find('h3')
cat_dict={}
for i in range(num_cats):
  a_table = cat.find_next('table')
#   print(cat.get_text())
  find_departs(a_table,cat_dict,cat.get_text())
  cat = a_table.find_next('h3')

print(cat_dict)
