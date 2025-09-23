ip = input("Enter IP address: ")
ip_sep = ip.split(".")
if len(ip) < 15 or len(ip_sep) > 15:
    print("Isn't correct")
elif (int(ip_sep[0]) < 0 or int(ip_sep[0]) > 255) or (int(ip_sep[1]) < 0 or int(ip_sep[1]) > 255) or (int(ip_sep[2]) < 0 or int(ip_sep[2]) > 255) or (int(ip_sep[3]) < 0 or int(ip_sep[3]) > 255):
    print("Isn't correct")
else:
    print("Is correct")