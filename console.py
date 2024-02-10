#!/usr/bin/python3
"""A console to manipulate the objects"""


import cmd


class HBNBCommand(cmd.Cmd):
    """a cmd console class that inherits from cmd class"""

    prompt = '(hbnb) '

    def do_quit(self, arg: str):
        """Quit command to exit the program
        """
        return True

    def do_EOF(self, arg):
        """EOF command to exit the program
        """
        return True

    def do_help(self, arg: str):
        """to get help
        """
        return super().do_help(arg)

    def emptyline(self):
        """empty line doesn't affect anything
        """
        pass


if __name__ == '__main__':
    HBNBCommand().cmdloop()
