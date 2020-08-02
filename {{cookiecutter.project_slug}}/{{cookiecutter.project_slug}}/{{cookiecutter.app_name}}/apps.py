from django.apps import AppConfig


class {{ cookiecutter.app_name_uppercase }}Config(AppConfig):
    name = "{{ cookiecutter.project_slug }}.{{ cookiecutter.app_name }}"
