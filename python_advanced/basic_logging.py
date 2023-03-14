import logging

def main():

    #use basic config to configure logging
    logging.basicConfig(filename="output.log",level=logging.DEBUG, filemode="w")


    logging.debug("this is a debug message")
    logging.info("THIS IS A info message")
    logging.warning("this is a warning message")
    logging.error("This is an error message")
    logging.critical("This is a critical message")
    
    #output formatted string 
    logging.info("Here is a {} variable and an int:".format("string", 10))




if __name__ == "__main__":
    main() 
