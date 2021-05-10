try:
    print("zero dividido.")
except ZeroDivisionError as err:
    print("erro " + err)
except err:
    print(err)
finally:
    print("================= Codigo Finalizado =================")