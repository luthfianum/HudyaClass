fruits = ["mango", "apple", "banana", "orange"]
cart = []

while True:
    item = input("Masukkan barang belanja: ")
    if item.lower() == 'checkout':
        break
    if item.lower() in fruits:
        cart.append(item.capitalize()())
        print(f'Berhasil memasukkan buah: {item.capitalize()}')
    else:
        print('Buah tidak ditemukan!')
        
print("\nBarang yang dibeli:")
for item in cart:
    print(item)