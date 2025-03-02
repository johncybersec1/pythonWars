# Implement a function that receives two IPv4 addresses, and returns the number of addresses between them (including the first one, excluding the last one).

# All inputs will be valid IPv4 addresses in the form of strings. The last address will always be greater than the first one.

def ips_between(start, end):
    def ip_to_int(ip):
        parts = list(map(int, ip.split('.')))
        return sum(parts[i] * (256 ** (3 - i)) for i in range(4))

    return ip_to_int(end) - ip_to_int(start)