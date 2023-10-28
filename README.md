# EcoEnergy
Trabalho de laboratório de python

while True:
    print('''    \n Menu principal\n     
    [ 1 ] - Módulo de Controle de Estoque de Produtos
    [ 2 ] - Módulo de Gerenciamenteo de Serviços Automotivos
    [ 3 ] - Módulo de Gestão da Mercearia
    [ 4 ] - Módulo de Monitoramento Energético
    [ 5 ] - Módulo de Relatórios e Análises
    [ 6 ] - Sair''')
    
    escolha = int(input("     \nSelecione um módulo: "))

    if escolha == 1:
        modulo_controle_estoque()

    elif escolha == 2:
        modulo_servicos_automotivos()

    elif escolha == 3:
        break

    elif escolha == 4:
        modulo_monitoramento_energetico()

    elif escolha == 5:
        break

    else:
        print("O programa foi encerrado.")
        break    
