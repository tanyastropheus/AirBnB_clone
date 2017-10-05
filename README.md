<p align="center">

  <img src="HBTN-hbnb-Final.png" width="400\"/>

<br>


<h1><p align="center">The Holberton B&B</h1></p></font>


# AirBnB clone project! (The Holberton B&B)

First step: Write a command interpreter to manage your AirBnB objects.

This is the first step towards building your first full web application: the AirBnB clone. This first step is very important because you will use what you build during this project with all other following projects: HTML/CSS templating, database storage, API, front-end integration...

Each tasks are linked and will help you to: - put in place a parent class (called BaseModel) to take care of the initialization, serialization and deserialization of your future instances - create a simple flow of serialization/deserialization: Instance <-> Dictionary <-> JSON string <-> file - create all classes used for AirBnB (User, State, City, Place...) that inherit from BaseModel - create the first abstracted storage engine of the project: File storage. - create all unittests to validate all our classes and storage engine


## Syntax
The AirBnB works by the following commands:
* To start the console for our project you need to type in `./console`.
* The console take in the following commands and format on how to use them:
  * `create` : create <Class Name>
  * `show` : show <Class Name> <id>
  * `destroy`: destroy <Class Name> <id>  
  * `all` : all or all <Class Name>
  * `update` : update <Class Name> <id> <attribute name> <attribute value>

## Example
   (hbnb) all MyModel
** class doesn't exist **
(hbnb) show BaseModel
** instance id missing **
(hbnb) show BaseModel Holberton
** no instance found **
(hbnb) create BaseModel
49faff9a-6318-451f-87b6-910505c55907
(hbnb) all BaseModel
[[BaseModel] (49faff9a-6318-451f-87b6-910505c55907) {'created_at': datetime.datetime(2017, 10, 2, 3, 10, 25, 903293), 'id': '49faff9a-6318-451f-87b6-910505c55907', 'updated_at': datetime.datetime(2017, 10, 2, 3, 10, 25, 903300)}]
(hbnb) show BaseModel 49faff9a-6318-451f-87b6-910505c55907
[BaseModel] (49faff9a-6318-451f-87b6-910505c55907) {'created_at': datetime.datetime(2017, 10, 2, 3, 10, 25, 903293), 'id': '49faff9a-6318-451f-87b6-910505c55907', 'updated_at': datetime.datetime(2017, 10, 2, 3, 10, 25, 903300)}
(hbnb) destroy
** class name missing **
(hbnb) update BaseModel 49faff9a-6318-451f-87b6-910505c55907 first_name "Betty"
(hbnb) show BaseModel 49faff9a-6318-451f-87b6-910505c55907
[BaseModel] (49faff9a-6318-451f-87b6-910505c55907) {'first_name': 'Betty', 'id': '49faff9a-6318-451f-87b6-910505c55907', 'created_at': datetime.datetime(2017, 10, 2, 3, 10, 25, 903293), 'updated_at': datetime.datetime(2017, 10, 2, 3, 11, 3, 49401)}
(hbnb) create BaseModel
2dd6ef5c-467c-4f82-9521-a772ea7d84e9
(hbnb) all BaseModel
[[BaseModel] (2dd6ef5c-467c-4f82-9521-a772ea7d84e9) {'id': '2dd6ef5c-467c-4f82-9521-a772ea7d84e9', 'created_at': datetime.datetime(2017, 10, 2, 3, 11, 23, 639717), 'updated_at': datetime.datetime(2017, 10, 2, 3, 11, 23, 639724)}, [BaseModel] (49faff9a-6318-451f-87b6-910505c55907) {'first_name': 'Betty', 'id': '49faff9a-6318-451f-87b6-910505c55907', 'created_at': datetime.datetime(2017, 10, 2, 3, 10, 25, 903293), 'updated_at': datetime.datetime(2017, 10, 2, 3, 11, 3, 49401)}]
(hbnb) destroy BaseModel 49faff9a-6318-451f-87b6-910505c55907
(hbnb) show BaseModel 49faff9a-6318-451f-87b6-910505c55907
** no instance found **

### Exiting commands
To exit out of a command or process the user can use `quit`, `exit` stops a process and causes it to abort.
The user can also utilize the command `ctrl D` which will just exit. 

### Authors
* Wendy Segura - https://github.com/wendysegura
* Tanya Kryukova - https://github.com/tanyastropheus
