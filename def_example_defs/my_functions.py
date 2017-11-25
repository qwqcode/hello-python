import time


def hello_world():
    print('HelloWorld')


def hello_python():
    print('HelloPython')


def your_name(name='无名英雄'):
    print('Hello, ' + name)


def built_person(username, **user_info):
    user_profile = {
        'username': username,
    }

    for key, value in user_info.items():
        user_profile[key] = str(value).strip()

    return user_profile


def get_time():
    return time.time()
