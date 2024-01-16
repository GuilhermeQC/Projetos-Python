from classes import Disciplina, Professor, Aluno

professor_1 = Professor("João Rafael", "Analista de sistemas", "Exclusiva")

prof_nome, prof_form, prof_carga, prof_id = professor_1.getDados()
print(f"Nome: {prof_nome} || "
      f"Formação: {prof_form}\n"
      f"Dedicação: {prof_carga}|| "
      f"Identificação: {prof_id}")
print("")
disciplina_1 = Disciplina("Lab. de Programação", professor_1, 80)
disc_nome, disc_professor, disc_carga = disciplina_1.getDados()
print(f"Nome: {disc_nome} || ", end=""
      f"Professor: {disc_professor}\n"
      f"Carga Horaria: {disc_carga} hrs"
      )
aluno_1 = Aluno("Silas Turbando", disciplina_1, 8.7)
print(aluno_1.getDados())
