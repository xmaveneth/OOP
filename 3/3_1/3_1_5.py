class Course:
    def __init__(self, name):
        self.name = name
        self.modules = []

    def add_module(self, module):
        self.modules.append(module)

    def remove_module(self, indx):
        self.modules.pop(indx)

class Module:
    def __init__(self, name):
        self.name = name
        self.lessons = []

    def add_lesson(self, lesson):
        self.lessons.append(lesson)

    def remove_lesson(self, indx):
        self.lessons.pop(indx)


class LessonItem:
    attrs = {'title': (str, ), 'practices': (int, ), 'duration': (int, )}

    def __init__(self, title, practices, duration):
        self.title = title
        self.practices = practices
        self.duration = duration

    def __setattr__(self, key, value):
        if key in self.attrs and type(value) in self.attrs[key]:
            if key in ('practices', 'duration') and value <= 0:
                raise TypeError("Неверный тип присваиваемых данных.")
        elif key in self.attrs:
            raise TypeError("Неверный тип присваиваемых данных.")

        object.__setattr__(self, key, value)

    def __getattr__(self, item):
        return False

    def __delattr__(self, item):
        if item in self.attrs:
            return None
        else:
            object.__delattr__(self, item)