#!/usr/bin/python3
"""
Console module.
"""

import cmd
import shlex
from models import storage
from models.base_model import BaseModel

class Console(cmd.Cmd):
    prompt = "(hbnb) "

    def do_create(self, args):
        """Creates a new instance of BaseModel, saves it, and prints the id."""
        if not args:
            print("** class name missing **")
            return

        try:
            cls = eval(args)
        except NameError:
            print("** class doesn't exist **")
            return

        instance = cls()
        instance.save()
        print(instance.id)

    def do_show(self, args):
        """Prints the string representation of an instance."""
        if not args:
            print("** class name missing **")
            return

        args_list = shlex.split(args)
        try:
            cls = eval(args_list[0])
        except NameError:
            print("** class doesn't exist **")
            return

        if len(args_list) < 2:
            print("** instance id missing **")
            return

        key = "{}.{}".format(args_list[0], args_list[1])
        if key not in storage.all():
            print("** no instance found **")
        else:
            print(storage.all()[key])

    def do_destroy(self, args):
        """Deletes an instance based on the class name and id."""
        if not args:
            print("** class name missing **")
            return

        args_list = shlex.split(args)
        try:
            cls = eval(args_list[0])
        except NameError:
            print("** class doesn't exist **")
            return

        if len(args_list) < 2:
            print("** instance id missing **")
            return

        key = "{}.{}".format(args_list[0], args_list[1])
        if key not in storage.all():
            print("** no instance found **")
        else:
            del storage.all()[key]
            storage.save()

    def do_all(self, args):
        """Prints all string representation of all instances."""
        args_list = shlex.split(args)
        if not args or args_list[0] not in storage.classes():
            print("** class doesn't exist **")
            return

        instances = [str(obj) for obj in storage.all().values()
                     if type(obj).__name__ == args_list[0]]
        print(instances)

    def do_update(self, args):
        """Updates an instance based on the class name and id."""
        if not args:
            print("** class name missing **")
            return

        args_list = shlex.split(args)
        try:
            cls = eval(args_list[0])
        except NameError:
            print("** class doesn't exist **")
            return

        if len(args_list) < 2:
            print("** instance id missing **")
            return

        key = "{}.{}".format(args_list[0], args_list[1])
        if key not in storage.all():
            print("** no instance found **")
            return

        if len(args_list) < 4:
            print("** attribute name missing **")
            return

        if len(args_list) < 5:
            print("** value missing **")
            return

        instance = storage.all()[key]
        setattr(instance, args_list[3], eval(args_list[4]))
        instance.save()

if __name__ == '__main__':
    console = Console()
    console.cmdloop()

