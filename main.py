import os
import sys
sys.path.append(os.path.abspath('../modules'))
from modules import speech
from modules import forward


def main():
    forward.a()
    speech.b()
                                                
if __name__ == '__main__':
    main()
