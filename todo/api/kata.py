from ipaddress import IPv4Address


def int32_to_ip(int32):
    return str(IPv4Address(int32))


print(int32_to_ip(21568901))
