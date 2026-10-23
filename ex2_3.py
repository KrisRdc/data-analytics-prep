   # 1. pitaj korisnika za sate rada i spremi u varijablu
   # 2. pitaj korisnika za cijenu sata i spremi u varijablu
   # 3. izračunaj bruto plaću i ispiši je

hours = float(input("Enter Hours: "))
rate = float(input("Enter Rate:"))
pay = hours * rate

print("Pay:",pay)