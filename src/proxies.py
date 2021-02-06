import os

proxies: set = {'92.186.181.242:80', '51.158.119.88:8761', '202.162.214.250:8080', '213.105.29.14:3128', '51.158.99.51:8811',
                '51.158.180.179:8811', '136.233.215.139:80', '136.233.215.142:80', '205.141.197.38:8080'}

# if use_proxy == True:
#     proxy = choice(proxies)
#     webdriver.DesiredCapabilities.CHROME['proxy'] = {
#         "httpProxy": proxy,
#         "ftpProxy": proxy,
#         "sslProxy": proxy,
#         "proxyType": "MANUAL"
#     }


def get_valid_proxies():
    valid_ips: set = set()
    for p in proxies:
        host, port = p.split(":")
        res = os.system(f"ping -c 1 {host} -p {port}")
        if res == 0:
            valid_ips.add(f"{host}:{port}")
    print("Invalid Ips:", proxies - valid_ips)
    return valid_ips
