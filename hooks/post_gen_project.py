import os


def remove_celery():
    os.remove(os.path.join("source", "{{cookiecutter.app_name}}", "celery.py"))


def main():
    if "{{ cookiecutter.use_celery }}".lower() == "n":
        remove_celery()


if __name__ == "__main__":
    main()
