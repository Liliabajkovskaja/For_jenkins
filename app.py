import os


if __name__ == '__main__':
    if os.getenv('MARKS', None):
        os.system(f"pytest test -m {os.getenv('MARKS')}")
    else:
        os.system(f"pytest test")
