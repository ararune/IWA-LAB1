#!python.exe

subjects = {
    'ip': {'name': 'Introduction to programming', 'year': 1, 'ects': 6},
    'c1': {'name': 'Calculus 1', 'year': 1, 'ects': 7},
    'cu': {'name': 'Computer usage', 'year': 1, 'ects': 5},
    'dmt': {'name': 'Digital and microprocessor technology', 'year': 1, 'ects': 6},
    'db': {'name': 'Databases', 'year': 2, 'ects': 6},
    'c2': {'name': 'Calculus 2', 'year': 2, 'ects': 7},
    'dsa': {'name': 'Data structures and alghoritms', 'year': 2, 'ects': 5},
    'ca': {'name': 'Computer architecture', 'year': 2, 'ects': 6},
    'isd': {'name': 'Information systems design', 'year': 3, 'ects': 5},
    'c3': {'name': 'Calculus 3', 'year': 3, 'ects': 7},
    'sa': {'name': 'Server Architecture', 'year': 3, 'ects': 6},
    'cds': {'name': 'Computer and data security', 'year': 3, 'ects': 6}
}

year_names = {
    1: '1st Year',
    2: '2nd Year',
    3: '3rd Year',
}

year_ids = {
    '1st Year': 1,
    '2nd Year': 2,
    '3rd Year': 3
}

status_names = {
    'not': 'Not selected',
    'enr': 'Enrolled',
    'pass': 'Passed',
}

def get_all_subjects_by_year(year = '1st Year'):
    year_id = year_ids[year]
    all_subjects_touples = [(k, v) for k, v in subjects.items()]
    all_subjects = []
    for subject in all_subjects_touples:
        if subject[1]['year'] == year_id:
            all_subjects.append(subject)
    return all_subjects

def get_all_statuses_from_session(subjects, data):
    all_subject_statuses = []
    for subject in subjects:
        if subject[0] in data:
            all_subject_statuses.append((subject[0], data[subject[0]]))
        else:
            all_subject_statuses.append((subject[0], 'not'))
    return all_subject_statuses