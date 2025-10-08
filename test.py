# test_tkinter.py
try:
    import tk
    print("tkinter is available")
except ImportError as e:
    print("tkinter is missing:", e)
