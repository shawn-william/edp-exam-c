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
