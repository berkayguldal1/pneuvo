from colorama import Fore, Style, init
import platform
import os
import getpass
from datetime import datetime
import time
import argparse

def main():
    parser = argparse.ArgumentParser(description="Bu bir örnek Python betiğidir.")
main()

def get_terminal_size():
    try:
        columns, rows = os.get_terminal_size()
    except OSError:
        columns, rows = 80, 24  # Varsayılan değerler
    return columns, rows

def display_logo():
    logo = f"""
{Fore.BLUE}{Style.BRIGHT}     ██████████  ██████████ 
{Fore.BLUE}{Style.BRIGHT}     ██████████  ██████████ 
{Fore.BLUE}{Style.BRIGHT}     ██████████  ██████████ 
{Fore.BLUE}{Style.BRIGHT}     ██████████  ██████████ 
{Fore.BLUE}{Style.BRIGHT}                            
{Fore.BLUE}{Style.BRIGHT}     ██████████  ██████████ 
{Fore.BLUE}{Style.BRIGHT}     ██████████  ██████████ 
{Fore.BLUE}{Style.BRIGHT}     ██████████  ██████████ 
{Fore.BLUE}{Style.BRIGHT}     ██████████  ██████████  {" ".join(f"{color}███{Style.RESET_ALL}" for color in [Fore.RED, Fore.GREEN, Fore.BLUE, Fore.YELLOW, Fore.MAGENTA, Fore.CYAN, Fore.WHITE])}{Style.RESET_ALL}
    """
    return logo

def display_info():
    init(autoreset=True)

    username = getpass.getuser()
    hostname = platform.node()
    os_name = platform.system()
    os_version = platform.version()
    os_release = platform.release()
    architecture = platform.architecture()[0]
    processor = platform.processor()
    terminal_size = get_terminal_size()

    logo = display_logo()

    info = f"""
{Fore.MAGENTA}{Style.BRIGHT}{username}@{hostname}
{Fore.YELLOW}{'-' * (len(username) + len(hostname) + 1)}
{Fore.CYAN}OS: {Fore.WHITE}{os_name} {os_release}
{Fore.CYAN}Version: {Fore.WHITE}{os_version}
{Fore.CYAN}Architecture: {Fore.WHITE}{architecture}
{Fore.CYAN}CPU: {Fore.WHITE}{processor}
{Fore.CYAN}Terminal Size: {Fore.WHITE}{terminal_size[0]}x{terminal_size[1]}
    """

    # Print logo and info side by side
    logo_lines = logo.splitlines()
    info_lines = info.splitlines()
    max_lines = max(len(logo_lines), len(info_lines))

    for i in range(max_lines):
        logo_part = logo_lines[i] if i < len(logo_lines) else ""
        info_part = info_lines[i] if i < len(info_lines) else ""
        print(f"{logo_part:<20} {info_part}")

    print(Style.RESET_ALL)

display_info()