from django.db import models

class Education(models.Model):
    school = models.CharField(max_length=200)
    degree = models.CharField(max_length=200)
    field = models.CharField(max_length=200)
    start_date = models.DateField()
    end_date = models.DateField(null=True, blank=True)
    description = models.TextField()

    class Meta:
        ordering = ['-start_date']

    def __str__(self):
        return f"{self.degree} - {self.school}"

class Experience(models.Model):
    company = models.CharField(max_length=200)
    position = models.CharField(max_length=200)
    location = models.CharField(max_length=200)
    start_date = models.DateField()
    end_date = models.DateField(null=True, blank=True)
    description = models.TextField()

    class Meta:
        ordering = ['-start_date']

    def __str__(self):
        return f"{self.position} - {self.company}"

class TechnicalSkill(models.Model):
    category = models.CharField(max_length=100)
    skills = models.TextField()

    def __str__(self):
        return self.category

class Project(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    technologies = models.TextField()
    date = models.DateField()

    class Meta:
        ordering = ['-date']

    def __str__(self):
        return self.title 