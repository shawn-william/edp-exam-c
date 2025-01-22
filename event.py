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
