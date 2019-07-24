# ScrapingCourses
a short program that scrapes course categorization rules from UVA's Lou's List.

## Why create this program?

This program only suits for those who want to categorize classes of Fall Term 2019 in University of Virginia. 

When assisting building another program that aims to offer Chinese international students a platform to check reviews and ratings of courses, the team encountered a problem. For the sake of better user experience, we need to categorize the courses. In this way, students who are looking for courses to enroll can find them more easily. The best criteria for categorization are "department" and "school." Therefore, I went to Lou's List, an unofficial course-listing website and web-scraped its categorization rules. 

The final result is stored as dict{"Category of departments": dict{"Department Name": list("Subjects")}}.

## Libraries Used
1. [BeautifulSoup:](https://www.crummy.com/software/BeautifulSoup/bs4/doc)
  - BeautifulSoup is a Python library for pulling data out of HTML and XML files.
2. [re](https://docs.python.org/3/library/re.html)
  - This module provides regular expression matching operations similar to those found in Perl.

## Data Sources
1. [Lou's List](https://rabi.phys.virginia.edu/mySIS/CS2/)
  - an unofficial website displaying class schedules in University of Virginia
  - made by Professor Lou Bloomfield
