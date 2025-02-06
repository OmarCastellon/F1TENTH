import sys
if sys.prefix == '/usr':
    sys.real_prefix = sys.prefix
    sys.prefix = sys.exec_prefix = '/home/anthomarlexchan/F1TENTH/install/f1tenth_stack'
