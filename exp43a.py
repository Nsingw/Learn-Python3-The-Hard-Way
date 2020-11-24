from sys import exit
from random import randint
from textwrap import dedent
# defent 简单地从字符串的行首删除空白


class Scene(object):

    def enter(self):
        print("This scene is not yet configured.")
        print("Subclass it and implement enter().")
        exit(1)


class Engine(object):

    def __init__(self, scene_map):
        self.scene_map = scene_map

    def play(self):
        current_scene = self.scene_map.opening_scene()  # 预先计划好的
        last_scene = self.scene_map.next_scene('finished')

        while current_scene != last_scene:
            next_scene_name = current_scene.enter()
            current_scene = self.scene_map.next_scene(next_scene_name)

        # be sure to print out the last scene_map
        current_scene.enter()


class Death(Scene):

# 定义的是一个字典变量
    quips = [
        "You died.You kinda suck at this.",
        "Your Mom would be proud...if she were smarter.",
        "Such a luser.",
        "I have a small puppy that's better at this.",
        "You're worse than your Dad's jokes."
    ]

    def enter(self):
        print(Death.quips[randint(0, len(self.quips)-1)])
        exit(1)


class Central_Corridor(Scene):

    def enter(self):
        print(dedent("""
            The Gothons of Planet Percal #25 have invaded your ship And
            destroyed your entire crew.You are the last surviving
            member and your last mission is to get the neutron destruct
            bomb from the Weapons Armory,put it in the bridge, and
            blow the ship up after getting into an escape pod.

            You're running down the central corridor to the Weapon
            Armory when a Gothon jumps out, red scaly skin, dark grimy
            teeth, and evil clown costume flowing around his hate
            filled body. He's blocking the door to the Armory and about
            to pull a weapon to blast you.
        """))

        action = input("> ")

        if action == "shoot!":
            print(dedent("""
                Quick on the draw you yank out your blaster and fire
                it at the Gothon. His clown costume is flowing
                ......
                ......
                ......
                ......
            """))
            return 'death'
        elif action == "dodge!":
            print(dedent("""
                Like a world class boxer you dodge, weave, slip And
                slide right....
                ....
                ...
                ..
            """))
            return 'death!'
        elif action == "tell a joke":
            print(dedent("""
                lucky for you they made you learn Gothon insults in
                the academy. You tell the one Gothon joke you know.
                ......
                ......
                ......
            """))
            return 'laser_weapon_armory'
        else:
            print("DOES NOT COMPUTE!")
            return 'central_corridor'


class LaserWeaponArmory(Scene):

    def enter(self):
        print(dedent("""
            You do dive roll into the Weapon Armory, crouch and scan
            the room for more Gothons that might be hiding.
            ......
            ......
            ......
        """))

        code = f"{randint(1, 9)}{randint(1, 9)}{randint(1, 9)}"
        guess = input("[keypad]> ")
        guesses = 0

        while guess != code and guesses < 10:
            print("BZZZEDDD")
            guesses += 1
            guess = input("[keypad]> ")
            if guess == "2":
                return 'central_corridor'

        if guess == code:
            print(dedent("""
                The container clicks open and seal breaks, letting
                gas out. You grab the neutron bomb and run as fast as
                ......
                ......
                ......
            """))
            return 'the_bridge'
        else:
            print(dedent("""
                The lock buzzes one last time and then you hear a
                sickening melting sound as the mechanism is fused
                ......
                ......
            """))
            return 'death'


class TheBrige(Scene):

    def enter(self):
        print(dedent("""
            You burst onto the Bridge with the neutron destruct bomb
            under your arm and surprise 5 Gothons who are trying to
            .....
            ......
            .......
        """))

        action = input("> ")

        if action == "throw the bomb":
            print(dedent("""
                In a panic you throw the bomb at the group of Gothons
                and make a leap for the door.Ritht as you drop it a
                ......
                ......
                .....
            """))
            return 'death'

        elif action == "slowly place the bomb":
            print(dedent("""
                You point your blaster at the bomb under your arm And
                the Gothons put their hands up and start to sweat.
                ......
                ......
                ......
            """))

            return 'escape_pod'
        else:
            print("DOES NOT CPMPUTE!")
            return "the_bridge"


class EscapePod(Scene):

    def enter(self):
        print(dedent("""
            You rush through the ship....
            ....
            There's 5 pod,which one do you take?
        """))

        good_pod = randint(1, 5)
        guess = input("[pod #]> ")

        if int(guess) != good_pod:
            print(dedent("""
                You jump into pod {guess} and hit the eject button.
                The pod ....
                .....
                .....
                .....
            """))
            return 'death'
        else:
            print(dedent("""
                You jump into pod {guess} and hit the eject button.
                The pod .....
                ......
                ......
            """))
            return 'finished'


class Finished(Scene):

    def enter(self):
        print("You won! Good job.")
        return 'finished'


class Map(object):

    scenes = {
        'central_corridor': Central_Corridor(),
        'laser_weapon_armory': LaserWeaponArmory(),
        'the_bridge': TheBrige(),
        'escape_pod': EscapePod(),
        'death': Death(),
        'finished': Finished(),
    }

    def __init__(self, start_scene):
        self.start_scene = start_scene

    def next_scene(self, scene_name):
        val = Map.scenes.get(scene_name)
        return val

    def opening_scene(self):
        return self.next_scene(self.start_scene)


a_map = Map('central_corridor')  # 初始化场景
a_game = Engine(a_map)  # 引擎启动
a_game.play()
