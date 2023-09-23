BaseException  # except: and except BaseException

BaseException < SystemExit

BaseException < KeyboardInterrupt

BaseException < Exception

Exception < AssertionError

Exception < ValueError

Exception < MemoryError  # con lack of free memory

Exception < StandardError < ImportError  # when importing failed

Exception < ArithmeticError < ZeroDivisionError

Exception < ArithmeticError < OverflowError  # con

Exception < LookupError  # abs invalid references of collections

LookupError < IndexError  # con

LookupError < KeyError  # con
