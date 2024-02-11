#!/usr/bin/python3
"""A console to manipulate the objects"""


import cmd
from models.base_model import BaseModel
from models import storage


class HBNBCommand(cmd.Cmd):
    """a cmd console class that inherits from cmd class"""

    prompt = '(hbnb) '

    def do_create(self, arg: str):
        """Create an instance of a class."""

        dic_of_class = {'BaseModel': BaseModel}

        if arg in dic_of_class:
            cls = dic_of_class[arg]
            obj = cls()
            obj.save()
            print(obj.id)
        elif not arg:
            print("** class name missing **")
        else:
            print("** class doesn't exist **")

    def do_show(self, args):
        """to show the instance info according to its calss name and id"""
        arg = args.split()
        if not args:
            print("** class name missing **")
            return
        class_name = arg[0]
        
        # Check if class name exists
        if class_name not in ['BaseModel']:  # Add other class names as needed
            print("** class doesn't exist **")
            return

        # Check if id is missing
        if len(arg) < 2:
            print("** instance id missing **")
            return

        instance_id = arg[1].replace("\"", "")

        # Check if instance exists
        instance_key = class_name + "." + instance_id
        if instance_key not in storage.all():  # Assuming storage.all() returns a dictionary of instances
            print("** no instance found **")
            return

        # Print the string representation of the instance
        print(storage.all()[instance_key])

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
