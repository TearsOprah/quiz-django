from django.db import models


DIFF_CHOICES = (
    ('easy', 'easy'),
    ('medium', 'medium'),
    ('hard', 'hard'),
)


class Quiz(models.Model):
    name = models.CharField(max_length=120)
    topic = models.CharField(max_length=120)
    number_of_questions = models.IntegerField()
    time = models.IntegerField(help_text='Максимальное время на выполнение')
    required_score_to_pass = models.IntegerField(help_text='Минимальный результат для прохождения')
    difficulty = models.CharField(max_length=6, choices=DIFF_CHOICES)

    def __str__(self):
        return f'{self.name}-{self.topic}'

    def get_questions(self):
        return self.question_set.all()