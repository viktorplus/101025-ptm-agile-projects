from rest_framework import serializers

from projects.models import Task, Project, Tag
from django.utils import timezone


class TaskDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = '__all__'


class TaskUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = (
            'name',
            'description',
            'status',
            'priority',
            'project',
            'created_at',
            'due_date',
            'tags',
            'assignee',
            'created_by',
        )


'''В приложении tasks, в модуле serializers создайте новый файл tasks_serializers.py.
Реализуйте сериализатор AllTasksSerializer для отображения краткой информации о задачах. 
Поля для отображения:
name
status
priority
project (название проекта)
assignee (email сотрудника)
due_date
'''

class AllTasksSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = ['name', 'status', 'priority', 'project', 'assignee' , 'due_date']

'''Реализуйте сериализатор CreateTaskSerializer для создания новой задачи. Поля для создания 
новой задачи:
name
description
priority
project(заполняется не по id, а по имени проекта)
tags
due_date'''

'''Добавьте в сериализатор на создание новой задачи валидаторы  полей:
name (минимальная длина)
description (минимальная длина)
priority (передаётся строго число, переданное число должно быть в доступных choices, от 1 до 5)

project (передаётся имя проекта, поиск среди всех проектов. Если такого имени нет - 
выводить сообщение об ошибке, что проекта не существует)

tags (список имён тегов, поиск среди всех тегов. Если тега по имени найдено не было - 
выводить сообщение об ошибке)

deadline (не может быть в прошлом)'''

class CreateTaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = ['name', 'description', 'priority', 'project', 'tags', 'due_date']

    def validate_name(self, value: str):
        if len(value) < 10:
            raise serializers.ValidationError(f'Название задачи должно быть минимум 10 символов')
        return value

    def validate_description(self, value: str):
        if len(value) < 25:
            raise serializers.ValidationError(f'Описание задачи минимум 25 символов')
        return value

    def validate_priority(self, value: str):

        if value not in [choice[0] for choice in Task.Priority.choices]:
            raise serializers.ValidationError(f"Приоритет не верный, доступные варианты от 1 до 4")

        return value

    def validate_project(self, value: str):
        # try:
        #     Project.objects.get(name=value)
        # except Project.DoesNotExist:
        #     raise serializers.ValidationError(f"Проект с именем {value} не существует")

        if not Project.objects.filter(name=value).exists():
            raise serializers.ValidationError(f"Проект с именем {value} не существует")

        return value

    '''tags (список имён тегов, поиск среди всех тегов. Если тега по имени найдено не было - 
    выводить сообщение об ошибке)'''

    def validate_tags(self, values: list[str]):
        # try:
        #     for tag_name in values:
        #         Tag.objects.get(title=tag_name)
        # except Tag.DoesNotExist:
        #     raise serializers.ValidationError(f"Тег {tag_name} не найден")

        if not Tag.objects.filter(title__in=values).exists():
            raise serializers.ValidationError(f"Тег не найден")
        return values


    '''deadline (не может быть в прошлом)'''

    def validate_due_date(self, value: str):
        # due_date = timezone.make_aware(value, timezone.get_current_timezone())
        # if due_date < timezone.now():
        #     raise serializers.ValidationError("Дедлайн не может быть в прошлом")

        if value < timezone.now():
            raise serializers.ValidationError("Дедлайн не может быть в прошлом")
        return value


'''
Переопределите метод create для добавления информации тегов в промежуточную таблицу.
Напишите класс-отображение AllTasksListAPIView для получения списка всех задач, привязанных к конкретному проекту, или сотруднику на выбор. Реализуйте пагинацию для отображения только первых пяти записей на одной странице. Добавьте метод post для создания задачи.
Зарегистрируйте новый эндпоинт, проверьте как отрабатывают запросы GET, POST.
Зафиксируйте все изменения, сделайте запрос на слияние.'''