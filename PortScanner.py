import socket
from datetime import datetime

# Common ports I care about
COMMON_PORTS = {
    21: 'FTP',
    22: 'SSH', 
    23: 'Telnet',
    25: 'SMTP',
    53: 'DNS',
    80: 'HTTP',
    110: 'POP3',
    143: 'IMAP',
    443: 'HTTPS',
    445: 'SMB',
    3389: 'RDP',
    3306: 'MySQL',
    5432: 'PostgreSQL',
    135: 'MS-RPC',
    139: 'NetBIOS',
}

def get_banner(port, target_ip):
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(1)
        sock.connect((target_ip, port))
        
        banner = sock.recv(1024).decode('utf-8', errors='ignore').strip()
        sock.close()
        
        return banner
    except:
        return None

def identify_service(port):
    return COMMON_PORTS.get(port, 'Unknown')

def scan_ports(target_ip, ports):
    print(f"Scanning {target_ip}...")
    print(f"Started: {datetime.now()}")
    
    for port in ports:
        try:
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.settimeout(1)
            
            result = sock.connect_ex((target_ip, port))
        except:
            continue
        
        if result == 0:
            print(f"Port {port} - OPEN")
            service_name = identify_service(port)
            print(f"  Service: {service_name}")
            
            # Skip banner for these ports - they don't respond well
            if port in [135, 139]:
                print(f"  (No banner - {service_name} doesn't respond)")
            else:
                banner = get_banner(port, target_ip)
                if banner:
                    print(f"  Banner: {banner}")
                # else:
                #     print("  No banner")
        # else:
        #     print(f"Port {port} is CLOSED")
        
        sock.close()
    
    print(f"Done: {datetime.now()}")

def main():
    target_ip = input("IP to scan: ")
    
    choice = input("Scan common ports or custom range? (c/custom): ").strip().lower()

    if choice == 'c' or choice == 'common':
        ports_to_scan = list(COMMON_PORTS.keys()) 
    elif choice == 'custom':
        port_range = input("Port range (start,end): ")
        try:
            start_port, end_port = map(int, port_range.split(','))
            if start_port < 0 or end_port < 0:
                print("Ports can't be negative")
                return
            if start_port > end_port:
                print("Start port must be <= end port")
                return
            ports_to_scan = range(start_port, end_port + 1) 
        except ValueError:
            print("Invalid format. Use: start,end")
            return
    else:
        print("Invalid choice")
        return

    scan_ports(target_ip, ports_to_scan)

if __name__ == "__main__":
    main()
