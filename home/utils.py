from home.models import *
import time

def run_this_function():
    print("This is a function from utils.py")
    print("This function is called at", time.ctime())
    print("This function is called at", time.time())
    print("This function is called at", time.localtime())