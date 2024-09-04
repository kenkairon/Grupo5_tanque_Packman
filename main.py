import sys
import time

def clear_console():
    # Mover el cursor al inicio de la pantalla
    sys.stdout.write('\033[H')
    
    # Borrar todas las líneas desde el cursor hasta el final de la pantalla
    sys.stdout.write('\033[J')
    
    # Asegurar que los cambios se reflejen inmediatamente
    sys.stdout.flush()

T = 46  # Debe ser divisible por 2
u = T/2 - 1
e = " "
n = " "
l = " " * int(u)

for i in range(1, T):
    print(f"{e}     ███████]▄▄▄▄▄▄▄▄▃")
    print(f"{e} ▂▄▅█████████▅▄▃▂")
    print(f"{e}I███████████████████].")
    print(f"{e}◥0▲0▲0▲0▲0▲0▲0▲0▲0▲◤")
    print(f"------------------------------------------------------------------")
    e=" "+e
    if i <= T/2:
      print(f"==================================================================")
      print(f"{n}     .-.   .-.     .--.                         ")
      if i % 2 == 0:
        print(f"{n}    | OO| | OO|   / _.-'{l}.''.  ")
        print(f"{n}    |   | |   |   \  '-.{l}'..'  ")
      else:
        print(f"{n}    | OO| | OO|   / ___\{l}.''.  ")
        print(f"{n}    |   | |   |   \    /{l}'..'  ")
      print(f"{n}    '^^^' '^^^'    '--'                         ")
      print(f"==================================================================")
      print(f"                                                                  ")
      time.sleep(0.5)
      n=" "+n
      l=l[:-1]
    if i > T/2:
       n=n[:-1]
       print(f"==================================================================")
       print(f"{n}     .-.   .-.     .--.                         ")

       if i % 2 == 0:
        print(f"{n}    |OO | |OO |   '-._ \   ")
        print(f"{n}    |~~ | |~~ |   .-'  /   ")
       else:
        print(f"{n}    |OO | |OO |   /___ \   ")
        print(f"{n}    |~~ | |~~ |   \    /   ")
       print(f"{n}    '^^^' '^^^'    '--'                         ")
       print(f"==================================================================")
       print(f"                                                                  ")
       time.sleep(0.5)
    if i<(T-1):
        clear_console()