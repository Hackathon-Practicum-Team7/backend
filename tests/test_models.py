def test_city_creation(city):
    assert city.title == "Test City"


def test_employment_type_creation(employment_type):
    assert employment_type.title == "Test Employment Type"


def test_grade_creation(grade):
    assert grade.title == "Test Grade"


def test_profession_creation(profession):
    assert profession.title == "Test Profession"


def test_skill_creation(skill):
    assert skill.title == "Test Skill"


def test_working_condition_creation(working_condition):
    assert working_condition.title == "Test Working Condition"


def test_student_creation(student):
    assert student.name == "Oleg"
    assert student.surname == "Lee"
    assert student.about == "Test Student"
    assert student.is_looking_for_job is True
    assert student.has_portfolio is False


def test_contact_creation(contact):
    assert contact.email == "mail@mail.ru"
    assert contact.phone == "+7(926)000-00-00"
    assert contact.telegram == "http://t.me/ya"
    assert contact.portfolio == "http://ya.ru"
    assert contact.whatsapp == "+7(926)000-00-00"


def test_job_creation(job):
    assert job.organisation == "Test Company"
