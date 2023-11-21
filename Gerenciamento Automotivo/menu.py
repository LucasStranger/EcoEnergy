import pandas as pd
import csv
import matplotlib.pyplot as plt
vendas = pd.read_csv(r'C:/Users/lucas/EcoEnergy/Gerenciamento Automotivo/estoque_mercearia.csv', encoding='ISO-8859-1')
servicos = pd.read_csv(r'C:/Users/lucas/EcoEnergy/Gerenciamento Automotivo/gerenciamento_servicos.csv', encoding='ISO-8859-1')
paineis_solares = pd.read_csv(r'C:/Users/lucas/EcoEnergy/Gerenciamento Automotivo/dados_paineis_solares.csv', encoding='utf-8')
monitoramento = 'dados_paineis_solares.csv'
arquivo_estoque = pd.read_csv(r'C:\Users\lucas\EcoEnergy\Gerenciamento Automotivo\estoque.csv')
estoque = {'gasolina': 1000, 'álcool': 800, 'diesel': 500, 'energia_solar': 50}
estoque_minimo = 20
arquivo_servicos = "gerenciamento_servicos.csv"
veiculos = {}
agendamento = {'Amanda': 0, 'Vanessa': 0, 'Luiz': 0}
registro = {'Troca de óleo': 600, 'Troca de pneus': 400, 'Troca de peças': 100}
tempo_execucao = {'pneus': 10, 'oleo': 20, 'peças': 40}
mecanico_disponivel = {'mecânicos total': 100}
estoque_mercearia = {
    'orgânico': {
        'abacate': {'quantidade': 100, 'descricao': 'Abacate orgânico'},
        'maçã': {'quantidade': 150, 'descricao': 'Maçã orgânica'},
        'cenoura': {'quantidade': 120, 'descricao': 'Cenoura orgânica'},
        'banana': {'quantidade': 80, 'descricao': 'Banana orgânica'},
        'morango': {'quantidade': 110, 'descricao': 'Morango orgânico'},
    },
    'consumo_consciente': {
        'sabonete': {'quantidade': 50, 'descricao': 'Sabonete de origem sustentável'},
        'shampoo': {'quantidade': 80, 'descricao': 'Shampoo biodegradável'},
        'caneca': {'quantidade': 30, 'descricao': 'Caneca reutilizável'},
        'escova de dentes': {'quantidade': 75, 'descricao': 'Escova de dentes de bambu'},
        'saco de compras': {'quantidade': 100, 'descricao': 'Saco de compras reutilizável'},
    }
}
while True:
    print('''    \n Menu principal\n     
    [ 1 ] - Módulo de Controle de Estoque de Produtos
    [ 2 ] - Módulo de Gerenciamenteo de Serviços Automotivos
    [ 3 ] - Módulo de Gestão da Mercearia
    [ 4 ] - Módulo de Monitoramento Energético
    [ 5 ] - Módulo de Relatórios e Análises
    [ 6 ] - Sair''')
    escolha = int(input("     \nSelecione um módulo: "))
    
    def carregar_estoque():
        try:
            global estoque
            estoque_df = pd.read_csv(arquivo_estoque)
            estoque = dict(zip(estoque_df['produto'], estoque_df['quantidade']))
        except FileNotFoundError:
            print("Arquivo de estoque não encontrado. O estoque foi inicializado.")

    def salvar_estoque():
        estoque_df = pd.DataFrame({'produto': list(estoque.keys()), 'quantidade': list(estoque.values())})
        estoque_df.to_csv(arquivo_estoque, index=False)

    def emitir_alertas():
        print("Verificando estoque e emitindo alertas...")
        for produto, quantidade in estoque.items():
            if quantidade < estoque_minimo:
                print(f"Alerta: Estoque mínimo atingido para {produto} ({quantidade} restantes).")

    def imprimir_estoque_pandas():
        estoque_df = pd.DataFrame({'produto': list(estoque.keys()), 'quantidade': list(estoque.values())})
        print("\nEstoque em formato Pandas:\n")
        print(estoque_df)
   
    def merge_sort(arr):
        if len(arr) > 1:
            mid = len(arr) // 2
            left_half = arr[:mid]
            right_half = arr[mid:]

            merge_sort(left_half)
            merge_sort(right_half)

            i = j = k = 0

            while i < len(left_half) and j < len(right_half):
                if left_half[i][1] < right_half[j][1]:
                    arr[k] = left_half[i]
                    i += 1
                else:
                    arr[k] = right_half[j]
                    j += 1
                k += 1

            while i < len(left_half):
                arr[k] = left_half[i]
                i += 1
                k += 1

            while j < len(right_half):
                arr[k] = right_half[j]
                j += 1
                k += 1
        return arr
    def ordenar_estoque():
    # Lendo os dados do arquivo CSV para um DataFrame
        estoque_df = arquivo_estoque

        # Transformando as linhas do DataFrame em uma lista de tuplas (produto, quantidade)
        dados_ordenacao = [(row['produto'], row['quantidade']) for index, row in estoque_df.iterrows()]

        # Chamando a função de ordenação (merge_sort)
        dados_ordenacao_ordenados = merge_sort(dados_ordenacao)

        # Mostrando o estoque ordenado
        print("Estoque Ordenado:")
        for produto, quantidade in dados_ordenacao_ordenados:
            print(f"Produto: {produto}, Quantidade: {quantidade}")
        
        return dados_ordenacao_ordenados
    def modulo_controle_estoque():
        while True:
            print("\nMódulo de Controle de Estoque de Produtos")
            print("1 - Registrar a quantidade de produtos recebidos dos fornecedores")
            print("2 - Atualizar o estoque após uma venda ou serviço")
            print("3 - Emitir alertas de estoque mínimo")
            print("4 - Imprimir estoque em formato Pandas")
            print("5 - Ordenação de estoque")
            print("6 - Sair")
            
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
                emitir_alertas()

            elif escolha == "4":
                imprimir_estoque_pandas()
            elif escolha == "5":
                ordenar_estoque()
            elif escolha == "6":
                salvar_estoque()
                break

            else:
                print("Opção inválida. Tente novamente.")
    def carregar_registros():
        try:
            with open(arquivo_servicos, mode='r', newline='') as file:
                reader = csv.DictReader(file)
                registros = []
                for row in reader:
                    registros.append(row)
            return registros
        except FileNotFoundError:
            return []

    def salvar_registros(registros):
        with open(arquivo_servicos, mode='w', newline='') as file:
            fieldnames = ['Data', 'Veículo', 'Serviço', 'Mecânico', 'Quantidade', 'Peças', 'Tempo']
            writer = csv.DictWriter(file, fieldnames=fieldnames)
            writer.writeheader()
            for registro in registros:
                writer.writerow(registro)

    def registrar_veiculo(registros):
        nome_veiculo = input('Digite o nome do veículo: ')
        if not any(registro['Veículo'] == nome_veiculo for registro in registros):
            novo_registro = {
                'Data': '',
                'Veículo': nome_veiculo,
                'Serviço': '',
                'Mecânico': '',
                'Quantidade': '',
                'Peças': '',
                'Tempo': ''
            }
            registros.append(novo_registro)
            print(f'Veículo {nome_veiculo} registrado com sucesso.')
        else:
            print(f'O veículo {nome_veiculo} já está registrado.')

    def agendar_servico(registros):
        atendente = input('Por favor, informe qual atendente agendou o seu serviço (Amanda, Vanessa, Luiz): ')
        registro_aten = input('Digite 1 - Troca de óleo, 2 - Troca de pneus, 3 - Troca de peças: ')
        registro_aten = int(registro_aten)

        if atendente in agendamento and mecanico_disponivel['mecânicos total'] > 0:
            agendamento[atendente] += 1
            mecanico_disponivel['mecânicos total'] -= 1
            veiculo = input('Digite o nome do veículo: ')

            if any(registro['Veículo'] == veiculo for registro in registros):
                servico = ''
                if registro_aten == 1:
                    servico = 'Troca de óleo'
                elif registro_aten == 2:
                    servico = 'Troca de pneus'
                elif registro_aten == 3:
                    servico = 'Troca de peças'
                else:
                    servico = 'Tipo de serviço desconhecido'

                data_agendamento = input('Digite a data do agendamento (no formato YYYY-MM-DD): ')
                cliente = veiculo
                mecanico = atendente
                novo_registro = {
                    'Data': data_agendamento,
                    'Veículo': cliente,
                    'Serviço': servico,
                    'Mecânico': mecanico,
                    'Quantidade': '',
                    'Peças': '',
                    'Tempo': ''
                }
                registros.append(novo_registro)
                print(f'O atendente(a) {atendente} registrou o seu serviço para o veículo {veiculo}. Número de serviços a sua frente: {agendamento[atendente]}. Mecânicos disponíveis: {mecanico_disponivel["mecânicos total"]}.')
            else:
                print(f'Nenhum veículo encontrado com o nome {veiculo}.')
        else:
            if atendente not in agendamento:
                print(f'O atendente {atendente} não está disponível para agendamentos.')
            else:
                print('Mecânicos não disponíveis no momento, volte mais tarde.')

    def registrar_detalhes_servico(registros):
        veiculo = input('Digite o nome do veículo para o qual deseja registrar detalhes de serviço: ')
        if any(registro['Veículo'] == veiculo for registro in registros):
            registro_servico = input('Digite o serviço prestado (Troca de óleo, Troca de pneus, Troca de peças): ')
            contabilizacao = int(input('Digite quantidade prestada desse serviço: '))
            pecas_utilizadas = int(input('Digite a quantidade de peças utilizadas: '))
            tempo_registro = input('Digite o produto utilizado durante o serviço (oleo, pneus, peças): ')
            tempo = int(input('Digite o tempo de execução para o serviço prestado desse produto: '))
            data_servico = input('Digite a data do serviço (no formato YYYY-MM-DD): ')

            if registro_servico in registro and tempo_registro in tempo_execucao:
                if registro[registro_servico] >= contabilizacao and tempo_execucao[tempo_registro] >= pecas_utilizadas:
                    registro[registro_servico] -= contabilizacao
                    tempo_execucao[tempo_registro] -= pecas_utilizadas

                    novo_registro = {
                        'Data': data_servico,
                        'Veículo': veiculo,
                        'Serviço': registro_servico,
                        'Mecânico': '',
                        'Quantidade': contabilizacao,
                        'Peças': pecas_utilizadas,
                        'Tempo': tempo
                    }
                    registros.append(novo_registro)
                    print(f'O registro de {registro_servico} foi atualizado para {registro[registro_servico]}.')
                    print(f'O tempo de execução {tempo_registro} foi atualizado para {tempo_execucao[tempo_registro]}.')
                    print(f'Detalhes do serviço {registro_servico} atualizados: Quantidade: {contabilizacao}, Peças Utilizadas: {pecas_utilizadas}, Tempo de Execução: {tempo}')
                else:
                    print('Quantidade insuficiente de serviço, peças ou tempo de execução disponível.')
            else:
                print('Serviço ou produto não encontrado.')
        else:
            print(f'Nenhum veículo encontrado com o nome {veiculo}.')

    def exibir_historico_servicos(registros):
        veiculo = input('Digite o nome do veículo para o qual deseja ver o histórico: ')
        print(f'Histórico de serviços para o veículo {veiculo}:')
        for registro in registros:
            if registro['Veículo'] == veiculo:
                print(f'Data: {registro["Data"]}, Serviço: {registro["Serviço"]}, Quantidade: {registro["Quantidade"]}, Peças Utilizadas: {registro["Peças"]}, Tempo de Execução: {registro["Tempo"]}')
    def merge_sort_servicos(registros):
        if len(registros) > 1:
            meio = len(registros) // 2
            esquerda = registros[:meio]
            direita = registros[meio:]

            merge_sort_servicos(esquerda)
            merge_sort_servicos(direita)

            i = j = k = 0

            while i < len(esquerda) and j < len(direita):
                
                if esquerda[i]['Data'] < direita[j]['Data']:
                    registros[k] = esquerda[i]
                    i += 1
                else:
                    registros[k] = direita[j]
                    j += 1
                k += 1

            while i < len(esquerda):
                registros[k] = esquerda[i]
                i += 1
                k += 1

            while j < len(direita):
                registros[k] = direita[j]
                j += 1
                k += 1
    def modulo_servicos_automotivos():
        registros = carregar_registros()

        while True:
            print('\nMódulo de Gerenciamento de Serviços Automotivos')
            print('1 - Registrar veículo')
            print('2 - Agendamento de serviços')
            print('3 - Registro detalhado dos serviços')
            print('4 - Histórico de serviços prestados')
            print('5 - ordenação dos serviços')
            print('6 - Sair')

            escolha = input('Digite o número da opção desejada: ')

            if escolha == '1':
                registrar_veiculo(registros)
                
            elif escolha == '2':
                agendar_servico(registros)
                
            elif escolha == '3':
                registrar_detalhes_servico(registros)
                
            elif escolha == '4':
                exibir_historico_servicos(registros)
            elif escolha == '5':
                merge_sort_servicos(registros)
                print("\nHistórico de serviços ordenado por data:")
                for registro in registros:
                    print(f"Data: {registro['Data']}, Veículo: {registro['Veículo']}, Serviço: {registro['Serviço']}")
            elif escolha == '6':
                print('Saindo do módulo de serviços automotivos.')
                salvar_registros(registros)
                break

            else:
                print('Opção inválida. Por favor, escolha uma opção válida.')
    def carregar_estoque():
        try:
            with open('estoque_mercearia.csv', mode='r', newline='') as file:
                reader = csv.DictReader(file)
                for row in reader:
                    categoria = row['Categoria']
                    produto = row['Produto']
                    quantidade = int(row['Quantidade'])
                    descricao = row['Descrição']
                    if categoria in estoque_mercearia and produto in estoque_mercearia[categoria]:
                        estoque_mercearia[categoria][produto]['quantidade'] = quantidade
                        estoque_mercearia[categoria][produto]['descricao'] = descricao
        except FileNotFoundError:
            print("Arquivo de estoque não encontrado. O estoque foi inicializado.")

    def salvar_estoque():
        with open('estoque_mercearia.csv', mode='w', newline='') as file:
            fieldnames = ['Categoria', 'Produto', 'Quantidade', 'Descrição']
            writer = csv.DictWriter(file, fieldnames=fieldnames)
            writer.writeheader()
            for categoria, produtos in estoque_mercearia.items():
                for produto, info in produtos.items():
                    writer.writerow({'Categoria': categoria, 'Produto': produto, 'Quantidade': info['quantidade'], 'Descrição': info['descricao']})

    def exibir_tabela():
        data = []
        for categoria, produtos in estoque_mercearia.items():
            for produto, info in produtos.items():
                data.append([categoria, produto, info['quantidade'], info['descricao']])
        
        df = pd.DataFrame(data, columns=['Categoria', 'Produto', 'Quantidade', 'Descrição'])
        print(df)

    def msp(produtos):
        if len(produtos) > 1:
            meio = len(produtos) // 2
            m_esq = produtos[:meio]
            m_dir = produtos[meio:]

            msp(m_esq)
            msp(m_dir)

            i, j, k = 0, 0, 0

            while i < len(m_esq) and j < len(m_dir):
                if m_esq[i]['quantidade'] > m_dir[j]['quantidade']:
                    produtos[k] = m_esq[i]
                    i += 1
                else:
                    produtos[k] = m_dir[j]
                    j += 1
                k += 1

            while i < len(m_esq):
                produtos[k] = m_esq[i]
                i += 1
                k += 1

            while j < len(m_dir):
                produtos[k] = m_dir[j]
                j += 1
                k += 1

    def exibir_menu():
        print("\nMódulo de Controle de Estoque da Mercearia")
        print("1 - Registrar a quantidade de produtos recebidos dos fornecedores")
        print("2 - Atualizar o estoque após uma venda ou serviço")
        print("3 - Emitir alertas de estoque mínimo")
        print("4 - Adicionar novo produto à mercearia")
        print("5 - ordenação de produtos/vendas do estoque da mercearia")
        print("6 - Sair")

    def registrar_recebimento():
        categoria = input("Digite a categoria do produto (orgânico/consumo_consciente): ")
        if categoria not in estoque_mercearia:
            print("Categoria não reconhecida.")
            return

        produto = input("Digite o produto recebido: ")
        if produto in estoque_mercearia[categoria]:
            quantidade = int(input("Digite a quantidade recebida: "))
            estoque_mercearia[categoria][produto]['quantidade'] += quantidade
            print(f"Estoque de {produto} atualizado para {estoque_mercearia[categoria][produto]['quantidade']}.")
        else:
            print("Produto não reconhecido.")

    def atualizar_estoque():
        categoria = input("Digite a categoria do produto vendido (orgânico ou consumo_consciente): ")
        if categoria not in estoque_mercearia:
            print("Categoria inválida. Use 'orgânico' ou 'consumo_consciente'.")
            return

        produto = input(f"Digite o nome do produto {categoria} vendido: ")
        if produto in estoque_mercearia[categoria]:
            quantidade = int(input("Digite a quantidade vendida: "))
            if estoque_mercearia[categoria][produto]['quantidade'] >= quantidade:
                estoque_mercearia[categoria][produto]['quantidade'] -= quantidade
                print(f"Estoque de {produto} atualizado para {estoque_mercearia[categoria][produto]['quantidade']}.")
            else:
                print("Quantidade insuficiente em estoque.")
        else:
            print("Produto não reconhecido.")

    def adicionar_produto():
        print("Adicionar novo produto à mercearia:")
        categoria = input("Digite a categoria do produto (orgânico/consumo_consciente): ")
        if categoria not in estoque_mercearia:
            print("Categoria não reconhecida.")
            return

        produto = input("Digite o nome do novo produto: ")

        if produto in estoque_mercearia[categoria]:
            print("Produto já existente.")
            return

        quantidade = int(input(f"Digite a quantidade inicial de {produto}: "))
        descricao = input(f"Digite uma descrição para {produto}: ")

        estoque_mercearia[categoria][produto] = {'quantidade': quantidade, 'descricao': descricao}
        print(f"{produto} adicionado à mercearia.")

    def emitir_alertas():
        for categoria, produtos in estoque_mercearia.items():
            for produto, info in produtos.items():
                if info['quantidade'] < 100:
                    print(f"Alerta: Estoque mínimo atingido para {produto} ({info['quantidade']} restantes).")
    
    def carregar_dados(monitoramento):
        try:
            # Carregar os dados do CSV para um DataFrame
            df = pd.read_csv(monitoramento)
            return df
        except FileNotFoundError:
            # Se o arquivo não for encontrado, crie um DataFrame vazio
            return pd.DataFrame()

    def salvar_dados(monitoramento, df):
        # Salvar o DataFrame de volta para o arquivo CSV
        df.to_csv(monitoramento, index=False)

    def modulo_monitoramento_energetico(monitoramento):
        dados = carregar_dados(monitoramento)

        while True:
            print('''\nMódulo de Monitoramento Energético
            [1] - Criar Painel Solar
            [2] - Editar Painel Solar
            [3] - Apagar Painel Solar
            [4] - Calcular Energia Solar
            [5] - Calcular Economia
            [6] - Leituras em tempo real da energia gerada pelos painéis solares
            [7] - Análises de eficiência e economia proporcionada pela energia solar
            [8] - Alertas em caso de falhas ou baixa produção de energia solar
            [9] - Sair''')

            escolha_energetico = int(input("\nSelecione uma opção: "))

            if escolha_energetico == 1:
                dados = criar_painel_solar(dados)

            elif escolha_energetico == 2:
                dados = editar_painel_solar(dados)

            elif escolha_energetico == 3:
                dados = apagar_painel_solar(dados)

            elif escolha_energetico == 4:
                dados = calcular_energia_solar(dados)

            elif escolha_energetico == 5:
                dados = calcular_economia(dados)

            elif escolha_energetico == 6:
                leituras_em_tempo_real(dados)

            elif escolha_energetico == 7:
                analises_eficiencia_economia(dados)

            elif escolha_energetico == 8:
                verificar_alertas(dados)

            elif escolha_energetico == 9:
                salvar_dados(monitoramento, dados)
                break

            else:
                print("Opção inválida. Por favor, escolha uma opção válida.")

    def criar_painel_solar(df):
        nome = input("Informe um nome para o painel solar: ")
        area = float(input("Informe a área dos painéis solares (em metros quadrados): "))
        eficiencia = float(input("Informe a eficiência dos painéis solares (em percentual): "))

        novo_painel = pd.DataFrame({
            'Nome': [nome],
            'Área (m²)': [area],
            'Eficiência (%)': [eficiencia],
            'Leitura Atual (watts)': [0],
            'Falha': [False],
            'Baixa Produção': [False],
            'Economia (R$)': [0]
        })

        df = pd.concat([df, novo_painel], ignore_index=True)
        salvar_dados(monitoramento, df)
        print(f"Painel solar '{nome}' criado com sucesso!")
        return df


    def editar_painel_solar(df):
        print("\nPainéis Solares:")
        for i, row in df.iterrows():
            print(f"{i + 1}. Nome: {row['Nome']}, Área: {row['Área (m²)']} m², Eficiência: {row['Eficiência (%)']}%")

        escolha = int(input("\nSelecione o número do painel que deseja editar: ")) - 1

        if 0 <= escolha < len(df):
            area = float(input("Informe a nova área dos painéis solares (em metros quadrados): "))
            eficiencia = float(input("Informe a nova eficiência dos painéis solares (em percentual): "))

            df.at[escolha, 'Área (m²)'] = area
            df.at[escolha, 'Eficiência (%)'] = eficiencia

            salvar_dados(monitoramento, df)
            print("Painel solar editado com sucesso!")

        else:
            print("Opção inválida.")
        return df

    def apagar_painel_solar(df):
        print("\nPainéis Solares:")
        for i, row in df.iterrows():
            print(f"{i + 1}. Nome: {row['Nome']}, Área: {row['Área (m²)']} m², Eficiência: {row['Eficiência (%)']}%")

        escolha = int(input("\nSelecione o número do painel que deseja apagar: ")) - 1

        if 0 <= escolha < len(df):
            df = df.drop(escolha)
            df = df.reset_index(drop=True)
            salvar_dados(monitoramento, df)
            print("Painel solar apagado com sucesso!")

        else:
            print("Opção inválida.")
        return df

    def calcular_energia_solar(df):
        for i, row in df.iterrows():
            area = row['Área (m²)']
            eficiencia = row['Eficiência (%)'] / 100
            leitura_atual = area * eficiencia * 1000
            df.at[i, 'Leitura Atual (watts)'] = leitura_atual

        salvar_dados(monitoramento, df)
        print("Energia solar calculada com sucesso para todos os painéis!")
        return df

    def calcular_economia(df):
        for i, row in df.iterrows():
            leitura_atual = row['Leitura Atual (watts)']
            economia_mensal = (leitura_atual / 1000) * 0.5 * 30
            df.at[i, 'Economia (R$)'] = economia_mensal

        salvar_dados(monitoramento, df)
        print("Economia calculada com sucesso para todos os painéis!")
        return df

    def leituras_em_tempo_real(df):
        print("\nLeituras em Tempo Real:")
        for i, row in df.iterrows():
            print(f"Nome: {row['Nome']}, Leitura Atual: {row['Leitura Atual (watts)']} watts")

    def analises_eficiencia_economia(df):
        print("\nAnálises de Eficiência e Economia:")
        for i, row in df.iterrows():
            economia_mensal = row['Economia (R$)']
            eficiencia = row['Eficiência (%)']
            print(f"Nome: {row['Nome']}, Economia Mensal: R${economia_mensal:.2f}, Eficiência: {eficiencia}%")

    def verificar_alertas(df):
        print("\nAlertas:")
        for i, row in df.iterrows():
            nome = row['Nome']
            falha = row['Falha']
            baixa_producao = row['Baixa Produção']
            if falha:
                print(f"ALERTA: Falha detectada no painel solar '{nome}'!")
            if baixa_producao:
                print(f"ALERTA: Baixa produção de energia solar detectada no painel solar '{nome}'!")
    
    def gerar_grafico_linhas(df, x_col, y_col, titulo, cor):
        plt.figure(figsize=(8, 6))
        plt.plot(df[x_col], df[y_col], marker='o', linestyle='-', color=cor, label=titulo)
        plt.title(titulo)
        plt.xlabel('Categoria')
        plt.ylabel('Quantidade')
        plt.grid(True)
        plt.legend()
        plt.show()

    def analisar_vendas():
        gerar_grafico_linhas(vendas, 'Categoria', 'Quantidade', 'Relatório de Vendas', 'blue')

    def analisar_desempenho_servicos():
        gerar_grafico_linhas(servicos, 'Veiculo', 'Quantidade', 'Desempenho dos Serviços Automotivos', 'green')

    def analisar_eficiencia_energetica_economia():
        gerar_grafico_linhas(paineis_solares, 'Eficiência (%)', 'Economia (R$)', 'Eficiência Energética e Economia', 'red')

    def modulo_relatorio_analise():
        while True:
            print('''\nMódulo de Relatório e Análise
            [1] - Relatório de Vendas
            [2] - Desempenho dos Serviços Automotivos
            [3] - Análise de Eficiência Energética e Economia
            [4] - Sair''')

            escolha = int(input("\nSelecione uma opção: "))

            if escolha == 1:
                analisar_vendas()
            elif escolha == 2:
                analisar_desempenho_servicos()
            elif escolha == 3:
                analisar_eficiencia_energetica_economia()
            elif escolha == 4:
                break
            else:
                print("Opção inválida. Por favor, escolha uma opção válida.")


    if escolha == 1:
        carregar_estoque()
        modulo_controle_estoque()

    elif escolha == 2:
        modulo_servicos_automotivos()

    elif escolha == 3:
        while True:
            exibir_menu()
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
                msp(estoque_mercearia)
            elif escolha == "6":
                salvar_estoque()
                exibir_tabela()
                break
            else:
                print("Opção inválida. Tente novamente.")

    elif escolha == 4:
        modulo_monitoramento_energetico(monitoramento)

    elif escolha == 5:
        modulo_relatorio_analise()
        break

    else:
        print("O programa foi encerrado.")
        break 
