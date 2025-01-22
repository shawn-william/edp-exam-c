from event import EnrollmentCertificateRequestEvent

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
