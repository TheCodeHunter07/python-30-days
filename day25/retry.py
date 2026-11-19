# ASSIGNMENT
# Stretch: A decorator that retries a failing function up to 3 times.

def retry(function):

    def wrapper(*args, **kwargs):

        attempts = 3

        for attempt in range(attempts):

            try:
                result = function(*args, **kwargs)
                return result

            except Exception as error:
                print(f"Attempt {attempt + 1} failed: {error}")

        print("Function failed after 3 attempts!")

    return wrapper


@retry
def connect_to_server():

    print("Connecting to server...")

    raise Exception("Connection failed!")


connect_to_server()