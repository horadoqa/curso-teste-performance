class TestePerformance:
    def stress(self):
        print("Teste de Stress: Avalia o comportamento do sistema em situações extremas, acima de sua capacidade máxima esperada.")

    def carga(self):
        print("Teste de Carga: Verifica o desempenho do sistema sob uma carga esperada de usuários, transações ou dados.")

    def pico(self):
        print("Teste de Pico: Mede a capacidade do sistema de lidar com aumentos súbitos e intensos de carga em um curto espaço de tempo.")

    def endurance(self):
        print("Teste de Endurance (ou Soak): Avalia o desempenho do sistema por um longo período sob carga constante, detectando problemas como vazamentos de memória.")

    def escalabilidade(self):
        print("Teste de Escalabilidade: Avalia a capacidade do sistema de crescer em desempenho proporcionalmente ao aumento de recursos ou usuários.")

# Exemplo de uso:
if __name__ == "__main__":
    teste = TestePerformance()
    teste.stress()
    teste.carga()
    teste.pico()
    teste.endurance()
    teste.escalabilidade()
