import os
from colorama import Fore, Style

print("Welcome to Ftp & LazyConfig Tools Hunter")
print("Silakan Pilih Menu:")
print(f"{Fore.RED}==================================={Style.RESET_ALL}")
print(f"{Fore.BLUE}1. Scan Cofnig & Ftp")
print(f"2. Split Ftp")
print(f"3. Cek Ftp{Style.RESET_ALL}")
print(f"{Fore.RED}==================================={Style.RESET_ALL}")
print(f"{Fore.GREEN}4. Clean Domain")
print(f"5. Sql Checker")
print(f"6. ExtractorDB")
print(f"7. Change Host To IP")
print(f"8. RemoteSql Checker")
print(f"9. ExtracDB For CpCrack")
print(f"10. Cpcrack From DB{Style.RESET_ALL}")
print(f"{Fore.RED}==================================={Style.RESET_ALL}")
print(f"{Fore.YELLOW}11. Domain To Ip")
print(f"12. Spliter Cred")
print(f"13. FileManger Scanner")
print(f"14. Twilio Checker")
print(f"15. Paypal Checker V1{Style.RESET_ALL}")
def screen_clear():
    os.system('cls')

data = {
    '1':'lazyconfig.py',
    '2':'ftpsplit.py',
    '3':'checkftp.py',
    '4':'clean.py',
    '5':'sqlcek.py',
    '6':'extracdb.py',
    '7':'hostip.py',
    '8':'remote.py',
    '9':'extraccp.py',
    '10':'cpcarck.py',
    '11':'domaintoip.py',
    '12':'splitcred.py',
    '13':'fmscanner.py',
    '14':'twcek.py',
    '15':'ppcek.py'
}

SCRIPT_DIR = "Script"

pilihan = input("Masukan Pilih dengan Angka 1, 2, atau 3: ")
if data.get(pilihan):
    full_path = os.path.join(SCRIPT_DIR, data.get(pilihan))
    os.system(f'python3 {full_path}')
else:
    print('ga ada ')
