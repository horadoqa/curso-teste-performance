import time
import logging
import sys
from colorama import init, Fore, Style

# Inicializa o colorama (necessário no Windows)
init(autoreset=True)

class TestePerformance:
    def __init__(self):
        logging.basicConfig(filename='log_testes.txt', level=logging.INFO,
                            format='%(asctime)s - %(message)s', datefmt='%Y-%m-%d %H:%M:%S')
        print(Fore.MAGENTA + "Inicializando Testes de Performance...\n")

    def registrar_log(self, nome_teste, descricao, cor=Fore.WHITE):
        log = f"{nome_teste}: {descricao}"
        logging.info(log)
        print(cor + f"[LOG] {log}" + Style.RESET_ALL)

    def simular_carga(self, duracao=2, intensidade="moderada", cor=Fore.WHITE):
        print(cor + f"Simulando carga ({intensidade}) por {duracao} segundos..." + Style.RESET_ALL)
        time.sleep(duracao)
        print(cor + "Simulação concluída.\n" + Style.RESET_ALL)

    def stress(self):
        cor = Fore.RED
        descricao = "Teste de Stress: Avalia o comportamento do sistema em situações extremas, acima de sua capacidade máxima esperada."
        self.registrar_log("Stress", descricao, cor)
        self.simular_carga(duracao=3, intensidade="alta", cor=cor)

    def carga(self):
        cor = Fore.BLUE
        descricao = "Teste de Carga: Verifica o desempenho do sistema sob uma carga esperada de usuários, transações ou dados."
        self.registrar_log("Carga", descricao, cor)
        self.simular_carga(duracao=2, intensidade="moderada", cor=cor)

    def pico(self):
        cor = Fore.YELLOW
        descricao = "Teste de Pico: Mede a capacidade do sistema de lidar com aumentos súbitos e intensos de carga em um curto espaço de tempo."
        self.registrar_log("Pico", descricao, cor)
        self.simular_carga(duracao=1, intensidade="explosiva", cor=cor)

    def endurance(self):
        cor = Fore.CYAN
        descricao = "Teste de Endurance (ou Soak): Avalia o desempenho do sistema por um longo período sob carga constante, detectando problemas como vazamentos de memória."
        self.registrar_log("Endurance", descricao, cor)
        self.simular_carga(duracao=4, intensidade="constante e prolongada", cor=cor)

    def escalabilidade(self):
        cor = Fore.GREEN
        descricao = "Teste de Escalabilidade: Avalia a capacidade do sistema de crescer em desempenho proporcionalmente ao aumento de recursos ou usuários."
        self.registrar_log("Escalabilidade", descricao, cor)
        self.simular_carga(duracao=2, intensidade="progressiva", cor=cor)

# Execução principal
if __name__ == "__main__":
    teste = TestePerformance()

    if len(sys.argv) > 1:
        metodo = sys.argv[1].lower()
        if hasattr(teste, metodo):
            getattr(teste, metodo)()
        else:
            print(Fore.RED + f"Teste '{metodo}' não encontrado. Use: stress, carga, pico, endurance, escalabilidade.")
    else:
        # Executa todos os testes se nenhum argumento for passado
        teste.stress()
        teste.carga()
        teste.pico()
        teste.endurance()
        teste.escalabilidade()

    print(Fore.MAGENTA + "Execução finalizada.\n")
