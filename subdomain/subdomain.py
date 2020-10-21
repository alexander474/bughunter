import requests
from threading import Thread
from queue import Queue

q = Queue()


def scan_subdomains(domain):
    global q
    while True:
        subdomain = q.get()
        url = f"http://{subdomain}.{domain}"
        try:
            requests.get(url)
        except requests.ConnectionError:
            pass
        else:
            print("[+] Discovered subdomain: ", url)

        q.task_done()


def main(domain, n_threads=10, subdomains=None):
    if subdomains is None:
        subdomains = open("./subdomain/subdomains.txt").read().splitlines()

    global q

    for subdomain in subdomains:
        q.put(subdomain)

    for thread in range(n_threads):
        worker = Thread(target=scan_subdomains, args=(domain,))
        worker.daemon = True
        worker.start()
    q.join()


if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser(description="Multithreading subdomain scanner")
    parser.add_argument("-d", "--domain", help="Domain to scan (Without protocol http / https)")
    parser.add_argument("-l", "--wordlist", help="Subdomains to scan. Default is subdomains.txt",
                        default="subdomains.txt")
    parser.add_argument("-t", "--threads", help="Number of threads. Default is 10", default=10, type=int)

    args = parser.parse_args()
    domain = args.domain
    wordlist = args.wordlist
    n_threads = args.threads

    main(domain=domain, n_threads=n_threads, subdomains=open(wordlist).read().splitlines())