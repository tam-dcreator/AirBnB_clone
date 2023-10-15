# Project: 0x00. AirBnB clone - The console
The AirBnB clone project starts now. The project's goal is to deploy a simple copy of the AirBnB website on your server.
The project has been broken into several steps and for the first step, we would be working on the console.
## The Console
### Description
The Console is a command-line tool that allows users to interact with the AirBnB application through a text-based interface. It enables users to perform various actions, access features, and manage the application conveniently by entering specific commands.

### How to Start
To start the Command Interpreter, follow these steps:

1. Open your terminal or command prompt.

2. Clone the repository using the command `git clone https://github.com/PrudenceLive/AirBnB_clone.git`.

3. Navigate to the cloned directory  with `cd AirBnB_clone`.

4. Run the interpreter script using `python3 console.py`. A prompt `(hbnb) ` would show the console is ready to accept commands.

### How to Use
Once the Console runs, you can use it to interact with the application by entering commands. Here's a general overview of how to use it:

1. Launch the Console as instructed above.

2. You will see a command prompt indicating that the interpreter is ready to accept your commands.

3. Enter a command and press Enter. The interpreter will execute the corresponding action or provide feedback.

4. You can enter additional commands to interact further with the application.

#### Examples
Here are some examples of how to use the Console:

1. Create New Entry:
	`create BaseModel` or `create User` or `create State`.

2. List All Created Items:
	`all` or `all BaseModel` or `all User`.

3. Show an item:
	`show BaseModel 1234-1234-1234`.
Where 1234-1234-1234 represents the unique ID of the item created. This command displays a list of all items in the application.

4. Delete an Item:
	`destroy BaseModel 1234-1234-1234`.
This command deletes the item with the specified ID from the application.

5. Update an Items:
	`update BaseModel 1234-1234-1234 first_name "Tester"`.

6. Exit the Interpreter:
	`quit` or `ctrl + D`.
Use this command to exit the interpreter and return to the command prompt.

7. Access Help:
	`help` .
For specific help on a command, you can do help and command name. eg.
	`help update`

These are the available commands.

A list of items you can interact with are:
`[BaseModel, User, Place, State, City, Amenity, Review]`


## Resources

#### Read or watch:

* [cmd module](https://intranet.alxswe.com/rltoken/8ecCwE6veBmm3Nppw4hz5A)
* [cmd module in depth](https://intranet.alxswe.com/rltoken/uEy4RftSdKypoig9NFTvCg)
* [packages concept page]()
* [uuid module](https://intranet.alxswe.com/rltoken/KfL9TqwdI69W6ttG6gTPPQ)
* [datetime](https://intranet.alxswe.com/rltoken/1d8I3jSKgnYAtA1IZfEDpA)
* [unittest module](https://intranet.alxswe.com/rltoken/IlFiMB8UmqBG2CxA0AD3jA)
* [args/kwargs](https://intranet.alxswe.com/rltoken/C_a0EKbtvKdMcwIAuSIZng)
* [Python test cheatsheet](https://intranet.alxswe.com/rltoken/tgNVrKKzlWgS4dfl3mQklw)
* [cmd module wiki page](https://intranet.alxswe.com/rltoken/EvcaH9uTLlauxuw03WnkOQ)
* [python unittest](https://intranet.alxswe.com/rltoken/begh14KQA-3ov29KvD_HvA)
## Learning Objectives

### General

* How to create a Python package
* How to create a command interpreter in Python using the <code>cmd</code> module
* What is Unit testing and how to implement it in a large project
* How to serialize and deserialize a Class
* How to write and read a JSON file
* How to manage <code>datetime</code>
* What is an <code>UUID</code>
* What is <code>*args</code> and how to use it
* What is <code>**kwargs</code> and how to use it
* How to handle named arguments in a function
## Tasks

| Task | File |
| ---- | ---- |
| 0. README, AUTHORS | [SOON](./) |
| 1. Be pycodestyle compliant! | [SOON](./) |
| 2. Unittests | [SOON](./) |
| 3. BaseModel | [SOON](./) |
| 4. Create BaseModel from dictionary | [SOON](./) |
| 5. Store first object | [SOON](./) |
| 6. Console 0.0.1 | [SOON](./) |
| 7. Console 0.1 | [SOON](./) |
| 8. First User | [SOON](./) |
| 9. More classes! | [SOON](./) |
| 10. Console 1.0 | [SOON](./) |
