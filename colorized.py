from color import Bcolors


class Colorizer:
    def __init__(self, color: str):
        self.colors = {
            'header': Bcolors.HEADER,
            'blue': Bcolors.OKBLUE,
            'green': Bcolors.OKGREEN,
            'yellow': Bcolors.WARNING,
            'red': Bcolors.FAIL,
            'bold': Bcolors.BOLD,
            'underline': Bcolors.UNDERLINE,
            'default': Bcolors.ENDC
        }
        self.color = color

    def __enter__(self):
        if self.color in self.colors:
            self.color = self.colors[self.color]
            print(self.color)

    def __exit__(self, color, value, traceback):
        print(self.colors['default'])


if __name__ == '__main__':
    colorizer = Colorizer('red')
    with colorizer:
        print('Eat some more of those soft French rolls and have some tea.')
    with colorizer:
        print('Eat some more of those soft French rolls and have some tea.')
