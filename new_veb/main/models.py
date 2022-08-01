from django.db import models

class Task(models.Model):
    title=models.CharField("Название",max_length=50)
    task=models.TextField("Описание")
    data=models.DateTimeField(auto_now_add="")



    def __str__(self):
        return self.title



