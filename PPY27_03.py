# Zad1
import math


def panel_calc(room_width, room_length, panel_width, panel_length, pack_number):
   room_surface = room_width * room_length
   room_surface += room_surface * 0.1
   panel_surface = panel_width * panel_length
   amount_of_panels = room_surface / panel_surface
   amount_of_packets = amount_of_panels // pack_number
   if amount_of_panels % pack_number > 0:
       amount_of_packets += 1
   return amount_of_packets


dlPodloga = input("Podaj długość podłogi")
dlPodloga = float(dlPodloga)

szPodloga = input("Podaj szerokość podłogi")
szPodloga = float(szPodloga)

dlPanel = input("Podaj dlugość panelu")
dlPanel = float(dlPanel)

szPanel = input("Podaj szerokość panelu")
szPanel = float(szPanel)

ilPaczka = input("Podaj ilość paneli w paczce")
ilPaczka = float(ilPaczka)

print(panel_calc(dlPodloga, szPodloga, dlPanel, szPanel, ilPaczka))


# zad2

def prime(*numbers):
   for n in numbers:
       if n == 0 or n == 1:
           print(n, "is not a prime number")
       else:

           for i in (2, math.sqrt(n) + 1):
               if n % i == 0:
                   print(n, "is not a prime number")
                   break
           else:
               print(n, "is a prime number")


prime(0, 1, 2, 3, 4, 5, 6)

# Zad3

def caesarCipher(to_cipher, offset, alphabet=None):
    if alphabet is None:
        alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't',
                    'u', 'v', 'w', 'x', 'y', 'z']
    to_cipher = str.lower(to_cipher)
    offset = offset % len(alphabet)
    result = ""
    for element in to_cipher:
        if alphabet.count(element) > 0:

            if alphabet.index(element) + offset > len(alphabet) - 1:
                result += alphabet[alphabet.index(element) + offset - len(alphabet)]
            else:
                result += alphabet[alphabet.index(element) + offset]
        else:
            result += element

    return result


data = "The Project Gutenberg eBook of Alice’s Adventures in Wonderland, by Lewis Carroll"
print(caesarCipher(data, 5))
print(caesarCipher(data, 3, ['a', 'B']))
