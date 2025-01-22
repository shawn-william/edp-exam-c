class Event:
    def __init__(self, name, payload):
        self.name = name
        self.payload = payload

class EnrollmentCertificateRequestEvent(Event):
    def __init__(self, student_id_number, date):
        super().__init__("enrollment_certificate_request", {"student_id_number": student_id_number, "date": date})

class EnrollmentCertificateIssuedEvent(Event):
    def __init__(self, student_id_number, is_confirmed):
        super().__init__("enrollment_certificate_issued", {"student_id_number": student_id_number, "is_confirmed": is_confirmed})

event_queue = []


class Student:
    def __init__(self, first_name, last_name, day_of_birth, address, phone_number, school_year, admission_number):
        self.first_name = first_name
        self.last_name = last_name
        self.day_birth = day_of_birth
        self.address = address
        self.phone_number = phone_number
        self.school_year = school_year
        self.admission_number = admission_number

    def ask_for_enrollment_certificate(self, date):
        event = EnrollmentCertificateRequestEvent(self.admission_number, date)
        event_queue.append(event)
        print('enrollment certificate request', event.name, 'sent!')

class University:
    def __init__(self, name, address, phone_number, email):
        self.name = name
        self.address = address
        self.phone_number = phone_number
        self.email = email

    def handle_enrollment_request(self, event):
        print(f"Received enrollment certificate request for student: {event.payload['student_id_number']} on {event.payload['date']}")
        issued_event = EnrollmentCertificateIssuedEvent(event.payload["student_id_number"], is_confirmed=True)
        event_queue.append(issued_event)
        print('enrollment certificate', issued_event.name, 'done!')


# Code Usage
shawn = Student("shawn", "fernandes", '7.02.2022', 'Maputo', '230194385', '34461', 'A12345')
liam = Student("liam", "fernandes", '9.02.2024', 'Maputo', '450276147', '89991', 'B91254')
allan = Student("allan", "marvin", '14.02.2020', 'Maputo', '259257639', '23441', 'C00229')

shawn.ask_for_enrollment_certificate('20.12.2024')
liam.ask_for_enrollment_certificate('21.12.2024')
allan.ask_for_enrollment_certificate('22.12.2024')

University_of_Technology_and_Arts = University('UTA', 'Warsaw, Ols 12', '234678987', 'uts@edu.tr')
