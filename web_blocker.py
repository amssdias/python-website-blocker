"""
Program to block websites
"""


user_is_working = input("Activate no distraction mode (y/n)?")

local_host = "127.0.0.1"
websites_to_block = ["www.facebook.com", "www.instagram.com"]

with open(r"C:\Windows\System32\drivers\etc\hosts", "r") as host_file:
    host_file_text = host_file.readlines()

with open(r"C:\Windows\System32\drivers\etc\hosts", "w") as host_file:

    if user_is_working == "n":

        for line in host_file_text:
            if line[:9] == "127.0.0.1":
                print(f"Unblocking website: {repr(line)}")
                continue

            host_file.write(line)

    else:

        host_file.writelines(host_file_text)

        for website in websites_to_block:
            host_file.write(f"{local_host} {website}\n")
