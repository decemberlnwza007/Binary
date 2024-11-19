data = [
    "Hello World"
]

for index, line in enumerate(data, start=1):
    byte_data = line.encode('utf-8')
    binary_raw = ' ' . join(format(byte, '08b') for byte in byte_data)
    print(f"ข้อความที่ {index}: {binary_raw}\n")