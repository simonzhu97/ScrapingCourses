# ScrapingCourses
a short program that scrapes course data from UVA's Lou's List.

## Why create this program?

When assisting building another program that aims to offer Chinese international students a platform to check reviews and ratings of courses, the team encountered a problem. For the sake of better user experience, we need to categorize the courses. In this way, students who are looking for courses to enroll can find them more easily. The best criteria for categorization are "department" and "school." Therefore, I went to Lou's List, an unofficial course-listing website and web-scraped its categorization rules. 

The final result is stored as dict{"Category of departments": dict{"Department Name": list("Subjects")}}.
