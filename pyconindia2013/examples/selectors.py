""" Selecting values from an iterable using multiple conditions """

import itertools
import collections

cutoffs = {'maths': 40, 'elec': 35,
           'lab'  : 45, 'cs': 30,
           'phy'  : 25, 'chem': 35}

marks_dict = { 'Karan': {'maths': 39, 'elec': 78, 'cs': 83,
                         'lab': 32, 'phy': 60, 'chem': 91},
               'Arjun':  {'maths': 49, 'elec': 45, 'lab': 53,
                          'cs': 43, 'phy': 86, 'chem': 54},
               'Rancho': {'maths': 86, 'elec': 85, 'cs': 95,
                          'lab': 83, 'phy': 91, 'chem': 75},
               'Raju':   {'maths': 32, 'elec': 36, 'lab': 50,
                          'cs': 26, 'phy': 35, 'chem': 41},
               'Farhan': {'maths': 30, 'elec': 56, 'cs': 21,
                          'lab': 33, 'phy': 27, 'chem': 56}}

def find_passed(marks_dict,cutoffs):

    # Initialize dictionary
    pass_dict = {subject:[] for subject in cutoffs}
    
    for subject, cutoff in cutoffs.iteritems():
        for student, student_marks in marks_dict.iteritems():
            if student_marks[subject] >= cutoff:
                pass_dict[subject].append(student)

    return pass_dict

def find_passedi(marks_dict, cutoffs):

    # defaultdict
    pass_dict = collections.defaultdict(list)
    
    # Dict comprehensions
    selectors = {(subject, student) :cutoffs[subject]<=val[subject] for subject in cutoffs for student,val in marks_dict.items()}
    # itertools compress
    passd = list(itertools.compress(selectors.keys(), selectors.values()))

    for subject,student in passd:
        pass_dict[subject].append(student)

    return pass_dict

if __name__ == "__main__":
    passd = find_passed(marks_dict, cutoffs)
    print 'Passed =>',passd

    passd = find_passedi(marks_dict, cutoffs)
    print 'Passed =>',passd
