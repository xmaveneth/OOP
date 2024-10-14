class RenderList:
    def __init__(self, type_list):
        self.type_list = type_list
        if type_list not in ('ul', 'ol'):
            self.type_list = 'ul'


    def __call__(self, *args, **kwargs):
        return '\n'.join([f'<{self.type_list}>'] + [f'<li>{el}</li>' for el in args[0]] + [f'</{self.type_list}>'])



lst = ["Пункт меню 1", "Пункт меню 2", "Пункт меню 3"]
render = RenderList("ol")
html = render(lst)
print(html)