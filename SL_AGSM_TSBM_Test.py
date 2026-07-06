import sys
import serial
from PyQt5 import QtWidgets, QtCore
import threading

NEW_FRAME_SIZE = 32  # 고정 32 bytes
NEW_FRAME_SIZE_EXTEND = 64