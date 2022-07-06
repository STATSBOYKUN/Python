#belajar format string
angka = 200090809.80861
format_str = f"angka = {angka:+,.2f}"
print(format_str)

persentase = 0.09
format_persen = f"persentase = {persentase:.3%}"
print(format_persen)

#format lain
angka = 111
format_lain  = f"biner : {bin(angka)}"
print(format_lain)
format_lain = f"octal : {oct(angka)}"
print(format_lain)
format_lain = f"hex : {hex(angka)}"
print(format_lain)

#format multiline
format_lain  = f"""
biner : {bin(angka)}
octal : {oct(angka)}
hex   : {hex(angka)}"""
print(format_lain)