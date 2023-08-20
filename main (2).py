def calcular_media_habilidade(time):
    return sum(jogador['habilidade'] for jogador in time) / len(time)

def balancear_times(jogadores, num_times):
    total_habilidades = sum(jogador['habilidade'] for jogador in jogadores)
    media_habilidade = total_habilidades / len(jogadores)
    
    jogadores.sort(key=lambda jogador: jogador['habilidade'])
    
    grupos = [jogadores[i::num_times] for i in range(num_times)]
    
    desvios = [sum(abs(jogador['habilidade'] - media_habilidade) for jogador in grupo) for grupo in grupos]
    
    melhor_combinacao = min(itertools.permutations(range(num_times)), key=lambda comb: sum(abs(desvios[i] - desvios[comb[i]]) for i in range(num_times)))
    
    times_balanceados = [[] for _ in range(num_times)]
    for i, grupo in enumerate(grupos):
        times_balanceados[melhor_combinacao[i]].extend(grupo)
    
    return times_balanceados

def obter_dados_jogador():
    nome = input("Nome: ")
    while True:
        habilidade = int(input("Nível de habilidade (1-5): "))
        if 1 <= habilidade <= 5:
            break
        else:
            print("Nível de habilidade deve estar entre 1 e 5.")
    return {'nome': nome, 'habilidade': habilidade}

def main():
    print("Bem-vindo ao Balanceador de Times")
    print("=" * 40)
    
    num_jogadores = int(input("Informe o número total de jogadores: "))
    num_times = int(input("Informe o número de times desejado: "))
    
    jogadores = []
    print("=" * 40)
    for i in range(num_jogadores):
        print(f"Jogador {i+1}")
        jogador = obter_dados_jogador()
        jogadores.append(jogador)
        print("=" * 40)
    
    times = balancear_times(jogadores, num_times)
    
    print("\nTimes Balanceados")
    print("=" * 40)
    
    for i, time in enumerate(times, start=1):
        print(f"Time {i}")
        media_habilidade = calcular_media_habilidade(time)
        
        for jogador in time:
            print(f"  {jogador['nome']} - Nível de habilidade: {jogador['habilidade']}")
        
        print(f"  Média de habilidade do time: {media_habilidade:.2f}")
        print("=" * 40)

if __name__ == "__main__":
    main()
