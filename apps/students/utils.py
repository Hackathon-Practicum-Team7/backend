import pandas as pd

from django.db.models import QuerySet


def get_dataframe(students: QuerySet) -> pd.DataFrame:
    """Формирование датафрейма для записи к эксель"""

    data = []

    for student in students:
        stud_dict = {}
        stud_dict["name"] = "\n".join([student.surname, student.name])
        stud_dict["profession"] = student.profession.title
        stud_dict["city"] = student.city.title
        stud_dict["grade"] = student.grade.title
        stud_dict["contact"] = "\n".join(
            [student.contact.telegram, student.contact.email]
        )
        skills = []
        for skill in student.skills.all():
            skills.append(skill.title)
        stud_dict["skils"] = "\n".join(skills)
        employment_types = []
        for empl_typ in student.employment_types.all():
            employment_types.append(empl_typ.title)
        stud_dict["empl_typ"] = "\n".join(employment_types)
        working_condition = []
        for work_cond in student.working_condition.all():
            working_condition.append(work_cond.title)
        stud_dict["work_cond"] = "\n".join(working_condition)
        data.append(stud_dict)

    df = pd.DataFrame(data)

    df.rename(columns={
        "name": "Профиль",
        "profession": "Профессия",
        "city": "Город",
        "grade": "Уровень",
        "skills": "Ключевые навыки",
        "contact": "Контакты",
        "empl_typ": "Тип занятости",
        "work_cond": "Условия работы"
    }, inplace=True)

    return df
