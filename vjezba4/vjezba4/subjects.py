#!python.exe

from http import cookies
import os
import cgi 

subjects = {
    'ip' : { 'name' : 'Introduction to programming' , 'year' : 1, 'ects' : 6 },
    'c1' : { 'name' : 'Calculus 1' , 'year' : 1, 'ects' : 7 },
    'cu' : { 'name' : 'Computer usage' , 'year' : 1, 'ects' : 5 },
    'dmt' : { 'name' : 'Digital and microprocessor technology', 'year' : 1, 'ects' : 6 },
    'db' : { 'name' : 'Databases' , 'year' : 2, 'ects' : 6 },
    'c2' : { 'name' : 'Calculus 2' , 'year' : 2, 'ects' : 7 },
    'dsa' : { 'name' : 'Data structures and alghoritms' , 'year' : 2, 'ects' : 5 },
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
    'not' : 'Not selected',
    'enr' : 'Enrolled',
    'pass' : 'Passed',
}

def get_subjects():
    return subjects 

def decide_year(year=None):
    cookies_string = os.environ.get('HTTP_COOKIE', '')
    all_cookies_object = cookies.SimpleCookie(cookies_string)
    if year is not None:
        cookie = cookies.SimpleCookie()
        cookie['year'] = year
        print (cookie.output())
    elif all_cookies_object.get('year'):
        year = all_cookies_object.get('year').value
    else:
        year = '1st Year'
    return year

def display_year():
    for key in year_names:
        print('<form action="" method="post">')
        print('<input type="submit" value="' + year_names.get(key) + '">') 


def display_subjects_of_year(year, params):
        for key in year_ids:
             if(key == year):  
                year = year_ids.get(key) 
        for key, subj in subjects.items():
                if(subj.get('year') == year):
                    print("""
                        </td>
                    </tr>
                    <tr>
                        <td>""")
                    print(str(subj.get('name'))) 
                    print("""
                        </td>
                        <td></td>
                        <td>""")
                    display_status(params, key)
                    print("""
                        </td>""")

def display(year, keys, status):
    for key in year_ids:
        if(key == year):  
            year = year_ids.get(key) 
    for key, subj in subjects.items():
            if(subj.get('year') == year):
                print("""
                    </td>
                </tr>
                <tr>
                    <td>""")
                print(str(subj.get('name'))) 
                print("""
                    </td>
                    <td></td>
                    <td>""")
                for k in status_names:
                    print('<input type="radio" name="' + keys + '" value="' + k + '"')
                    if cook_sub(keys,k,status):
                        print('checked')
                    print('/>' + status_names.get(k) + '')  
                print("""
                    </td>""")
                    

def cookies_sub(name,value,params):
    
    cookies_str = os.environ.get('HTTP_COOKIE', '')
    cookie= cookies.SimpleCookie(cookies_str)
    
    if(params.getvalue(name) == value):
        return 1
    elif(cookie.get(str(name))):
        if(cookie.get(str(name)).value == value):
            return 1
    else:
        return 0

def cook_sub(keys,k, status):
    
    cookies_str = os.environ.get('HTTP_COOKIE', '')
    cookie= cookies.SimpleCookie(cookies_str)
    
    if(status == k):
        return 1
    elif(cookie.get(str(keys))):
        if(cookie.get(str(keys)).value == k):
            return 1
    else:
        return 0

def display_status(params, name):
     for key in status_names:
        print('<input type="radio" name="' + name + '" value="' + key + '"')
        if cookies_sub(name,key,params):
            print('checked')
        print('/>' + status_names.get(key) + '')        

def get_all(cookies):
    all = 0
    for key, value in subjects.items():
        print("""
        <tr>
            <td>""")
        print('<br>'+ value.get('name'))
        print("""
        </td>""")
        print("""
        <td>""")
        print(cookies.get(str(key)).value)
        print("""
            </td>""")
        if(cookies.get(key).value == 'enr'):
            all +=value.get('ects')
        print("""
        <td>""")    
        print(str(value.get('ects')))
        print("""
        </tr>
            </td>""")
    print("""
        <td>
        </td>
        <td>
        """)    
    print('Total: ')
    print("""
        <td>
        """)
    print(all)
    print("""
        </td>""")