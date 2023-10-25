import pandas as pd


def get_dataframe(students):
    data = []
    for student in students:
        stud_dict = {}
        stud_dict["name"] = student.name
        stud_dict["surname"] = student.surname
        stud_dict["city"] = student.city.title
        stud_dict["profession"] = student.profession.title
        stud_dict["grade"] = student.grade.title
        stud_dict["contact"] = [
            student.contact.telegram, student.contact.email
        ]
        stud_dict["skills"] = []
        for skill in student.skills.all():
            stud_dict["skills"].append(skill.title)
        stud_dict["empl_typ"] = []
        for empl_typ in student.employment_types.all():
            stud_dict["empl_typ"].append(empl_typ.title)
        stud_dict["work_cond"] = []
        for work_cond in student.working_condition.all():
            stud_dict["work_cond"].append(work_cond.title)
        data.append(stud_dict)
    df = pd.DataFrame(data)
    df.rename(columns={
        "name": "Имя",
        "surname": "Фамилия",
        "city": "Город",
        "profession": "Профессия",
        "grade": "Уровень",
        "skills": "Ключевые навыки",
        "contact": "Контакты",
        "empl_typ": "Тип занятости",
        "work_cond": "Условия работы"
    }, inplace=True)
    return df
