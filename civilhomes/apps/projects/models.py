from django.db import models


class ProjectPlan(models.Model):
    sheet_url = models.URLField(max_length=200)
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class Location(models.Model):
    name = models.CharField(max_length=200)
    latitude = models.CharField(max_length=10)
    longitude = models.CharField(max_length=10)
    iframe_snippet = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.name


class Project(models.Model):
    status = (
        (1, "Not Started"),
        (2, "Ongoing"),
        (3, "Completed"),
        (4, "On Hold")
    )
    name = models.CharField(max_length=200)
    description = models.TextField()
    address = models.CharField(max_length=200)
    status = models.IntegerField(choices=status, default=1)
    brochure_url = models.URLField(max_length=200)
    project_plan = models.ForeignKey(ProjectPlan, on_delete=models.CASCADE)
    location = models.ForeignKey(Location, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class Amenitie(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()
    project = models.ForeignKey(Project, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class Info(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class ProjectInfo(models.Model):
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    info = models.ForeignKey(Info, on_delete=models.CASCADE)
    value = models.CharField(max_length=200)


class ProjectExtrasCard(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    project = models.ForeignKey(Project, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.title
