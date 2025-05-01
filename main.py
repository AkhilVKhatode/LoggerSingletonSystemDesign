class Logger:
    # 1. Private static variable to hold the single instance
    _instance = None

    # 2. Private constructor to prevent instantiation
    def __init__(self):
        if Logger._instance is not None:
            raise Exception("This class is a singleton!")
        else:
            Logger._instance = self

    # 3. Public method to provide access to the instance
    @staticmethod
    def get_instance():
        if Logger._instance is None:
            Logger()
        return Logger._instance

    def log(self, message):
        print(f"Log: {message}")

class Application:
    def run(self):
        # 4. Fetch the single instance of the Logger
        logger = Logger.get_instance()
        logger.log("Application started.")

# Running the application
app = Application()
app.run()
