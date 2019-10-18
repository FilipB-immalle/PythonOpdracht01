naam = 'Filip'
klas = '6ITN'

print(f'{naam} {klas}')

print(f"""
***********
** {naam} **
***********
""")

print(f'Hallo {naam}! Wist je dat jouw naam uit ' + str(len(naam)) + ' letters bestaat?')
print()
getal1 = 192
getal2 = 168
getal3 = 240

print(f'Het getal [{getal1}] wordt in het hexadecimaal voorgesteld als [' + hex(getal1) + '] en in het binair als [' + bin(getal1) +'].')

print(f'Het getal [{getal2}] wordt in het hexadecimaal voorgesteld als [' + hex(getal2) + '] en in het binair als [' + bin(getal2) +'].')

print(f'Het getal [{getal3}] wordt in het hexadecimaal voorgesteld als [' + hex(getal3) + '] en in het binair als [' + bin(getal3) +'].')
print()

print(int(17)/int(3))
print(float(17)/float(3))
print()

bits = int(input('Hoeveel bits?\n'))
uitkomst = 2 ** bits
print(str(uitkomst) + ' verschillende getallen')