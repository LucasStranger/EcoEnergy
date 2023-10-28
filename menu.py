while True:
    print('''    \n Menu principal\n     
    [ 1 ] - Módulo de Controle de Estoque de Produtos
    [ 2 ] - Módulo de Gerenciamenteo de Serviços Automotivos
    [ 3 ] - Módulo de Gestão da Mercearia
    [ 4 ] - Módulo de Monitoramento Energético
    [ 5 ] - Módulo de Relatórios e Análises
    [ 6 ] - Sair''')
    
    escolha = int(input("     \nSelecione um módulo: "))
    estoque = {'gasolina': 1000, 'álcool': 800, 'diesel': 500, 'energia_solar': 50, 'orgânico': 200, 'consumo_consciente': 150}
    produtos_detalhes = {'gasolina': 'Combustível comum', 'álcool': 'Combustível alternativo', 'diesel': 'Combustível para motores diesel', 'energia_solar': 'Fonte de energia renovável', 'orgânico': 'Produtos orgânicos', 'consumo_consciente': 'Produtos de consumo consciente'}
    registro_detalhado = {
    'troca de oleo': {'quantidade': 100, 'peças_utilizadas': 50, 'tempo_execução': 30},
    'troca de pneus': {'quantidade': 200, 'peças_utilizadas': 100, 'tempo_execução': 60},
    'troca de peças': {'quantidade': 300, 'peças_utilizadas': 150, 'tempo_execução': 90}
    }
    veiculos = {}
    agendamento = {'Amanda': 0, 'Vanessa': 0, 'Luiz': 0}
    registro = {'troca de oleo': 600, 'troca de pneus': 400, 'troca de peças': 100}
    tempo_execução = {'pneus': 10, 'oleo': 20, 'peças': 40}
    mecanico_disponivel = {'mecânicos total': 100}

    def modulo_controle_estoque():
        while True:
            print("\nMódulo de Controle de Estoque de Produtos")
            print("1 - Registrar a quantidade de produtos recebidos dos fornecedores")
            print("2 - Atualizar o estoque após uma venda ou serviço")
            print("3 - Emitir alertas de estoque mínimo")
            print("4 - Sair")
            
            escolha = input("Digite o número da opção desejada: ")

            if escolha == "1":
                produto = input("Digite o produto recebido (gasolina, álcool, diesel, energia_solar): ")
                quantidade = int(input("Digite a quantidade recebida: "))
                estoque[produto] += quantidade
                print(f"Estoque de {produto} atualizado para {estoque[produto]}.")

            elif escolha == "2":
                produto = input("Digite o produto vendido (gasolina, álcool, diesel, energia_solar): ")
                quantidade = int(input("Digite a quantidade vendida: "))
                if estoque[produto] >= quantidade:
                    estoque[produto] -= quantidade
                    print(f"Estoque de {produto} atualizado para {estoque[produto]}.")
                else:
                    print("Quantidade insuficiente em estoque.")

            elif escolha == "3":
                for produto, quantidade in estoque.items():
                    if quantidade < 100:
                        print(f"Alerta: Estoque mínimo atingido para {produto} ({quantidade} restantes).")

            elif escolha == "4":
                break
    def modulo_servicos_automotivos():
            while True:
                print('\nMódulo de Gerenciamento de Serviços Automotivos')
                print('1 - Registrar veículo')
                print('2 - Agendamento de serviços')
                print('3 - Registro detalhado dos serviços')
                print('4 - Histórico de serviços prestados')
                print('5 - Sair')

                escolha = input('Digite o número da opção desejada: ')

                if escolha == '1':
                    nome_veiculo = input('Digite o nome do veículo: ')
                    veiculos[nome_veiculo] = {
                    'histórico_serviços': [],
                    'outras_informações': {}
                }
                    print(f'Veículo {nome_veiculo} registrado com sucesso.')

                elif escolha == '2':
                    atendente = input('Por favor, informe qual atendente agendou o seu serviço (Amanda, Vanessa, Luiz): ')
                    registro_aten = input('Digite 1 - Troca de oleo, 2 - Troca de pneus, 3 - Troca de peças: ')
                    registro_aten = int(registro_aten)
                    if mecanico_disponivel['mecânicos total'] > 0:
                        agendamento[atendente] += 1
                        mecanico_disponivel['mecânicos total'] -= 1
                        veiculo = input('Digite o nome do veículo: ')

                        if 'histórico_serviços' not in veiculos[veiculo]:
                            veiculos[veiculo]['histórico_serviços'] = []

                        veiculos[veiculo]['histórico_serviços'].append((atendente, registro_aten))

                        print(f'O atendente(a) {atendente} registrou o seu serviço para o veículo {veiculo}. Número de serviços a sua frente: {agendamento[atendente]}. Mecânicos disponíveis: {mecanico_disponivel["mecânicos total"]}.')
                    else:
                        print('Mecânicos não disponíveis no momento, volte mais tarde')

                elif escolha == '3':
                    print('\nRegistro Detalhado de Serviços')
                    veiculo = input('Digite o nome do veículo para o qual deseja registrar detalhes de serviço: ')

                    if veiculo in veiculos:
                        registro_serviço = input('Digite o serviço prestado (troca de oleo, troca de pneus, troca de peças): ')
                        contabilização = int(input('Digite quantidade prestada desse serviço: '))
                        peças_utilizadas = int(input('Digite a quantidade de peças utilizadas: '))
                        tempo_registro = input('Digite o produto utilizado durante o serviço (pneus, oleo, peças): ')
                        tempo = int(input('Digite o tempo de execução para o serviço prestado desse produto: '))

                        if registro_serviço in registro_detalhado and tempo_registro in tempo_execução:
                            if registro[registro_serviço] >= contabilização and tempo_execução[tempo_registro] >= peças_utilizadas:
                                registro[registro_serviço] -= contabilização
                                tempo_execução[tempo_registro] -= peças_utilizadas

                                veiculos[veiculo]['histórico_serviços'].append(
                                    (registro_serviço, contabilização, peças_utilizadas, tempo_registro, tempo)
                                )

                                if registro_serviço in veiculos[veiculo]['outras_informações']:
                                    veiculos[veiculo]['outras_informações'][registro_serviço]['quantidade'] += contabilização
                                    veiculos[veiculo]['outras_informações'][registro_serviço]['peças_utilizadas'] += peças_utilizadas
                                    veiculos[veiculo]['outras-informações'][registro_serviço]['tempo_execução'] += tempo
                                else:
                                    veiculos[veiculo]['outras_informações'][registro_serviço] = {
                                        'quantidade': contabilização,
                                        'peças_utilizadas': peças_utilizadas,
                                        'tempo_execução': tempo
                                    }

                                print(f'O registro de {registro_serviço} foi atualizado para {registro[registro_serviço]}.')
                                print(f'O tempo de execução {tempo_registro} foi atualizado para {tempo_execução[tempo_registro]}.')
                                print(f'Detalhes do serviço {registro_serviço} atualizados: Quantidade: {contabilização}, Peças Utilizadas: {peças_utilizadas}, Tempo de Execução: {tempo}')
                            else:
                                print('Quantidade insuficiente de serviço, peças ou tempo de execução disponível.')
                        else:
                            print('Serviço ou produto não encontrado.')
                    else:
                        print(f'Nenhum veículo encontrado com o nome {veiculo}.')

                elif escolha == '4':
                    print('\nHistórico de Serviços Prestados')
                    veiculo = input('Digite o nome do veículo para o qual deseja ver o histórico: ')

                    if veiculo in veiculos:
                        print(f'Histórico de serviços para o veículo {veiculo}:')
                        for item in veiculos[veiculo]['histórico_serviços']:
                            if len(item) == 2:
                                atendente, registro_aten = item
                                print(f'Atendente: {atendente}, Serviço agendado: {registro_aten}')
                            elif len(item) == 5:
                                registro_serviço, contabilização, peças_utilizadas, tempo_registro, tempo = item
                                print(f'Serviço: {registro_serviço}, Quantidade realizada: {contabilização}, Peças Utilizadas: {peças_utilizadas}, Tempo de Execução: {tempo}')
                    else:
                        print(f'Nenhum registro encontrado para o veículo {veiculo}.')

                elif escolha == '5':
                    print('Saindo do módulo de serviços automotivos.')
                    break

                else:
                    print('Opção inválida. Por favor, escolha uma opção válida.')    
    
    def exibir_menu():
        while True:
            print("\nMódulo de Controle de Estoque da Mercearia")
            print("1 - Registrar a quantidade de produtos recebidos dos fornecedores")
            print("2 - Atualizar o estoque após uma venda ou serviço")
            print("3 - Emitir alertas de estoque mínimo")
            print("4 - Adicionar novo produto à mercearia")
            print("5 - Sair")

            escolha = input("Digite o número da opção desejada: ")

            if escolha == "1":
                registrar_recebimento()
            elif escolha == "2":
                atualizar_estoque()
            elif escolha == "3":
                emitir_alertas()
            elif escolha == "4":
                adicionar_produto()
            elif escolha == "5":
                break
            else:
                print("Opção inválida. Tente novamente.")

    def registrar_recebimento():
            produto = input("Digite o produto recebido: ")
            if produto in estoque:
                quantidade = int(input("Digite a quantidade recebida: "))
                estoque[produto] += quantidade
                print(f"Estoque de {produto} atualizado para {estoque[produto]}.")
            else:
                print("Produto não reconhecido.")

    def atualizar_estoque():
            produto = input("Digite o produto vendido: ")
            if produto in estoque:
                quantidade = int(input("Digite a quantidade vendida: "))
                if estoque[produto] >= quantidade:
                    estoque[produto] -= quantidade
                    print(f"Estoque de {produto} atualizado para {estoque[produto]}.")
                else:
                    print("Quantidade insuficiente em estoque.")
            else:
                print("Produto não reconhecido.")

    def emitir_alertas():
            for produto, quantidade in estoque.items():
                if quantidade < 100:
                    print(f"Alerta: Estoque mínimo atingido para {produto} ({quantidade} restantes).")

    def adicionar_produto():
            novo_produto = input("Digite o nome do novo produto: ")
            if novo_produto not in estoque:
                estoque[novo_produto] = int(input(f"Digite a quantidade inicial de {novo_produto}: "))
                produtos_detalhes[novo_produto] = input(f"Digite uma descrição para {novo_produto}: ")
                print(f"{novo_produto} adicionado à mercearia.")
            else:
                print("Produto já existente.")
    
    def modulo_monitoramento_energetico():
        while True:
            print('''\nMódulo de Monitoramento Energético
            [ 1 ] - Leituras em tempo real da energia gerada pelos painéis solares
            [ 2 ] - Análises de eficiência e economia proporcionada pela energia solar
            [ 3 ] - Alertas em caso de falhas ou baixa produção de energia solar
            [ 4 ] - Voltar ao Menu Principal''')

            escolha_energetico = int(input("\nSelecione uma opção: "))

            if escolha_energetico == '1':
                leituras_em_tempo_real()

            elif escolha_energetico == '2':
                analises_eficiencia_economia()

            elif escolha_energetico == '3':
                verificar_alertas()

            elif escolha_energetico == '4':
                break

            else:
                print("Opção inválida. Por favor, escolha uma opção válida.")
            
        def leituras_em_tempo_real():
                leitura_atual = 150  # Em watts
                print(f"Leitura atual: {leitura_atual} watts")
                return leitura_atual

        def analises_eficiencia_economia():
                economia_mensal = 50  # Em reais
                eficiencia = 85  # Em percentual
                print(f"Economia mensal: R${economia_mensal}")
                print(f"Eficiência dos painéis solares: {eficiencia}%")

        def verificar_alertas():
                falha = False
                baixa_producao = False

                if falha:
                    print("ALERTA: Falha detectada nos painéis solares!")

                if baixa_producao:
                    print("ALERTA: Baixa produção de energia solar detectada!")
    
    if escolha == 1:
        modulo_controle_estoque()

    elif escolha == 2:
        modulo_servicos_automotivos()

    elif escolha == 3:
        exibir_menu()

    elif escolha == 4:
        modulo_monitoramento_energetico()

    elif escolha == 5:
        break

    else:
        print("O programa foi encerrado.")
        break    