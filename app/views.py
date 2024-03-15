from django.http import HttpResponse
from rest_framework.views import APIView
from .models import Student, Student_Finance, Student_Units, Unit_Info, CourseInfo
import re


class UssdCallback(APIView):
    def post(self, request, *args, **kwargs) -> str:
        session_id = request.POST.get('sessionId', None)
        serviceCode = request.POST.get("serviceCode", None)
        phone_number = request.POST.get("phoneNumber", None)
        text = request.POST.get("text", "default")
        response = ''
        student = None
        print(text)

        text = text.split("*")
        if len(text) > 1:
            reg_no = text[0]
            student = Student.objects.get(reg_no=reg_no)
            current_year = student.current_year
            current_semester = student.current_semester
            new_year = current_year + 1
            new_semester = current_semester

            if current_semester == 2:
                new_semester == 1

            else:
                new_semester = 2
            course = CourseInfo.objects.get(course_name=student.course)
            units = Unit_Info.objects.filter(
                semester=current_semester, year=current_year, course=course.pk)

        if len(text) == 1 and text[0] == '':
            response = 'CON Welcome to university USSD portal\n'
            response += 'Please enter you registration number to continue (or 0 to exit)'

        elif len(text) == 1 and re.match(r"^[a-zA-Z]{3}\d{3}-\d{4}/\d{4}$", text[0]):
            try:
                student = Student.objects.get(reg_no=text[0])
                response = f'CON Welcome {student.name}, chose your option:\n'
                response += '1. Student Finance\n'
                response += '2. Academics\n'
                response += '3. Feedback\n'
                response += '0. Exit'
            except Student.DoesNotExist:
                response = f'END Student with {text[0]} number does not exist'

        elif len(text) == 2 and text[-1] == '1':
            response = 'CON Student Finance\nChose your option:\n'
            response += '1. Check balance\n'
            response += '2. Pay fees\n'
            response += '0. Exit'

        elif len(text) == 3 and text[-1] == '1' and text[-2] == '1':
            response = 'END An sms will be sent to you with your fee balance'

        elif len(text) == 3 and text[-1] == '2' and text[-2] == '1':
            student_finace = Student_Finance.objects.get(student=student)
            response = 'CON This is your current fee balance:\n'
            response += f'Balance: {student_finace.balance}\n'
            response += f'Semester fee: {student_finace.fee}\n'
            response += f'Enter amount you wish to pay'

        elif len(text) == 4 and text[-3] == '1' and text[2] == '2':
            amount = int(text[-1])
            student_finace = Student_Finance.objects.get(student=student)
            student_finace.balance -= amount
            student_finace.save()
            response = 'END Payment successful'

        elif len(text) == 2 and text[-1] == '2':
            response = 'CON Academics\nChose your option:\n'
            response += '1. Session reporting\n'
            response += '2. Register units\n'
            response += '3. Results\n'

        elif text[-1] == '1' and text[-2] == '2' and len(text) == 3:
            response += 'CON Would you like to report for year {} semester {}?\n'.format(
                new_year, new_semester)
            response += '1. Yes\n'
            response += '0. No\n'

        elif len(text) == 4 and text[-1] == '1' and text[-2] == '1' and text[-3] == '2':
            student.current_semester = new_semester
            student.current_year = new_year
            student.save()

            response = 'END You have successfully reported for the year {} semester {}?\n'.format(
                new_year, new_semester)

        elif text[-1] == '2' and text[-2] == '2' and len(text) == 3:
            response = 'CON These are the current units for this session\n'
            print(current_year)
            print(current_semester)

            for unit in units:
                response += f'{unit.unit_code} - {unit.unit_name}\n'
            response += '1. Register\n'
            response += '0. Exit'

        elif len(text) == 4 and text[-1] == '1' and text[-2] == '2' and text[-3] == '2':
            for unit in units:
                student_unit = Student_Units.objects.create(
                    reg_no=student.pk, unit_code=unit.pk)
                student_unit.save()

            response = 'END You have successfully registered for year {} semister {} units'.format(
                current_year, current_semester)

        elif text[-1] == '2' and text[-2] == '3' and len(text) == 3:
            response = 'END An sms with your previous exam results will be sent to you'

        elif text[-1] == '3' and len(text) == 2:
            response = 'CON Feedback\nEnter your message'

        elif text[-1] == '0':
            response = 'END Thank you for using our service'

        return HttpResponse(response, content_type='text/plain')
