import socket 
sites=["google.com","Facebook.com",
            "youtube.com","Instagram.com"]
for site in sites:
    try:
        ip=socket.gethostbyname(site)
        print(f"{site} is ONLINE | IP:{ip}")
    except:
        print(f"{site} is DOWN")
