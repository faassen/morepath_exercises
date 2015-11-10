class Galaxy(object):
    def __init__(self, name):
        self.name = name
        self.robots = {}

    def add(self, robot):
        self.robots[robot.name] = robot

    def get(self, name):
        return self.robots.get(name)


class Robot(object):
    def __init__(self, name):
        self.name = name


starwars = Galaxy('starwars')
starwars.add(Robot('c3po'))
starwars.add(Robot('r2d2'))

milkyway = Galaxy('milkyway')
milkyway.add(Robot('knight_rider'))
milkyway.add(Robot('data'))

galaxies = {
    'starwars': starwars,
    'milkyway': milkyway
}

def get_galaxy(robot):
    for galaxy in galaxies.values():
        if galaxy.get(robot.name) is not None:
            return galaxy
    return None
