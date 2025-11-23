import logging

logging.basicConfig(level=logging.DEBUG)

def divide(a,b):
    try:
        logging.debug(f" Starting division with a={a:g}, b={b:g}")
        result = a / b
        logging.info(f"Result = {result}")
        print(f"Division successful: {result}")
        return result
    except ZeroDivisionError:
        logging.error("ERROR: Cannot divide by zero.")
        print("Division failed.")
        return None