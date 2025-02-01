import random
import collections


# Classe que realiza a análise da Lotofácil
class LotofacilAnalyzer:
    # Método construtor que inicializa a classe com o caminho do arquivo
    def __init__(self, file_path):
        self.file_path = file_path
        self.jogos = self.ler_arquivo()  # Ler os resultados dos jogos
        self.frequencia = self.calcular_frequencia()  # Calcular frequência dos números sorteados
        self.fib_numeros = self.fibonacci(max(self.frequencia.keys()))  # Gerar números da sequência Fibonacci
        self.numeros_menos_comuns = self.calcular_numeros_menos_comuns()  # Calcular números menos comuns
        self.numeros_mais_comuns = self.calcular_numeros_mais_comuns()  # Calcular números mais comuns

    # Método para ler o arquivo .txt e extrair os números sorteados
    def ler_arquivo(self):
        with open(self.file_path, 'r') as file:
            resultados = file.readlines()

        jogos = []
        for resultado in resultados:
            # Remover caracteres indesejados e dividir os números
            numeros = list(map(lambda x: int(x.replace(',', '').strip()), resultado.strip().split()))
            jogos.append(numeros)
        return jogos

    # Método para calcular a frequência dos números sorteados
    def calcular_frequencia(self):
        frequencia = collections.Counter()
        for jogo in self.jogos:
            frequencia.update(jogo)
        return frequencia

    # Método para gerar a sequência de Fibonacci até um valor máximo
    def fibonacci(self, max_value):
        seq = [0, 1]
        while seq[-1] + seq[-2] <= max_value:
            seq.append(seq[-1] + seq[-2])
        return seq[2:]  # Remover os primeiros dois valores 0 e 1

    # Método para calcular os números menos comuns
    def calcular_numeros_menos_comuns(self):
        return sorted(self.frequencia, key=self.frequencia.get)[:15]

    # Método para calcular os números mais comuns
    def calcular_numeros_mais_comuns(self):
        return sorted(self.frequencia, key=self.frequencia.get, reverse=True)[:15]

    # Método para identificar padrões e sequências (exemplo simples)
    def padroes_sequencias(self):
        sequencias = []
        for jogo in self.jogos:
            if all(jogo[i] < jogo[i + 1] for i in range(len(jogo) - 1)):
                sequencias.append(jogo)
        return sequencias

    # Método para criar novos jogos com base na análise
    def criar_jogos(self, num_jogos=5):
        numeros_disponiveis = list(self.frequencia.keys())
        novos_jogos = []
        for _ in range(num_jogos):
            # Selecionar 15 números aleatórios dos números disponíveis
            jogo = random.sample(numeros_disponiveis, 15)
            # Ordenar os números do jogo
            jogo.sort()
            if any(num in jogo for num in self.fib_numeros):
                novos_jogos.append(jogo)
            else:
                # Se não houver números da sequência Fibonacci, escolher novamente
                novos_jogos.append(sorted(random.sample(self.fib_numeros, 15)))
        return novos_jogos

    # Método para realizar análise dos resultados passados e criar novos jogos
    def analisar_e_criar_jogos(self, num_jogos=5):
        novos_jogos = self.criar_jogos(num_jogos)
        print("Novos Jogos Gerados (números separados por vírgula):")
        for i, jogo in enumerate(novos_jogos, 1):
            print(f"Jogo {i}: {', '.join(map(str, jogo))}")

        # Mostrar análises adicionais
        print("\nNúmeros Menos Comuns:")
        print(self.numeros_menos_comuns)

        print("\nNúmeros Mais Comuns e suas Frequências:")
        for numero in self.numeros_mais_comuns:
            print(f"Número {numero}: {self.frequencia[numero]} vezes")

        print("\nPadrões e Sequências Identificados:")
        padroes = self.padroes_sequencias()
        for i, seq in enumerate(padroes, 1):
            print(f"Sequência {i}: {', '.join(map(str, seq))}")


# Exemplo de uso do algoritmo orientado a objetos ---
file_path = 'C:/mega/loto_facil_asloterias_ate_concurso_3290_sorteio_2.txt'
analyzer = LotofacilAnalyzer(file_path)
analyzer.analisar_e_criar_jogos()