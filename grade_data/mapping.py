def get_mapping():
    return {
        "school": {
            "name": "School",
            "description": "Student's school (binary: 'GP' - Gabriel Pereira or 'MS' - Mousinho da Silveira)",
            "type": "Categorical",
            "demographic": None
        },
        "sex": {
            "name": "Sex",
            "description": "Student's sex (binary: 'F' - female or 'M' - male)",
            "type": "Binary",
            "demographic": "Sex"
        },
        "age": {
            "name": "Age",
            "description": "Student's age (numeric: from 15 to 22)",
            "type": "Integer",
            "demographic": "Age"
        },
        "address": {
            "name": "Address",
            "description": "Student's home address type (binary: 'U' - urban or 'R' - rural)",
            "type": "Categorical",
            "demographic": None
        },
        "famsize": {
            "name": "Family Size",
            "description": "Family size (binary: 'LE3' - less or equal to 3 or 'GT3' - greater than 3)",
            "type": "Categorical",
            "demographic": "Other"
        },
        "Pstatus": {
            "name": "Parental Status",
            "description": "Parent's cohabitation status (binary: 'T' - living together or 'A' - apart)",
            "type": "Categorical",
            "demographic": "Other"
        },
        "Medu": {
            "name": "Mother's Education",
            "description": "Mother's education (numeric: 0 - none, 1 - primary education (4th grade), 2 - 5th to 9th grade, 3 - secondary education, 4 - higher education)",
            "type": "Integer",
            "demographic": "Education Level"
        },
        "Fedu": {
            "name": "Father's Education",
            "description": "Father's education (numeric: 0 - none, 1 - primary education (4th grade), 2 - 5th to 9th grade, 3 - secondary education, 4 - higher education)",
            "type": "Integer",
            "demographic": "Education Level"
        },
        "Mjob": {
            "name": "Mother's Job",
            "description": "Mother's job (nominal: 'teacher', 'health' care related, civil 'services' (e.g., administrative or police), 'at_home' or 'other')",
            "type": "Categorical",
            "demographic": "Occupation"
        },
        "Fjob": {
            "name": "Father's Job",
            "description": "Father's job (nominal: 'teacher', 'health' care related, civil 'services' (e.g., administrative or police), 'at_home' or 'other')",
            "type": "Categorical",
            "demographic": "Occupation"
        },
        "reason": {
            "name": "Reason for School Choice",
            "description": "Reason to choose this school (nominal: close to 'home', school 'reputation', 'course' preference, or 'other')",
            "type": "Categorical",
            "demographic": None
        },
        "guardian": {
            "name": "Guardian",
            "description": "Student's guardian (nominal: 'mother', 'father' or 'other')",
            "type": "Categorical",
            "demographic": None
        },
        "traveltime": {
            "name": "Travel Time",
            "description": "Home to school travel time (numeric: 1 - <15 min., 2 - 15 to 30 min., 3 - 30 min. to 1 hour, or 4 - >1 hour)",
            "type": "Integer",
            "demographic": None
        },
        "studytime": {
            "name": "Study Time",
            "description": "Weekly study time (numeric: 1 - <2 hours, 2 - 2 to 5 hours, 3 - 5 to 10 hours, or 4 - >10 hours)",
            "type": "Integer",
            "demographic": None
        },
        "failures": {
            "name": "Failures",
            "description": "Number of past class failures (numeric: n if 1<=n<3, else 4)",
            "type": "Integer",
            "demographic": None
        },
        "schoolsup": {
            "name": "School Support",
            "description": "Extra educational support (binary: yes or no)",
            "type": "Binary",
            "demographic": None
        },
        "famsup": {
            "name": "Family Support",
            "description": "Family educational support (binary: yes or no)",
            "type": "Binary",
            "demographic": None
        },
        "paid": {
            "name": "Paid Classes",
            "description": "Extra paid classes within the course subject (Math or Portuguese) (binary: yes or no)",
            "type": "Binary",
            "demographic": None
        },
        "activities": {
            "name": "Extracurricular Activities",
            "description": "Extra-curricular activities (binary: yes or no)",
            "type": "Binary",
            "demographic": None
        },
        "nursery": {
            "name": "Nursery",
            "description": "Attended nursery school (binary: yes or no)",
            "type": "Binary",
            "demographic": None
        },
        "higher": {
            "name": "Higher Education",
            "description": "Wants to take higher education (binary: yes or no)",
            "type": "Binary",
            "demographic": None
        },
        "internet": {
            "name": "Internet Access",
            "description": "Internet access at home (binary: yes or no)",
            "type": "Binary",
            "demographic": None
        },
        "romantic": {
            "name": "Romantic Relationship",
            "description": "With a romantic relationship (binary: yes or no)",
            "type": "Binary",
            "demographic": None
        },
        "famrel": {
            "name": "Family Relationship Quality",
            "description": "Quality of family relationships (numeric: from 1 - very bad to 5 - excellent)",
            "type": "Integer",
            "demographic": None
        },
        "freetime": {
            "name": "Free Time After School",
            "description": "Free time after school (numeric: from 1 - very low to 5 - very high)",
            "type": "Integer",
            "demographic": None
        },
        "goout": {
            "name": "Going Out with Friends",
            "description": "Going out with friends (numeric: from 1 - very low to 5 - very high)",
            "type": "Integer",
            "demographic": None
        },
        "Dalc": {
            "name": "Workday Alcohol Consumption",
            "description": "Workday alcohol consumption (numeric: from 1 - very low to 5 - very high)",
            "type": "Integer",
            "demographic": None
        },
        "Walc": {
            "name": "Weekend Alcohol Consumption",
            "description": "Weekend alcohol consumption (numeric: from 1 - very low to 5 - very high)",
            "type": "Integer",
            "demographic": None
        },
        "health": {
            "name": "Health Status",
            "description": "Current health status (numeric: from 1 - very bad to 5 - very good)",
            "type": "Integer",
            "demographic": None
        },
        "absences": {
            "name": "Absences",
            "description": "Number of school absences (numeric: from 0 to 93)",
            "type": "Integer",
            "demographic": None
        },
        "G1": {
            "name": "First Period Grade",
            "description": "First period grade (numeric: from 0 to 20)",
            "type": "Integer",
            "demographic": None
        },
        "G2": {
            "name": "Second Period Grade",
            "description": "Second period grade (numeric: from 0 to 20)",
            "type": "Integer",
            "demographic": None
        },
        "G3": {
            "name": "Final Grade",
            "description": "Final grade (numeric: from 0 to 20, output target)",
            "type": "Integer",
            "demographic": None
        }
    }
