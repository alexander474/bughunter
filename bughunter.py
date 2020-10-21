__author__ = 'Alexander Bredesen'
__version__ = '1.0'

from subdomain import subdomain as subfinder
import sys


def main(root_domain, number_of_threads):
    subfinder.main(domain=domain, n_threads=n_threads)


def banner():
    print("""
                            BUGHUNTER
                # Coded By Alexander Bredesen
    """)


def parser_error(errmsg):
    banner()
    print("Usage: python3 " + sys.argv[0] + " [Options] use -h for help")
    print("Error: " + errmsg)
    sys.exit()


def parser_args():
    import argparse

    parser = argparse.ArgumentParser(description="Bughunter automation tool",
                                     epilog='\tExample: \r\npython3 ' + sys.argv[0] + " -d google.com")
    parser.error = parser_error
    parser._optionals.title = "OPTIONS"
    parser.add_argument("-d", "--domain", help="Domain to scan (Without protocol http / https)")
    parser.add_argument("-t", "--threads", help="Number of threads. Default is 10", default=10, type=int)
    return parser.parse_args()


if __name__ == "__main__":
    args = parser_args()

    domain = args.domain
    n_threads = args.threads
    banner()

    main(root_domain=domain, number_of_threads=n_threads)
