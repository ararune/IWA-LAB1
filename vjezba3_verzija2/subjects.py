import cgi
import os
from http import cookies

params = cgi.FieldStorage()

year = '1st Year' if params.getvalue('year') is None else params.getvalue('year')


subjects = {
    'ip' : { 'name' : 'Introduction to programming' , 'year' : 1, 'ects' : 6 },
    'c1' : { 'name' : 'Calculus 1' , 'year' : 1, 'ects' : 7 },
    'cu' : { 'name' : 'Computer usage' , 'year' : 1, 'ects' : 5 },
    'dmt' : { 'name' : 'Digital and microprocessor technology', 'year' : 1, 'ects' : 6 },
    'db' : { 'name' : 'Databases' , 'year' : 2, 'ects' : 6 },
    'c2' : { 'name' : 'Calculus 2' , 'year' : 2, 'ects' : 7 },
    'dsa' : { 'name' : 'Data structures and algorithms' , 'year' : 2, 'ects' : 5 },
    'ca' : { 'name' : 'Computer architecture', 'year' : 2, 'ects' : 6 },
    'isd' : { 'name' : 'Information systems design' , 'year' : 3, 'ects' : 5 },
    'c3' : { 'name' : 'Calculus 3' , 'year' : 3, 'ects' : 7 },
    'sa' : { 'name' : 'Server Architecture' , 'year' : 3, 'ects' : 6 },
    'cds' : { 'name' : 'Computer and data security', 'year' : 3, 'ects' : 6 }
    }
        
year_names = {
        1 : '1st Year',
        2 : '2nd Year',
        3 : '3rd Year'
    }

year_ids = {
        '1st Year' : 1,
        '2nd Year' : 2,
        '3rd Year' : 3
}

status_names = {
    'pass' : 'Passed',
    'enr' : 'Enrolled',
    'not' : 'Not selected',
}
def get_all_subjects_by_year(year='1st Year'):
    year_id = year_ids[year]
    all_subjects = [(k, v) for k, v in subjects.items() if v['year'] == year_id]
    return all_subjects


def create_cookie():
    for i in params:
        value = params.getvalue(i)
        cookie = cookies.SimpleCookie()
        # set the cookie's key-value pair
        cookie[i] = value
        # print the cookie's HTTP header
        print(cookie.output())


def get_all_statuses_from_cookie(subjects):
    """
    Gets the statuses for each subject from the cookie, or 'not' if no status exists.
    """
    cookies_string = os.environ.get('HTTP_COOKIE', '')
    all_cookies_object = cookies.SimpleCookie(cookies_string)
    
    all_subject_statuses = []
    
    for subject in subjects:
        # check if the subject's status was submitted via POST
        if params.getvalue(subject[0]) is not None:
            all_subject_statuses.append((subject[0], params.getvalue(subject[0])))
        # check if the subject's status is stored in a cookie
        elif subject[0] in all_cookies_object:
            all_subject_statuses.append((subject[0], all_cookies_object.get(subject[0]).value))
        # if the subject has no status, set it to 'not'
        else:
            all_subject_statuses.append((subject[0], 'not'))
    
    return all_subject_statuses