from django.db import models
from info.models import Lesson, Cabinet, Teacher, Group

times = [   '09:00 - 09:45',
            '09:50 - 10:35',
            '10:55 - 11:40',
            '11:45 - 12:30',
            '13:00 - 13:45',
            '13:50 - 14:35',
            '14:45 - 15:30',
            '15:35 - 16:20',
            '16:25 - 17:10',
            '17:15 - 18:00'
]


class TeachLesson(models.Model):
    #teacher = models.OneToOneField(Teacher)123
    teacher = models.ForeignKey(Teacher, verbose_name='Преподаватель')
    lesson = models.ForeignKey(Lesson, verbose_name='Преподает')
    cabinet = models.ForeignKey(Cabinet, verbose_name='Кабинет')

    def __str__(self):
        return self.lesson.name + ' ' + str(self.cabinet.number) + ' ' + self.teacher.last_name

    def as_json(self):
        return dict(teacher=self.teacher.as_json(),
                    lesson=self.lesson.as_json(),
                    cabinet=self.cabinet.as_json()
                    )

    class Meta:
        verbose_name = 'Преподавание'
        verbose_name_plural = 'Преподавания'


class DaySchedule(models.Model):
    # teacher = models.OneToOneField(Teacher)123
    one = models.ForeignKey(TeachLesson, verbose_name='1 пара', related_name='one', null=True, blank=True)
    two = models.ForeignKey(TeachLesson, verbose_name='2 пара', related_name='two', null=True, blank=True)
    three = models.ForeignKey(TeachLesson, verbose_name='3 пара', related_name='three', null=True, blank=True)
    four = models.ForeignKey(TeachLesson, verbose_name='4 пара', related_name='four', null=True, blank=True)
    five = models.ForeignKey(TeachLesson, verbose_name='5 пара', related_name='five', null=True, blank=True)

    def __str__(self):
        return '{} {} {} {} {}'.format(self.one.lesson, self.two.lesson, self.three.lesson, self.four.lesson, self.five.lesson)

    def as_json(self):
        return dict(one=self.one.as_json() if self.one else None,
                    two=self.two.as_json() if self.two else None,
                    three=self.three.as_json() if self.three else None,
                    four=self.four.as_json() if self.four else None,
                    five=self.five.as_json() if self.five else None,
                    )

    class Meta:
        verbose_name = 'Дневное расписание'
        verbose_name_plural = 'Дневные расписания'


class GroupSchedule(models.Model):
    # teacher = models.OneToOneField(Teacher)123python
    group = models.OneToOneField(Group, verbose_name='Группа')
    monday = models.ForeignKey(DaySchedule, verbose_name='Понедельник', related_name='monday', null=True, blank=True)
    tuesday = models.ForeignKey(DaySchedule, verbose_name='Вторник', related_name='tuesday', null=True, blank=True)
    wednesday = models.ForeignKey(DaySchedule, verbose_name='Среда', related_name='wednesday', null=True, blank=True)
    thursday = models.ForeignKey(DaySchedule, verbose_name='Четверг', related_name='thursday', null=True, blank=True)
    friday = models.ForeignKey(DaySchedule, verbose_name='Пятница', related_name='friday', null=True, blank=True)
    saturday = models.ForeignKey(DaySchedule, verbose_name='Суббота', related_name='saturday', null=True, blank=True)

    def __str__(self):
        return str(self.group.number)

    class Meta:
        verbose_name = 'Расписание группы'
        verbose_name_plural = 'Расписания групп'

    def as_json(self):
        return dict(group=self.group.as_json(),
                    monday=self.monday.as_json() if self.monday else None,
                    tuesday=self.tuesday.as_json() if self.tuesday else None,
                    wednesday=self.wednesday.as_json() if self.wednesday else None,
                    thursday=self.thursday.as_json() if self.thursday else None,
                    friday=self.friday.as_json() if self.friday else None,
                    saturday=self.saturday.as_json() if self.saturday else None
                    )
