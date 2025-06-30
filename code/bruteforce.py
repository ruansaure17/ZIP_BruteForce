from zipfile import ZipFile

def main():
    print("[+] Beginning bruteforce ")
    with ZipFile('enc.zip') as zf:
        with open('rockyou.txt', 'rb') as f:
            for passwords in f:
                passwords = passwords.strip()
                try:
                    zf.extractall(pwd=passwords)
                    print(f"[+] Password Found: {passwords.decode()}")
                except Exception:
                    continue
            

if __name__ == "__main__":
    main()
