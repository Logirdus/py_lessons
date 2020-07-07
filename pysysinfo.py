import subprocess
import os


def uname():
    uname = "uname"
    uname_arg = "-a"
    print(f"Gathering system information with command {uname}:\n")
    subprocess.call([uname, uname_arg])


def diskspace():
    diskspace = "df"
    diskspace_arg = "-h"
    print(f"Information about disk space with command {diskspace}:\n")
    subprocess.call([diskspace, diskspace_arg])


def ip():
    ip_st = "ip"
    ip_arg= "a"
    print(f"Network interfaces status with command {ip_st}:\n")
    subprocess.call([ip_st, ip_arg])


def main():
    uname()
    diskspace()
    ip()


if __name__ == "__main__":
    main()


os.listdir()

print()