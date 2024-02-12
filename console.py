#!/usr/bin/python3
"""A console to manipulate the objects"""


import cmd
from models.base_model import BaseModel
from models import storage
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review


class HBNBCommand(cmd.Cmd):
    """a cmd console class that inherits from cmd class"""

    prompt = '(hbnb) '

    def do_create(self, arg: str):
        """Create an instance of a class."""

        dic_of_class = {
                        'BaseModel': BaseModel, 'User': User,
                        'State': State, 'City': City,
                        'Amenity': Amenity, 'Place': Place,
                        'Review': Review
                        }

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
        cls = arg[0]

        if cls not in [
                'BaseModel', 'User', 'Place',
                'State', 'City', 'Amenity',
                'Review'
                ]:
            print("** class doesn't exist **")
            return

        if len(arg) < 2:
            print("** instance id missing **")
            return

        ID = arg[1].replace("\"", "")

        instance_key = cls + "." + ID
        if instance_key not in storage.all():
            print("** no instance found **")
            return

        print(storage.all()[instance_key])

    def do_destroy(self, args):
        """to delete an object(instance)"""
        arg = args.split()
        if not args:
            print("** class name missing **")
            return
        cls = arg[0]

        if cls not in [
                'BaseModel', 'User', 'Place',
                'State', 'City', 'Amenity',
                'Review'
                ]:
            print("** class doesn't exist **")
            return

        if len(arg) < 2:
            print("** instance id missing **")
            return

        ID = arg[1].replace("\"", "")

        instance_key = cls + "." + ID
        if instance_key not in storage.all():
            print("** no instance found **")
            return
        storage.all().pop(instance_key)
        storage.save()

    def do_all(self, args):
        """to print instance in string format"""
        if args:
            if args not in ['BaseModel', 'User', 'Place',
                            'State', 'City', 'Amenity',
                            'Review']:
                print("** class doesn't exist **")
                return
            cls = eval(args + '()')
            print('[\"', end="")
            print(cls, end="")
            print('\"]')
        else:
            cls = eval(args + '()')
            print('[\"', end="")
            print(cls, end="")
            print('\"]')

    def do_update(self, args):
        """update the attributes with new ones"""
        arg = args.split()
        if not args:
            print("** class name missing **")
            return
        cls = arg[0]
        if cls not in [
                'BaseModel', 'User', 'Place',
                'State', 'City', 'Amenity',
                'Review'
                ]:
            print("** class doesn't exist **")
            return
        if len(arg) < 2:
            print("** instance id missing **")
            return
        ID = arg[1].replace("\"", "")
        instance_key = cls + "." + ID
        if instance_key not in storage.all():
            print("** no instance found **")
            return
        if len(arg) < 3:
            print("** attribute name missing **")
            return
        if len(arg) < 4:
            print("** value missing **")
            return

        attr = arg[2]
        val = arg[3]
        Upd_inst = storage.all()[instance_key]
        setattr(Upd_inst, attr, val)
        Upd_inst.save()

    def do_count(self, args):
        """to count the instances"""
        arg = args.split('.')
        cls = arg[0]
        if cls not in [
                'BaseModel', 'User', 'Place',
                'State', 'City', 'Amenity',
                'Review'
                ]:
            print("** class doesn't exist **")
            return
        c = 0
        for key, value in storage.all().items():
            c += 1
        print(c)

    def do_quit(self, arg: str):
        """Quit command to exit the program"""
        return True

    def do_EOF(self, arg):
        """EOF command to exit the program"""
        return True

    def do_help(self, arg: str):
        """to get help"""
        return super().do_help(arg)

    def emptyline(self):
        """empty line doesn't affect anything"""
        pass


if __name__ == '__main__':
    HBNBCommand().cmdloop()
