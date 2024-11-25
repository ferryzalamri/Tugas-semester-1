# Mengenal String
# String = Kumpulan karakter


data = "ini adalah String" # 21 karakter
print(data)
print(type(data))


# 1. cara membuat string

"""
    1. dengan menggunakan single quote '...'
    2. dengan menggunakan double quote "..."
"""

data = 'menggunakan single quote'
print(data)


data = "menggunakan double quote"
print(data)


# 2. menggunakan tanda \

# membuat tanda ' menjadi string
print('mari sholat jum\'at')

print('c:\\user\\adam')

# tab 
print("ronaldo\t\tmessi")
print("MU\t\tJuara")

# backspace
print("MU\bJuara")

# newline
print(" baris pertama.\nbaris kedua.") # LF -> Line feed
print(" baris pertama.\r\nbaris kedua.") # CLRF -> Line feed carriage


# raw string
print(r'c:\user\adam')