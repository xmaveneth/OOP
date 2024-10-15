class PolyLine:
    def __init__(self, *args):
        self.coords = list(args)

    def add_coord(self, x, y):
        self.coords.append((x, y))

    def remove_coord(self, indx):
        if indx + 1 <= len(self.coords):
            self.coords.pop(indx)

    def get_coords(self):
        return self.coords