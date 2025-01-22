from student import Student
from university import University

event_queue = []

# Code Usage
shawn = Student("shawn", "fernandes", '7.02.2022', 'Maputo', '230194385', '34461', 'A12345')
liam = Student("liam", "fernandes", '9.02.2024', 'Maputo', '450276147', '89991', 'B91254')
allan = Student("allan", "marvin", '14.02.2020', 'Maputo', '259257639', '23441', 'C00229')

shawn.ask_for_enrollment_certificate('20.12.2024')
liam.ask_for_enrollment_certificate('21.12.2024')
allan.ask_for_enrollment_certificate('22.12.2024')

University_of_Technology_and_Arts = University('UTA', 'Warsaw, Ols 12', '234678987', 'uts@edu.tr')

