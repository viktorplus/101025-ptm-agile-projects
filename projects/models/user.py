from django.contrib.auth.base_user import AbstractBaseUser
from django.contrib.auth.models import UserManager, PermissionsMixin
from django.db import models


class User(AbstractBaseUser, PermissionsMixin):
    class Role(models.TextChoices):
        CEO = "ceo", "CEO"
        CTO = "cto", "CTO"
        BACKEND = "backend", "Backend Developer"
        FRONTEND = "frontend", "Frontend Developer"
        QA = "qa", "QA Engineer"
        DEVOPS = "devops", "DevOps Engineer"
        ML = "ml", "Machine Learning Engineer"
        DS = "ds", "Data Scientist"
        DESIGN = "design", "Designer"
        PM = "pm", "Project Manager"
        HR = "hr", "Human Resources"
        FINANCE = "finance", "Finance"
        MARKETING = "marketing", "Marketing"
        SALES = "sales", "Sales"
        SUPPORT = "support", "Support"

    class Gender(models.TextChoices):
        male = "male", "Male"
        female = "female", "Female"
        other = "other", "Other"

    username = models.CharField(max_length=30, unique=True)
    email = models.EmailField(max_length=80, unique=True)
    first_name = models.CharField(max_length=30, null=True, blank=True)
    last_name = models.CharField(max_length=30, null=True, blank=True)
    phone = models.CharField(max_length=25, null=True, blank=True)
    birth_date = models.DateField(null=True, blank=True)
    role = models.CharField(max_length=15, choices=Role)
    gender = models.CharField(max_length=10, choices=Gender)
    age = models.PositiveSmallIntegerField(null=True, blank=True)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    date_joined = models.DateTimeField(
        auto_now_add=True
    )
    project = models.ForeignKey(
        'Project',
        on_delete=models.SET_NULL,
        related_name='employees',
        null=True,
        blank=True
    )
    deleted_at = models.DateTimeField(null=True, blank=True)

    objects = UserManager()

    USERNAME_FIELD = "username"
    REQUIRED_FIELDS = ["email", "role", "gender"]

    def __str__(self):
        return self.email

    class Meta:
        db_table = "users"
        verbose_name = "User"
        verbose_name_plural = "Users"
        ordering = ["-date_joined"]

