from PyQt5.QAxContainer import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
import sys
import time
import pandas as pd

class Kiwoom(QAxWidget):
    def __init__(self):
        super().__init__()