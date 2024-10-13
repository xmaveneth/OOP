class SmartPhone:
    def __init__(self, model):
        self.model = model
        self.apps = []
        self.types = []

    def add_app(self, app):
        if type(app) not in self.types:
            self.apps.append(app)
            self.types.append(type(app))

    def remove_app(self, app):
        if app in self.apps:
            self.apps.remove(app)
            self.types.remove(type(app))

class AppVK:
    def __init__(self):
        self.name = "ВКонтакте"

class AppYouTube:
    def __init__(self, memory):
        self.name = "YouTube"
        self.memory = memory

class AppPhone:
    def __init__(self, phone_list):
        self.name = "Phone"
        self.phone_list = phone_list

sm = SmartPhone("Honor 1.0")
sm.add_app(AppVK())
sm.add_app(AppVK())  # второй раз добавляться не должно
sm.add_app(AppYouTube(2048))
for a in sm.apps:
    print(a.name)