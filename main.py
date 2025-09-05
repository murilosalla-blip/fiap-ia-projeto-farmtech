import csv

areas_cadastradas = []

ESPACAMENTO_CANA_METROS = 1.5
DOSE_HERBICIDA_L_HA = 5.0

print("--- Bem-vindo ao sistema da FarmTech! ---")

while True:
    print("\nEscolha uma opção:")
    print("1 - Cadastrar nova área de plantio")
    print("2 - Listar áreas cadastradas")
    print("3 - Deletar área cadastrada")
    print("4 - Atualizar área cadastrada")
    print("5 - Salvar dados e Sair")

    opcao = input("Digite o número da opção desejada: ")

    if opcao == "1":
        
        print("\n--- Cadastro de Nova Área ---")
        cultura = input("Digite o tipo de cultura (Cana de Açúcar ou Milho): ")
        comprimento_str = input("Digite o comprimento (em metros): ")
        largura_str = input("Digite a largura (em metros): ")
        comprimento = float(comprimento_str)
        largura = float(largura_str)
        area_calculada = comprimento * largura
        tipo_insumo, qtde_insumo, unidade_insumo, info_extra = "", 0, "", {}
        if "cana" in cultura.lower():
            num_ruas = int(largura / ESPACAMENTO_CANA_METROS)
            info_extra['num_ruas'] = num_ruas
            qtde_insumo = 0.5 * comprimento * num_ruas
            tipo_insumo = "Fertilizante NPK"
            unidade_insumo = "kg"
            print(f"Baseado nas dimensões {comprimento}m x {largura}m, calculamos {num_ruas} ruas de plantio.")
            print(f"Cálculo do fertilizante: 0.5 kg/m * {comprimento}m de comprimento * {num_ruas} ruas = {qtde_insumo:.2f} kg.")
        elif "milho" in cultura.lower():
            area_ha = area_calculada / 10000
            qtde_insumo = DOSE_HERBICIDA_L_HA * area_ha
            tipo_insumo = "Herbicida"
            unidade_insumo = "Litros"
            info_extra['dose_por_ha'] = DOSE_HERBICIDA_L_HA
            print(f"A área de {area_calculada:.2f} m² equivale a {area_ha:.2f} hectares.")
            print(f"Cálculo do herbicida: {area_ha:.2f} ha * {DOSE_HERBICIDA_L_HA} L/ha = {qtde_insumo:.2f} Litros.")
        nova_area = {"cultura": cultura, "comprimento": comprimento, "largura": largura, "area_m2": area_calculada, "tipo_insumo": tipo_insumo, "qtde_insumo": qtde_insumo, "unidade_insumo": unidade_insumo, "info_extra": str(info_extra)}
        areas_cadastradas.append(nova_area)
        print("\n--- Área Cadastrada com Sucesso ---")
        print(f"Cultura: {nova_area['cultura']}\nDimensões: {nova_area['comprimento']}m x {nova_area['largura']}m\nÁrea Total: {nova_area['area_m2']:.2f} m²")
        if "cana" in nova_area['cultura'].lower():
            info_extra_dict = eval(nova_area['info_extra'])
            print(f"Baseado nas dimensões {nova_area['comprimento']}m x {nova_area['largura']}m, calculamos {info_extra_dict['num_ruas']} ruas de plantio.")
            print(f"Cálculo do fertilizante: 0.5 kg/m * {nova_area['comprimento']}m de comprimento * {info_extra_dict['num_ruas']} ruas = {nova_area['qtde_insumo']:.2f} kg.")
        elif "milho" in nova_area['cultura'].lower():
            area_ha = nova_area['area_m2'] / 10000
            info_extra_dict = eval(nova_area['info_extra'])
            dose_aplicada = info_extra_dict['dose_por_ha']
            print(f"A área de {nova_area['area_m2']:.2f} m² equivale a {area_ha:.2f} hectares.")
            print(f"Cálculo do herbicida: {area_ha:.2f} ha * {dose_aplicada} L/ha = {nova_area['qtde_insumo']:.2f} Litros.")

    elif opcao == "2":
        
        print("\n--- Áreas Cadastradas ---")
        if not areas_cadastradas: print("Nenhuma área foi cadastrada ainda.")
        else:
            for i, area in enumerate(areas_cadastradas):
                print(f"\n--- Área {i+1} ---")
                print(f"Cultura: {area['cultura']}\nDimensões: {area['comprimento']}m x {area['largura']}m\nÁrea Total: {area['area_m2']:.2f} m²")
                info_extra_dict = eval(area['info_extra'])
                if "cana" in area['cultura'].lower():
                    insumo_por_rua = 0.5 * area['comprimento']
                    print(f"Ruas de plantio: {info_extra_dict['num_ruas']}")
                    print(f"Insumo Necessário: {area['qtde_insumo']:.2f} {area['unidade_insumo']} de {area['tipo_insumo']} ({insumo_por_rua:.2f} kg por rua)")
                    print(f"\n  --- Laudo de Cálculo (Cana) ---\n  - Ruas: O cálculo depende da largura ({area['largura']}m). Terreno mais largo = mais ruas.\n  - Insumo: O cálculo depende do comprimento ({area['comprimento']}m). Ruas mais curtas = menos insumo total.")
                elif "milho" in area['cultura'].lower():
                    area_ha = area['area_m2'] / 10000
                    dose_aplicada = info_extra_dict['dose_por_ha']
                    print(f"Hectares: {area_ha:.2f}")
                    print(f"Insumo Necessário: {area['qtde_insumo']:.2f} {area['unidade_insumo']} de {area['tipo_insumo']}")
                    print(f"\n  --- Laudo de Cálculo (Milho) ---\n  - Conversão de Área: {area['area_m2']:.2f} m² / 10000 = {area_ha:.2f} ha.\n  - Insumo: O cálculo usa a dose padrão de {dose_aplicada} L/ha aplicada sobre a área em hectares.")

    
    elif opcao == "3":
        print("\n--- Deletar Área Cadastrada ---")
        if not areas_cadastradas:
            print("Nenhuma área foi cadastrada para deletar.")
        else:
            for i, area in enumerate(areas_cadastradas): print(f"{i+1} - Área de {area['cultura']} ({area['area_m2']:.2f} m²)")
            
            num_a_deletar_str = input("Digite o número da área que você deseja deletar (ou 0 para voltar): ")
            
            if num_a_deletar_str == '0':
                print("Operação cancelada. Voltando ao menu.")
                continue # Volta para o início do loop while
            
            try:
                num_a_deletar = int(num_a_deletar_str)
                if 1 <= num_a_deletar <= len(areas_cadastradas):
                    area_removida = areas_cadastradas.pop(num_a_deletar - 1)
                    print(f"\nA área de {area_removida['cultura']} foi deletada com sucesso!")
                else: print("Número inválido. Nenhuma área foi deletada.")
            except ValueError: print("Entrada inválida. Por favor, digite um número.")
    
    
    elif opcao == "4":
        print("\n--- Atualizar Área Cadastrada ---")
        if not areas_cadastradas:
            print("Nenhuma área foi cadastrada para atualizar.")
        else:
            for i, area in enumerate(areas_cadastradas): print(f"{i+1} - Área de {area['cultura']} ({area['area_m2']:.2f} m²)")

            num_a_atualizar_str = input("Digite o número da área que você deseja atualizar (ou 0 para voltar): ")

            if num_a_atualizar_str == '0':
                print("Operação cancelada. Voltando ao menu.")
                continue # Volta para o início do loop while

            try:
                num_a_atualizar = int(num_a_atualizar_str)
                if 1 <= num_a_atualizar <= len(areas_cadastradas):
                    indice = num_a_atualizar - 1
                    area_antiga = areas_cadastradas[indice]
                    print(f"Você está atualizando a área de {area_antiga['cultura']}. Insira os novos dados:")
                    
                    comprimento_str = input(f"Digite o novo comprimento (anterior: {area_antiga['comprimento']}m): ")
                    largura_str = input(f"Digite a nova largura (anterior: {area_antiga['largura']}m): ")
                    
                    comprimento = float(comprimento_str)
                    largura = float(largura_str)
                    area_calculada = comprimento * largura
                    info_extra = {}
                    
                    if "cana" in area_antiga['cultura'].lower():
                        num_ruas = int(largura / ESPACAMENTO_CANA_METROS)
                        info_extra['num_ruas'] = num_ruas
                        qtde_insumo = 0.5 * comprimento * num_ruas
                    elif "milho" in area_antiga['cultura'].lower():
                        area_ha = area_calculada / 10000
                        qtde_insumo = DOSE_HERBICIDA_L_HA * area_ha
                        info_extra['dose_por_ha'] = DOSE_HERBICIDA_L_HA

                    areas_cadastradas[indice]['comprimento'] = comprimento
                    areas_cadastradas[indice]['largura'] = largura
                    areas_cadastradas[indice]['area_m2'] = area_calculada
                    areas_cadastradas[indice]['qtde_insumo'] = qtde_insumo
                    areas_cadastradas[indice]['info_extra'] = str(info_extra)
                    
                    area_atualizada = areas_cadastradas[indice]
                    print("\n--- Área Atualizada com Sucesso ---")
                    print(f"Cultura: {area_atualizada['cultura']}\nDimensões: {area_atualizada['comprimento']}m x {area_atualizada['largura']}m\nÁrea Total: {area_atualizada['area_m2']:.2f} m²")
                    if "cana" in area_atualizada['cultura'].lower():
                        info_extra_dict = eval(area_atualizada['info_extra'])
                        print(f"Baseado nas dimensões {area_atualizada['comprimento']}m x {area_atualizada['largura']}m, calculamos {info_extra_dict['num_ruas']} ruas de plantio.")
                        print(f"Cálculo do fertilizante: 0.5 kg/m * {area_atualizada['comprimento']}m de comprimento * {info_extra_dict['num_ruas']} ruas = {area_atualizada['qtde_insumo']:.2f} kg.")
                    elif "milho" in area_atualizada['cultura'].lower():
                        area_ha = area_atualizada['area_m2'] / 10000
                        info_extra_dict = eval(area_atualizada['info_extra'])
                        dose_aplicada = info_extra_dict['dose_por_ha']
                        print(f"A área de {area_atualizada['area_m2']:.2f} m² equivale a {area_ha:.2f} hectares.")
                        print(f"Cálculo do herbicida: {area_ha:.2f} ha * {dose_aplicada} L/ha = {area_atualizada['qtde_insumo']:.2f} Litros.")

                else:
                    print("Número inválido. Nenhuma área foi atualizada.")
            except ValueError:
                print("Entrada inválida. Por favor, digite um número.")

    elif opcao == "5":
        if not areas_cadastradas: print("Nenhuma área foi cadastrada para salvar.")
        else:
            nome_arquivo = "dados_fazenda.csv"
            cabecalho = areas_cadastradas[0].keys()
            with open(nome_arquivo, 'w', newline='', encoding='utf-8') as arquivo_csv:
                escritor = csv.DictWriter(arquivo_csv, fieldnames=cabecalho)
                escritor.writeheader()
                escritor.writerows(areas_cadastradas)
            print(f"\nDados salvos com sucesso no arquivo '{nome_arquivo}'!")
        print("\nSaindo do sistema... Até logo!")
        break
        
    else:
        print("\nOpção inválida! Por favor, escolha uma opção válida.")