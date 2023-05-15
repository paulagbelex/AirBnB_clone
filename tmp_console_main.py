#!/usr/bin/python3
"""
Contains a class for entry to command interpreter
"""

import cmd
from models.base_model import BaseModel
from models import storage


class HBNBCommand(cmd.Cmd):
    """
    Class that is the entry point
    of command interpreter
    """
    prompt = '(hbnb) '

    def do_create(self, line):
        """
        Create command to creates a new instance of BaseModel,
        saves it (to the JSON file) and prints the id
        """
        if len(line) == 0:
            print("** class name missing **")
        else:
            if line[0] >= "0" and line[0] <= "9":
                x = False
                print("** class doesn't exist **")
            else:
                try:
                    class_name = eval(line)
                    x = True
                except NameError:
                    x = False
                    print("** class doesn't exist **")
                if x is True:
                    my_model = BaseModel()
                    my_model.save()
                    print(my_model.id)

    def do_show(self, line):
        """
        Show command to prints the string representation of
        an instance based on the class name and id
        """
        if len(line) == 0:
            print("** class name missing **")
        else:
            if line[0] >= "0" and line[0] <= "9":
                x = False
                print("** class doesn't exist **")
            else:
                two_words = False
                for a in line:
                    if a == " ":
                        two_words = True
                        break
                if two_words is True:
                    first, second = line.split(" ")
                    try:
                        class_name = eval(first)
                        x = True
                    except NameError:
                        x = False
                        print("** class doesn't exist **")
                    if x is True:
                        obj = storage.all()
                        val = []
                        for key, value in obj.items():
                            cls_name, ident = key.split(".")
                            val.append(ident)
                        i = 0
                        for key, value in obj.items():
                            if second == val[i]:
                                print(value)
                                break
                            i = i + 1
                        if i == len(val):
                            print("** no instance found **")
                else:
                    try:
                        class_name = eval(line)
                        x = True
                    except NameError:
                        x = False
                        print("** class doesn't exist **")
                    if x is True:
                        print("** instance id missing **")

    def do_destroy(self, line):
        """
        Destroy command to delete an instance based on
        the class name and id (save the change into the
        JSON file)
        """
        if len(line) == 0:
            print("** class name missing **")
        else:
            if line[0] >= "0" and line[0] <= "9":
                x = False
                print("** class doesn't exist **")
            else:
                two_words = False
                for a in line:
                    if a == " ":
                        two_words = True
                        break
                if two_words is True:
                    first, second = line.split(" ")
                    try:
                        class_name = eval(first)
                        x = True
                    except NameError:
                        x = False
                        print("** class doesn't exist **")
                    if x is True:
                        obj = storage.all()
                        val = []
                        for key, value in obj.items():
                            cls_name, ident = key.split(".")
                            val.append(ident)
                        i = 0
                        for key, value in obj.items():
                            if second == val[i]:
                                del obj[key]
                                storage.save()
                                break
                            i = i + 1
                        if i == len(val):
                            print("** no instance found **")
                else:
                    try:
                        class_name = eval(line)
                        x = True
                    except NameError:
                        x = False
                        print("** class doesn't exist **")
                    if x is True:
                        print("** instance id missing **")

    def do_all(self, line):
        """
        All command to print all string representation of
        all instances based or not on the class name
        """
        if len(line) == 0:
            obj = storage.all()
            val = []
            for key, value in obj.items():
                val.append(str(value))
            print(val)
        else:
            if line[0] >= "0" and line[0] <= "9":
                x = False
                print("** class doesn't exist **")
            else:
                try:
                    class_name = eval(line)
                    x = True
                except NameError:
                    x = False
                    print("** class doesn't exist **")
                if x is True:
                    obj = storage.all()
                    val = []
                    for key, value in obj.items():
                        val.append(str(value))
                    print(val)

    def do_update(self, line):
        """
        Update command to update an instance based on the
        class name and id by adding or updating attribute
        (save the change into the JSON file)
        """
        if len(line) == 0:
            print("** class name missing **")
        else:
            if line[0] >= "0" and line[0] <= "9":
                x = False
                print("** class doesn't exist **")
            else:
                two_words = False
                for a in line:
                    if a == " ":
                        two_words = True
                        break
                if two_words is True:
                    first = ""
                    second = ""
                    third = ""
                    fourth = ""
                    a = 0
                    for i in range(0, len(line)):
                        if line[i] == " ":
                            a = i + 1
                            break
                        first = first + line[i]
                    for i in range(a, len(line)):
                        if line[i] == " ":
                            a = i + 1
                            break
                        second = second + line[i]
                    j = len(line) - 1
                    three_words = True
                    if i == j:
                        three_words = False
                    try:
                        class_name = eval(first)
                        x = True
                    except NameError:
                        x = False
                        print("** class doesn't exist **")
                    if x is True:
                        if three_words is True:
                            for i in range(a, len(line)):
                                if line[i] == " ":
                                    a = i + 1
                                    break
                                third = third + line[i]
                            four_words = True
                            if i == j:
                                four_words = False
                            if four_words is True:
                                strtyp = False
                                for i in range(a, len(line)):
                                    """
                                    if line[i] == '"':
                                        i = i + 1
                                        for i in range(i, len(line)):
                                            if line[i] == '"':
                                                break
                                            else:
                                                fourth = fourth + line[i]
                                        break
                                    """
                                    if line[i] == " ":
                                        a = i + 1
                                        break
                                    fourth = fourth + line[i]
                                obj = storage.all()
                                val = []
                                if strtyp is False:
                                    print(fourth)
                                    fourth = eval(fourth)
                                    print(fourth)
                                    print(type(fourth))
                                for key, value in obj.items():
                                    cls_name, ident = key.split(".")
                                    val.append(ident)
                                i = 0
                                for key, value in obj.items():
                                    if third == "id" or third == "created_at":
                                        break
                                    if third == "updated_at":
                                        break
                                    if second == val[i]:
                                        setattr(value, third, fourth)
                                        value.save()
                                        break
                                    i = i + 1
                                if i == len(val):
                                    print("** no instance found **")
                            else:
                                obj = storage.all()
                                val = []
                                for key, value in obj.items():
                                    cls_name, ident = key.split(".")
                                    val.append(ident)
                                i = 0
                                for key, value in obj.items():
                                    if second == val[i]:
                                        print("** value missing **")
                                        break
                                    i = i + 1
                                if i == len(val):
                                    print("** no instance found **")
                        else:
                            obj = storage.all()
                            val = []
                            for key, value in obj.items():
                                cls_name, ident = key.split(".")
                                val.append(ident)
                            i = 0
                            for key, value in obj.items():
                                if second == val[i]:
                                    print("** attribute name missing **")
                                    break
                                i = i + 1
                            if i == len(val):
                                print("** no instance found **")
                else:
                    try:
                        class_name = eval(line)
                        x = True
                    except NameError:
                        x = False
                        print("** class doesn't exist **")
                    if x is True:
                        print("** instance id missing **")

    def do_quit(self, line):
        """Quit command to exit the program"""
        exit()

    def do_EOF(self, line):
        """EOF command to exit the program"""
        exit()

    def emptyline(line):
        """
        Empty line + ENTER shouldn’t execute anything
        """
        return


if __name__ == '__main__':
    HBNBCommand().cmdloop()
