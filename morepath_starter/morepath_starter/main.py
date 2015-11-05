import morepath
from .app import App


def main():
    morepath.autosetup()
    morepath.run(App())
