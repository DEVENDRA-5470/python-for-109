import requests
URL=r'http://lms.devilhai.info'

def create_students():
    data={
        "stu_name":"rohan",
        "stu_age":"2002-01-01",
        "stu_phone":"70000000",
        "stu_email":"test1@gmail.com",
        "stu_password":"test1234",
        "stu_address":"YE DATA PYTHON SE AYA HAI"
    }
    r=requests.post(f"{URL}/student/student-register",data=data,timeout=10)
    print(r.status_code)
create_students()

