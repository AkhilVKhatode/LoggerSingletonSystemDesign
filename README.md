# Logger Singleton Pattern in Python

This repository contains the implementation of the **Logger** class following the **Singleton Design Pattern**. The Singleton pattern ensures that a class has only one instance and provides a global point of access to that instance.

## Project Overview

This project demonstrates how to implement a Singleton pattern in Python by creating a `Logger` class that logs messages. The `Logger` class ensures that only one instance of the logger is created, no matter how many times it is accessed.

### Example Usage

```python
# logger.py

class Logger:
    _instance = None

    def __init__(self):
        if Logger._instance is not None:
            raise Exception("This class is a singleton!")
        else:
            Logger._instance = self

    @staticmethod
    def get_instance():
        if Logger._instance is None:
            Logger()
        return Logger._instance

    def log(self, message):
        print(f"Log: {message}")

class Application:
    def run(self):
        logger = Logger.get_instance()
        logger.log("Application started.")

app = Application()
app.run()
```
Output:
```
Log: Application started.
```
### Explanation of Code
- Logger class: This class is a Singleton, meaning only one instance of it can exist. It uses the _instance class variable to store the single instance.
- get_instance(): This static method checks if the instance of the Logger exists. If it doesn't, it creates one.
- Application class: This class demonstrates the use of the Singleton Logger. When the run() method is called, it fetches the single Logger instance and logs a message.

### Why Use Singleton?
The Singleton pattern is useful when you want to ensure that only one instance of a class exists and provides a global point of access. In this case, it is ideal for logging because you want a single logger instance used throughout the application.



## Update: (Multi threading)
In multi threading approach the above code may generate multiple instances, as more than one instance may access getinstance at the same time, which may lead to creating more than one logger
Updated code
```python
import threading

class Logger:
    # 1. Private static variable to hold the single instance
    _instance = None
    _lock = threading.Lock()  # Lock for thread safety

    # 2. Private constructor to prevent instantiation
    def __init__(self):
        if Logger._instance is not None:
            raise Exception("This class is a singleton!")
        else:
            Logger._instance = self

    # 3. Public method to provide access to the instance with double-checked locking
    @staticmethod
    def get_instance():
        if Logger._instance is None:
            with Logger._lock:  # Synchronize only when creating the instance
                if Logger._instance is None:
                    Logger()  # Create the instance if it's still None
        return Logger._instance

    def log(self, message):
        print(f"Log: {message}")


# Example usage
logger = Logger.get_instance()
logger.log("Application started.")
```
