m_inicial = float(input("Digite a massa inicial do material (Em gramas).\n"))
t_segundos = 0
massa = m_inicial

while massa > 0.05:
    t_segundos += 50
    massa /= 2
if massa <= 0.05:
    m_final = massa
    print(f"A massa inicial do material radioativo foi de :{m_inicial} gramas\n"
          f"A massa final do material radioativo é de : {m_final:.2f} gramas\n"
          f"Foram necessários: {(t_segundos/60)/60:.2f} horas.\n")
    