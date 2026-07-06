import sys
import serial
from PyQt5 import QtWidgets, QtCore
import threading

FRAME_SIZE = 32  # 고정 32 bytes