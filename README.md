# Introduction 
This repository is primarily my Python dumping ground and exercise repository. The general purpose is to keep myself fairly refreshed in Python and to introduce other developers to Python using base exercises over various aspects of the language.

## refresher.py
This is by far the most raw dump of sample Python code in this project. A series of very base concepts as I began to re-introduce myself to Python.

The concepts covered here are as follows:

* Basic string building
* Creating an array and referencing items in the array
* Creating an array from a single string using split
* Importing a class from another file and creating an instance of that class and using the methods within that class
* Using Python dictionary
* Creating an array from a for statement
* Using a multi parameter method with an argument that allows for optional parameters

## usejson.py
Using Python's built in JSON parsing to read a JSON string and treat the result like an object.

## classinheritance Folder
This one is a little more loaded as I wanted to try a number of things regarding Python. The first one involves using classes that happen to be in a separate folder. The classes also involve a base class of "Pet" and child classes that act as Pets. Naturally, I wanted to test this all out and also introduce using Python unit testing as a means to familiarizing myself with unit testing in a Python environment.

## make-api-call.py
This is the first file in this repo that needs to use pip to install a separate library. I am using requests to make a call to an API endpoint. I prefer this library over urllib2 as it is a lot simpler and I see it used a lot more in the Python community. It is included in the requirements.txt file, so to install, the following command will need to be run;

```
pip install -r requirements.txt
```

or

```
pip install requests
```

I make a basic GET call and print the results