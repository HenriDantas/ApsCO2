def calculoEmissao():
    from time import sleep
    co2PessoaCarro = co2PessoaLuz = co2Lixo = 0
    print("""Qual modelo de trabalho da empresa?
        1-Presencial
        2-Híbrido
        3-Home Office""")
    tipoJob = str(input("Tipo: "))
    while tipoJob not in "123":
        tipoJob = str(input("Comando inválido digite [1, 2, 3]: "))
    if tipoJob == "1":
        Qtpessoas = int(input("Quantas pessoas trabalham na empresa? "))
        co2PessoaCarro = Qtpessoas * 230 
        co2Lixo = Qtpessoas * 150
        co2PessoaTotal = co2Lixo + co2PessoaCarro
    elif tipoJob == "2":
        Qtpessoas = int(input("Quantas pessoas trabalham na empresa? "))
        co2PessoaCarro = Qtpessoas * 110
        co2PessoaLuz = Qtpessoas * 200
        co2Lixo = Qtpessoas * 150
        co2PessoaTotal = co2Lixo + co2PessoaLuz + co2PessoaCarro
    else:
        Qtpessoas = int(input("Quantas pessoas trabalham na empresa? "))
        co2PessoaLuz = Qtpessoas * 390
        co2Lixo = Qtpessoas * 150
        co2PessoaTotal = co2Lixo + co2PessoaLuz
    sleep(0.25)
    print("\nAVISO: SEMPRE COLOQUE OS VALORES CONTANDO DE TODAS AS PESSOAS DA EMPRESA\n")
    sleep(0.3)
    print("""Para o calculo de emissão do combustivel, selecione a opção desejada! 
        1-Por litro usado, menos preciso, com menos detalhes
        2-Por kilometro andado, mais preciso, com maiores detalhes""")
    tipoCalc = input("Opção: ") 
    while tipoCalc not in "12":
        tipoCalc = str(input("Comando inválido digite [1, 2]: "))
    co2Litro = 0
    kmAno = co2Carro = 0
    mais = outroComb = "S"
    if tipoCalc == "1":
        sleep(0.25)
        Litros = float(input("Quantos litros de combustivel todos da empresa gastam em média no mês?(generalizando todos os tipos)\nQuantidade: "))
        co2Litro += Litros * 20
    else:
        while outroComb in "S":
            sleep(0.25)
            print("""Qual tipo de combustivel o veículo usa?
        1-Gasolina
        2-Diesel
        3-Álcool
        4-Gás natural""")
            tipoComb = str(input("Tipo: "))
            sleep(0.25)
            while tipoComb not in "1234":
                tipoComb = str(input("Comando inválido digite [1, 2, 3, 4]: "))
            if tipoComb == "1":
                while mais in "S":
                    sleep(0.25)
                    print("""Qual seu tipo de veículo?
        1-Pequeno(até 1,4L)
        2-Médio(de 1,5 a 2L)
        3-Grande(mais que 2L)
        4-Motocicleta""")
                    tipoCarro = str(input("Tipo: "))
                    while tipoCarro not in "1234":
                        tipoCarro = str(input("Comando inválido digite [1, 2, 3, 4]: "))
                    if tipoCarro == "1":
                        kmMes = float(input("Quantos Km roda por mês: "))
                        kmAno += kmMes * 12
                        co2Carro += kmMes * 2
                    elif tipoCarro == "2":
                        kmMes = float(input("Quantos Km roda por mês: "))
                        kmAno += kmMes * 12
                        co2Carro += kmMes * 3
                    elif tipoCarro == "3":
                        kmMes = float(input("Quantos Km roda por mês: "))
                        kmAno += kmMes * 12
                        co2Carro += kmMes * 4
                    elif tipoCarro == "4":
                        kmMes = float(input("Quantos Km roda por mês: "))
                        kmAno += kmMes * 12
                        co2Carro += kmMes
                    mais = str(input("Deseja incluir algum outro tipo de veículo[S/N]): ")).upper().strip()
                    while mais not in "SN":
                        mais = str(input("Comando inválido, digite [S/N]: ")).upper().strip()
            elif tipoComb == "2":
                while mais in "S":
                    sleep(0.25)
                    print("""Qual seu tipo de veículo?
        1-Carro
        2-Ônibus urbano
        3-Ônibus em rodovia""")
                    tipoCarro = str(input("Tipo: "))
                    while tipoCarro not in "123":
                        tipoCarro = str(input("Comando inválido, digite [1, 2, 3]: "))
                    if tipoCarro == "1":
                        kmMes = float(input("Quantos Km roda por mês: "))
                        kmAno += kmMes * 12
                        co2Carro += kmMes * 3
                    elif tipoCarro == "2":
                        kmMes = float(input("Quantos Km roda por mês: "))
                        kmAno += kmMes * 12
                        co2Carro += kmMes * 2
                    elif tipoCarro == "3":
                        kmMes = float(input("Quantos Km roda por mês: "))
                        kmAno += kmMes * 12
                        co2Carro += kmMes
                    mais = str(input("Deseja incluir algum outro tipo de veículo[S/N]): ")).upper().strip()
                    while mais not in "SN":
                        mais = str(input("Comando inválido, digite [S/N]: ")).upper().strip()
            elif tipoComb == "3":
                while mais in "S":
                    sleep(0.25)
                    print("""Qual seu tipo de carro?
        1-Pequeno(até 1,4L)
        2-Médio(de 1,5 a 2L)
        3-Grande(mais que 2L)""")
                    tipoCarro = str(input("Tipo: "))
                    while tipoCarro not in "123":
                        tipoCarro = str(input("Comando inválido, digite [1, 2, 3]: "))
                    if tipoCarro == "1" or "2" or "3":
                        kmMes = float(input("Quantos Km roda por mês: "))
                        kmAno += kmMes * 12
                        co2Carro += kmMes
                    mais = str(input("Deseja incluir algum outro tipo de veículo[S/N]): ")).upper().strip()
                    while mais not in "SN":
                        mais = str(input("Comando inválido, digite [S/N]: ")).upper().strip()
            elif tipoComb == "4":
                kmMes = float(input("Quantos Km roda por mês: "))
                kmAno += kmMes * 12
                co2Carro += kmMes * 3
            outroComb = str(input("Deseja colocar mais algum outro tipo de combustivel?[S/N]: ")).upper().strip()
            mais = "S"
            while outroComb not in "SN":
                outroComb = str(input("Comando inválido, digite [S/N]: ")).upper().strip() 
    sleep(0.25)
    locomPub = str(input("\nAlguém da empresa utiliza meios públicos de locomoção(trêm, taxi, etc)?[S/N] ")).strip().upper()
    while locomPub not in "SN":
        sleep(0.25)
        locomPub = str(input("Comando inválido, digite [S/N]: ")).upper().strip()
    co2Pub = 0
    if locomPub == "S":
        reaisLocomPub = float(input("Quantos reais em média é usado no mês para a locomoção? "))
        co2Pub = reaisLocomPub
    sleep(0.25) 
    voar = str(input("\nFoi realizado viagens de avião pela empresa durante o ano?[S/N]: ")).upper().strip()
    while voar not in "SN":
        sleep(0.25)
        voar = str(input("Comando inválido, digite [S/N]: ")).upper().strip()
    co2Voos = 0
    if voar == "S":
        outroVooTipo = "S"
        while outroVooTipo in "S":
            sleep(0.25)
            print("""Qual tipo de voo deseja adicionar?
        1-Nacional
        2-Internacional""")
            vooTipo = str(input("Tipo: "))
            while vooTipo not in "12":
                sleep(0.25)
                vooTipo = str(input("Comando inválido, digite (1, 2): ")).strip()
            if vooTipo == "1":
                voos = int(input("Quantos voos foram feitos no ultimo mês pela empresa?(ida e volta contam como 2) "))
                co2Voos += voos * 80
            else:
                voos = int(input("Quantos voos foram feitos no ultimo mês pela empresa?(ida e volta contam como 2) "))
                co2Voos += voos * 1125
            outroVooTipo = str(input("Deseja adicionar outro tipo de voo?[S/N]: ")).strip().upper()
            while outroVooTipo not in "SN":
                sleep(0.25)
                outroVooTipo = str(input("Comando inválido, digite [S/N]: ")).strip().upper()
    sleep(0.25)
    if tipoJob == "1" or "2":
        ar = str(input("\nNa empresa possui ar-condicionado?[S/N]: ")).strip().upper()
        co2Ares = 0
        while ar not in "SN":
            sleep(0.25)
            ar = str(input("Comando inválido, digite [S/N]: ")).strip().upper()
        if ar == "S":
            outroArTipo = "S"
            while outroArTipo in "S":
                sleep(0.25)
                print("""Qual tipo deseja adicionar? 
        1-Split
        2-Central""")
                arTipo = str(input("Tipo: ")).strip()
                while arTipo not in "12":
                    sleep(0.25)
                    arTipo = str(input("Comando inválido, digite (1, 2): ")).strip()
                if arTipo == "1":
                    ares = int(input("Quantos ares-condicionados splits possui dentro da empresa? "))
                    co2Ares += ares * 300
                else:
                    ares = int(input("Quantos ares-condicionados centrais possui dentro da empresa? "))
                    co2Ares += ares * 44300
                outroArTipo = str(input("Deseja adicionar outro tipo de ar-condicionado?[S/N]: ")).strip().upper()
                while outroArTipo not in "SN":
                    sleep(0.25)
                    outroArTipo = str(input("Comando inválido, digite [S/N]: ")).strip().upper()
        sleep(0.25)
        extin = str(input("\nNa empresa possui extintores de incêndio?[S/N]: ")).upper().strip()
        while extin not in "SN":
            sleep(0.25)
            extin = str(input("Comando inválido, digite [S/N]: ")).strip().upper()
        co2Extintores = 0
        if extin == "S":
            extintores = int(input("Quantos? "))
            co2Extintores = extintores * 0.6
        co2refrigerador = 0
        sleep(0.25)
        refrig = str(input("\nNa empresa possui refrigeradores?[S/N]: ")).strip().upper()
        while refrig not in "SN":
            sleep(0.2)
            refrig = str(input("Comando inválido, digite [S/N]: ")).strip().upper()
        if refrig == "S":
            refrig = int(input("Quantos? "))
            co2refrigerador = refrig
        sleep(0.25)
        gas = str(input("\nNa empresa é usado gás?[S/N]: ")).strip().upper()
        while gas not in "SN":
            sleep(0.25)
            gas = str(input("Comando inválido, digite [S/N]: ")).strip().upper()
        outroGasTipo = "S"
        co2Gas = 0
        if gas == "S":
            while outroGasTipo in "S":
                sleep(0.25)
                print("""Qual o tipo? 
        1-Botijão
        2-Encanado""")
                gasTipo = str(input("Tipo: ")).strip()
                while gasTipo not in "12":
                    sleep(0.25)
                    gasTipo = str(input("Comando inválido, digite (1, 2): ")).strip()
                if gasTipo == "1":
                    gases = float(input("Quanto é o gasto médio mensal em kg? "))
                    co2Gas += gases * 36
                else:
                    gases = float(input("Quantos M³ são consumidos em média mensalmente? "))
                    co2Gas += gases * 23
                outroGasTipo = str(input("Deseja adicionar outro tipo de Gás?[S/N]: ")).strip().upper()
                while outroGasTipo not in "SN":
                    sleep(0.25)
                    outroGasTipo = str(input("Comando inválido, digite [S/N]: ")).strip().upper()
        sleep(0.25)
        luz = int(input("\nQuanto é o custo médio mensal na conta de luz da empresa em Kwh: "))
        co2Luz = luz * 0.15
    co2Total = co2PessoaTotal + co2Litro + co2Carro + co2Pub + co2Voos + co2Ares + co2Extintores + co2refrigerador + co2Gas + co2Luz
    sleep(0.25)
    print(f"\nSua empresa emitiu no total {co2Total:.2f}Kg de CO2e no ano")
    sleep(0.25)
    tipoEmissao = str(input("Deseja saber o exato de cada tipo de emissão?[S/N]: ")).strip().upper()
    if tipoEmissao == "S":
        sleep(0.25)
        co2Transportes = co2Carro + co2Litro + co2PessoaCarro + co2Pub
        co2Energia = co2PessoaLuz + co2Luz
        co2Voo = co2Voos
        co2Fugitiva = co2Ares + co2refrigerador + co2Extintores
        co2GasEmissao = co2Gas
        co2LixoEmissao = co2Lixo
        outroTipoEmissao = "S"
        while outroTipoEmissao in "S":
            sleep(0.25)
            print("""\nQual deseja saber?
        1-Transportes
        2-Energia Elétrica
        3-Voos
        4-Emissões Fugitivas
        5-Gás
        6-Lixo""")
            tipoEmissao = str(input("Tipo: "))
            sleep(0.25)
            while tipoEmissao not in "123456":
                sleep(0.25)
                tipoEmissao = str(input("Comando inválido, digite (1, 2, 3, 4, 5, 6): ")).strip()
            if tipoEmissao == "1":
                print(f"O total das emissões dos transportes foi de {co2Transportes:.2f}Kg de CO2e no ano")
            elif tipoEmissao == "2":
                print(f"O total das emissões do uso da eletricidade foi de {co2Energia:.2f}Kg de CO2e no ano")    
            elif tipoEmissao == "3":
                print(f"O total das emissões dos voos foi de {co2Voo:.2f}Kg de CO2e no ano")    
            elif tipoEmissao == "4":
                print(f"O total das emissões fugitivas foi de {co2Fugitiva:.2f}Kg de CO2e no ano")
            elif tipoEmissao == "5":
                print(f"O total das emissões dos gases foi de {co2GasEmissao:.2f}Kg de CO2e no ano")
            else:
                print(f"O total das emissões dos resíduos foi de {co2LixoEmissao:.2f}Kg de CO2e no ano")
            sleep(0.25)
            outroTipoEmissao = str(input("Deseja saber outro tipo de emissão?[S/N]: ")).strip().upper()
            while outroTipoEmissao not in "SN":
                sleep(0.25)
                outroTipoEmissao = str(input("Comando inválido, digite [S/N]: ")).strip().upper()
    sleep(0.25)
    print(f"\nAgora para poder compensar os {co2Total}Kg de CO2e emitidos.")
    outroBuy = "S"
    while outroBuy in "S":
        print("""Você deseja comprar árvores para:
        1-Compensar
        2-Ter um crédito""")
        tipoBuyArvore = str(input("Tipo: "))
        sleep(0.25)
        while tipoBuyArvore not in "12":
            sleep(0.25)
            tipoBuyArvore = str(input("Comando inválido, digite (1, 2): ")).strip()
        if tipoBuyArvore == "1":
            qtArvore = co2Total / 190
            print(f"Sua empresa precisa comprar no máximo {qtArvore:.0f} árvores para poder compensar tudo sem ter nenhum crédito")
            print(f"e para comprar essas {qtArvore:.0f} é necessario gastar em torno de R${qtArvore * 17.6:.2f}")
        else:
            qtArvore = co2Total / 190
            print(f"Sua empresa precisa comprar no mínimo {qtArvore + 1:.0f} árvores para poder compensar tudo e ter o mínimo de crédito")
            print(f"e para comprar essas {qtArvore:.0f} árvores é necessario gastar em torno de R${qtArvore * 17.6:.2f}")
        outroBuy = str(input("\nDeseja saber o valor do outro tipo de compra?[S/N]: ")).strip().upper()
        while outroBuy not in "SN":
                sleep(0.25)
                outroBuy = str(input("Comando inválido, digite [S/N]: ")).strip().upper()

calculoEmissao()