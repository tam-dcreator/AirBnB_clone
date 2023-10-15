#!/usr/bin/python3
""" A Module that implements a custom console for the AirBnB clone"""
import cmd
from models.base_model import BaseModel
from models import storage
from re import findall


class HBNBCommand(cmd.Cmd):
    """Custom Interpreter class that implements the commands for the AirBnB
    clone.
    """
    prompt = "(hbnb) "

    @staticmethod
    def split_string_with_quotes(line=""):
        """Use regular expression to split the string while preserving
        quoted words

        Args:
            line(str): Input string to turn into a list of commands
        Returns:
            list: List of commands
        """
        words = findall(r'"[^"]*"|\S+', line)
        # Remove the quotes from quoted words
        words = [word.strip('"') for word in words]
        return words

    def do_create(self, line):
        """ Creates a new instance of BaseModel and prints the id.
        Ex: create BaseModel
        """
        if line:
            # create a list of commands
            commands = type(self).split_string_with_quotes(line)

            if commands[0] == "BaseModel":
                instance = BaseModel()
                print(instance.id)
            else:
                print("** class doesn't exist **")
        else:
            print("** class name missing **")

    def do_show(self, line):
        """ Prints the string representation of an instance based on the class
        name and id.
        Ex: show BaseModel 1234-1234-1234
        """
        if line:
            # create a list of commands
            commands = type(self).split_string_with_quotes(line)

            if commands[0] == "BaseModel":
                if len(commands) > 1:
                    try:
                        instances = storage.all()
                        key = "{}.{}".format(commands[0], commands[1])
                        print(instances[key])
                    except KeyError:
                        print("** no instance found **")
                else:
                    print("** instance id missing ** ")
            else:
                print("** class doesn't exist **")
        else:
            print("** class name missing **")

    def do_destroy(self, line):
        """ Function that deletes an instance based on the class name and id
        Saves the changes in the file
        ex: destroy BaseModel 1234-1234-1234
        """
        if line:
            # create a list of commands
            commands = type(self).split_string_with_quotes(line)

            if commands[0] == "BaseModel":
                if len(commands) > 1:
                    try:
                        instances = storage.all()
                        key = "{}.{}".format(commands[0], commands[1])
                        del instances[key]
                    except KeyError:
                        print("** no instance found **")
                else:
                    print("** instance id missing ** ")
            else:
                print("** class doesn't exist **")
        else:
            print("** class name missing **")

    def do_all(self, line):
        """Prints all string representation of all instances based or not on
        the class name.
        Ex: all BaseModel or all
        """
        instances = storage.all()
        list_all = []
        if line:
            # create a list of commands
            commands = type(self).split_string_with_quotes(line)

            if commands[0] == "BaseModel":
                for key, value in instances.items():
                    if commands[0] in key:
                        list_all.append(str(value))
                print(list_all)
            else:
                print("** class doesn't exist **")
        else:
            for value in instances.values():
                list_all.append(str(value))
            print(list_all)

    def do_update(self, line):
        """Updates an instance based on the class name and id by adding or
        updating attributes
        Ex: update BaseModel 1234-1234-1234 email "aibnb@mail.com"
        """
        if line:
            # create a list of commands
            commands = type(self).split_string_with_quotes(line)

            if commands[0] == "BaseModel":
                if len(commands) > 1:
                    try:
                        instances = storage.all()
                        key = "{}.{}".format(commands[0], commands[1])
                        instance = instances[key]
                    except KeyError:
                        print("** no instance found **")
                    else:
                        # Check if the attribute is present in this instance
                        try:
                            attr_name = commands[2]
                            try:
                                attr_value = commands[3]
                                # Get the type of the existing attribute value
                                inst_type = type(getattr(instance, attr_name))
                                # Cast the attribute value to existing type
                                casted_value = inst_type(attr_value)
                            except IndexError:
                                print("** value missing **")
                            except AttributeError:
                                setattr(instance, attr_name, attr_value)
                            else:
                                # Set the attribute value
                                setattr(instance, attr_name, casted_value)
                        except IndexError:
                            print("** attribute name missing **")
                else:
                    print("** instance id missing ** ")
            else:
                print("** class doesn't exist **")
        else:
            print("** class name missing **")

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
