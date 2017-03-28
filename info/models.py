from django.db import models


class Teacher(models.Model):
    last_name = models.CharField(verbose_name='Фамилия', max_length=50)
    first_name = models.CharField(verbose_name='Имя', max_length=50)
    middle_name = models.CharField(verbose_name='Отчество', max_length=50)

    def __str__(self):
        return self.last_name + ' ' + self.first_name + ' ' + self.middle_name

    class Meta:
        verbose_name = 'Преподаватель'
        verbose_name_plural = 'Преподаватели'
        ordering = ['last_name', 'first_name', 'middle_name']

    def as_json(self):
        return dict(last_name=self.last_name,
                    first_name=self.first_name,
                    middle_name=self.middle_name
                    )


class Lesson(models.Model):
    name = models.CharField(verbose_name='Имя предмета', max_length=50, unique=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Урок'
        verbose_name_plural = 'Уроки'
        ordering = ['name']

    def as_json(self):
        return dict(name=self.name)


class Cabinet(models.Model):
    number = models.IntegerField(verbose_name='Номер кабинета', unique=True)

    def __str__(self):
        return str(self.number)

    class Meta:
        verbose_name = 'Кабинет'
        verbose_name_plural = 'Кабинеты'
        ordering = ['number']

    def as_json(self):
        return dict(number=self.number)


class Group(models.Model):
    number = models.IntegerField(verbose_name='Номер группы', unique=True)

    def __str__(self):
        return str(self.number)

    class Meta:
        verbose_name = 'Группа'
        verbose_name_plural = 'Группы'

    def as_json(self):
        return dict(number=self.number)




