def obter_parametros_shopee(preco, tipo_vendedor):
    #Se for CPF, a Shopee cobra uma multa de 3 reais por item vendido
    if tipo_vendedor.upper() == 'CPF':
        adicional_cpf = 3
    else:
        adicional_cpf = 0

    #Verifica o preço para decidir a comissão certa
    if preco <= 79.99:
        percentual = 0.20
        fixo = 4
    elif preco <= 99.99:
        percentual = 0.14
        fixo = 16
    elif preco <= 199.99:
        percentual = 0.14
        fixo = 20
    else:
        percentual = 0.14
        fixo = 26

    #Retorna a porcentagem e a taxa fixa (com o adicional se for CPF)
    total_fixo = fixo + adicional_cpf
    return percentual, total_fixo

def calcular_subsidio_pix(preco_venda):
    # Regra de 2026: define a porcentagem de desconto do PIX baseado no preço de venda
    if preco_venda <= 79.99:
        desconto_pct = 0.00
    elif preco_venda <= 99.99:
        desconto_pct = 0.01  # 1% de desconto
    elif preco_venda <= 199.99:
        desconto_pct = 0.015 # 1,5% de desconto
    else:
        desconto_pct = 0.02  # 2% de desconto
        
    # Retorna o valor em reais que será descontado para o comprador
    return preco_venda * desconto_pct


def calcular_preco_ideal(custo, lucro_desejado, tipo_vendedor):
    receita_necessaria = custo + lucro_desejado
    preco_sugerido = receita_necessaria
    
    # O loop roda 10 vezes para ajustar o preço aproximado ao valor real com a taxa
    for _ in range(10):
        percentual, fixo = obter_parametros_shopee(preco_sugerido, tipo_vendedor)
        # Fórmula para descobrir o preço de venda cobrindo as taxas
        preco_sugerido = (receita_necessaria + fixo) / (1 - percentual)

    # Cálculo final para apresentar na tela
    percentual_final, fixo_final = obter_parametros_shopee(preco_sugerido, tipo_vendedor)
    taxa_total = (preco_sugerido * percentual_final) + fixo_final
    comissao_real_pct = (taxa_total / preco_sugerido) * 100
    
    return preco_sugerido, taxa_total, comissao_real_pct


def executar_calculadora():
    print("-" * 50)
    print("      CALCULADORA ESTRATÉGICA SHOPEE 2026      ")
    print("-" * 50)
    #Loop de validação para o tipo de cadastro
    while True:
        tipo = input("Tipo de vendedor (CNPJ ou CPF): ").strip().upper()
        if tipo not in ['CNPJ', 'CPF']:
            print("Tipo inválido! Digite apenas CNPJ ou CPF.")
            continue
        else:
            break
    #loop de validação para o custo do produto e margem de lucro
    while True:
        try:
            custo = float(input("Custo total do produto (R$): ").replace(',', '.'))
            if custo <= 0:
                print("O custo do produto deve ser maior que zero.")
                continue
            lucro = float(input("Lucro líquido desejado (R$): ").replace(',', '.'))
            if lucro <= 0:
                print("O lucro desejado deve ser maior que zero.")
                continue
        except ValueError:
            print("Erro: Digite apenas números válidos.")
            continue
        break

    #Chama a função principal que faz os cálculos 
    preco_venda, taxa_shopee, pct_real = calcular_preco_ideal(custo, lucro, tipo)
    
    #Chama a nova função para calcular o subsídio do PIX e o preço final ao consumidor
    valor_desconto_pix = calcular_subsidio_pix(preco_venda)
    preco_final_comprador = preco_venda - valor_desconto_pix

    #Mostra os resultados finais
    print("\n" + "=" * 50)
    print(f"LUCRO LÍQUIDO: R$ {lucro:.2f}")
    print("=" * 50)
    print(f"""PREÇO DE VENDA IDEAL (CADASTRAR NO ANÚNCIO): R$ {preco_venda:.2f}
Total retido pela Shopee: R$ {taxa_shopee:.2f}
Impacto real da comissão: {pct_real:.1f}% do preço final""")
    print("-" * 50)
    print(f"""Desconto do Subsídio PIX (Pago pela Shopee): R$ {valor_desconto_pix:.2f}
PREÇO VISÍVEL PARA O COMPRADOR NO PIX: R$ {preco_final_comprador:.2f}""")
    print("=" * 50)
    #Alerta caso o custo fixo comprometa a viabilidade do produto devido ao preço baixo
    if pct_real > 25:
        print("""ALERTA: A taxa consumiu mais de 25% do valor final.
O preço do item está baixo para essa estrutura de taxas fixas.""")
        print("=" * 50)

if __name__ == "__main__":
    executar_calculadora()