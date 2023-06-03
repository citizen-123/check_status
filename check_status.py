import requests
import argparse
import threading

def check_response(ip, working_ips):
    try:
        response = requests.get(f'http://{ip}', timeout=3)
        if response.status_code == 200:
            working_ips.append(ip)
    except requests.exceptions.RequestException:
        pass

def read_ips_from_file(file_name):
    with open(file_name, 'r') as file:
        return file.read().splitlines()

def write_ips_to_file(file_name, ips):
    with open(file_name, 'w') as file:
        file.write('\n'.join(ips))

def main():
    parser = argparse.ArgumentParser(description='Check the response code of all addresses in a text file.')
    parser.add_argument('-f', type=str, required=True, help='Input file name')
    parser.add_argument('-t', type=int, required=True, help='Number of threads')
    parser.add_argument('-o', type=str, default='working.txt', help='Output file name (default: working.txt)')
    args = parser.parse_args()

    ips = read_ips_from_file(args.f)
    working_ips = []
    
    total_ips = len(ips)
    threads = min(args.t, total_ips)

    for i in range(0, total_ips, threads):
        batch = ips[i:i+threads]
        thread_list = []
        for ip in batch:
            thread = threading.Thread(target=check_response, args=(ip, working_ips))
            thread.start()
            thread_list.append(thread)
        
        for thread in thread_list:
            thread.join()

        # Display progress
        progress = ((i + len(batch)) / total_ips) * 100
        print(f'Progress: {progress:.2f}%')
    
    write_ips_to_file(args.o, working_ips)

if __name__ == "__main__":
    main()
  
