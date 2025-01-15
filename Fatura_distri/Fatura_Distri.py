import json

# Dados do faturamento diário (em JSON)
faturamento_diario = '''
{
    "SP": [67836.43, 0, 12345.67, 0, 5678.90],
    "RJ": [0, 6789.45, 2345.67],
    "MG": [3456.78, 0, 2345.67],
    "ES": [0, 1234.56, 0, 7890.12],
    "Outros": [5000.34, 0, 2000.45]
}
'''

# Carregar os dados do faturamento
dados = json.loads(faturamento_diario)

# Preparar uma lista com todos os faturamentos
faturamentos = [valor for estados in dados.values()
                for valor in estados if valor > 0]

# Calcular o menor, maior faturamento e a média mensal
menor_faturamento = min(faturamentos)
maior_faturamento = max(faturamentos)
media_mensal = sum(faturamentos) / len(faturamentos)

# Contar o número de dias com faturamento acima da média
dias_acima_da_media = sum(1 for valor in faturamentos if valor > media_mensal)

# Exibir os resultados
print(f"Menor faturamento: R${menor_faturamento:.2f}")
print(f"Maior faturamento: R${maior_faturamento:.2f}")
print(f"Número de dias com faturamento acima da média: {dias_acima_da_media}")
