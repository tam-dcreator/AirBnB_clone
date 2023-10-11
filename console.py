#!/usr/bin/python3
""" A Module that implements a custom console for the AirBnB clone"""
import cmd


class HBNBCommand(cmd.Cmd):
    """Custom Interpreter class that implements the commands for the AirBnB
    clone.

    """
    prompt = "(hbnb) "

    def do_EOF(self, line):
        """Allows you exit the program in a clean way, using EOF char
        """
        return True

    def do_quit(self, line):
        """Quit command to exit the program
        """
        exit(0)

    def postloop(self):
        """Prints an empty line when the program ends, for a nicer format
        """
        print()


if __name__ == "__main__":
    HBNBCommand().cmdloop()
