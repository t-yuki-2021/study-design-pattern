from abc import ABCMeta, abstractmethod

class UserInfo:
    def __init__(self, user_name, job_name, nationality):
        self.user_name = user_name
        self.job_name = job_name
        self.nationality = nationality

    def __str__(self):
        return '{} {} {}'.format(
            self.user_name, self.job_name, self.nationality
        )

class Comparation(metaclass=ABCMeta):

    @abstractmethod
    def is_equal(self, other):
        pass

class Filter(metaclass=ABCMeta):
    
    @abstractmethod
    def filter(self, comparation, items):
        pass


class JobNameComparation(Comparation):

    def __init__(self, job_name):
        self.job_name = job_name

    def is_equal(self, other):
        return self.job_name == other.job_name


class NationalityComparation(Comparation):

    def __init__(self, nationality):
        self.nationality = nationality

    def is_equal(self, other):
        return self.nationality == other.nationality


class UserInfoFilter(Filter):

    def filter(self, comparation, items):
        for item in items:
            if comparation.is_equal(item):
                yield item

""" class UserInfoFilter:

    @staticmethod
    def filter_users_job(users, job_name):
        for user in users:
            if user.job_name == job_name:
                yield user

    @staticmethod
    def filter_users_nationality(users, nationality):
        for user in users:
            if user.nationality == nationality:
                yield user """

taro = UserInfo('taro', 'salary man', 'Japan')
jiro = UserInfo('jiro', 'police man', 'Japan')
john = UserInfo('john', 'salary man', 'USA')

user_list = [taro, jiro, john]
salary_man = JobNameComparation('salary man')
user_info_filter = UserInfoFilter()
for user in user_info_filter.filter(salary_man, user_list):
    print(user)
""" for man in UserInfoFilter.filter_users_job(user_list, 'police man'):
    print(man)

for man in UserInfoFilter.filter_users_nationality(user_list, 'Japan'):
    print(man) """