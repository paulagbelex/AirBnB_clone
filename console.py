#!/usr/bin/python3
import cmd
class HBNBCommand(cmd.Cmd):
        prompt = '(hbnb) '
        def do_quit(self, line):
            """Quit command exits the program"""
            return True
        do_EOF = do_quit

        def emptyline(self):
            pass

        def do_create(self, BaseModel):
            pass

        def do_show(self, BaseModel):
            pass

        def do_destroy(self, BaseModel):
            pass

        def do_all(self, BaseModel):
            pass

        def do_update(self, BaseModel):
            pass

if __name__ == '__main__':
    HBNBCommand().cmdloop()
