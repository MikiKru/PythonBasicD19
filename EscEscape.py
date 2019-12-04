import msvcrt

# while True
print("Podaj napis")
if(msvcrt.kbhit() and msvcrt.getch()==chr(27)):
    print("ESC")
else:
    print("XXX")