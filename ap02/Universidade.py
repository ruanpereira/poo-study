from abc import ABC, abstractmethod
class Pessoa():
    def __init__(self, nome = ''):
        self.nome = nome
    pass

class Funcionario(Pessoa, ABC):
    @abstractmethod
    def definirCursoLecionado(self, nomeDoCurso : str):
        pass
    @abstractmethod
    def definirSalario(self, valor : float):
        pass
    pass
class Estudante(Pessoa):
    @abstractmethod
    def definirCursoFrequentado(self, nomeDoCurso : str):
        pass
    @abstractmethod
    def definirMatricula(self, numero:int):
        pass
    pass
class Professor(Funcionario):
    __id = 0
    def __init__(self, nome='', salario=0, nomeDoCurso=''):
        Pessoa.__init__(self,nome)
        self.salario = salario
        self.nomeDoCurso = nomeDoCurso
        self.id = Professor.__id
        Professor.__id += 1

    def definirCursoLecionado(self, nomeDoCurso : str ):
        self.cursolec = nomeDoCurso
    def definirSalario(self, valor : float):
        self.valor = valor
    def __str__(self):
        return f'curso lecionado: {self.cursolec}, curso frequentado: {self.cursofreq}, valor: {self.valor}, matricula: {self.matricula}'

class Aluno(Estudante):
    __id = 0
    def __init__(self, nome='', matricula = 0, nomeDoCurso = ''):
        Pessoa.__init__(self,nome)
        self.matricula = matricula
        self.nomeDoCurso = nomeDoCurso
        self.id = Aluno.__id
        Aluno.__id += 1

    def definirCursoFrequentado(self, nomeDoCurso : str):
        self.curso = nomeDoCurso
    def definirMatricula(self, numero : int):
        self.matricula = numero
    def __str__(self):
        return f'curso lecionado: {self.cursolec}, curso frequentado: {self.cursofreq}, valor: {self.valor}, matricula: {self.matricula}'


class AssistentedeEnsino(Funcionario, Estudante):
    __id = 0
    def __init__(self, nome = '', matricula = 0, cursofreq = '', salario = 0, cursolec = '' ):
        Pessoa.__init__(self, nome)
        self.matricula = matricula
        self.cursofreq = cursofreq
        self.salario = salario
        self.cursiolec = cursolec
        self.id = AssistentedeEnsino.__id
        AssistentedeEnsino.__id =+1

    def definirCursoLecionado(self, nomeDoCurso : str):
        self.cursolec = nomeDoCurso
    def definirCursoFrequentado(self, nomeDoCurso : str):
        self.cursofreq = nomeDoCurso
    def definirSalario(self, valor : float):
        self.valor = valor
    def definirMatricula(self, numero : int):
        self.matricula = numero
    def __str__(self):
        return f'curso lecionado: {self.cursolec}, curso frequentado: {self.cursofreq}, valor: {self.valor}, matricula: {self.matricula}'

if __name__ == '__main__':
    p = Pessoa('Joao')
    print(p.nome)

    prof = Professor('Jose', 1000, 'matematica')
    print(prof.id)
    print(prof.nome)
    prof2 = Professor('maria', 2000, 'fisica')
    print(prof2.id)
    print(prof2.nome)
    prof.definirSalario(2000)
    print(prof.salario)
    prof.definirCursoLecionado('telecom')
    print(prof.nomeDoCurso)

    a = Aluno('cecilia', 1234, 'telecom')
    b = Aluno('ana', 234, 'telecomhj')
    

