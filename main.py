from analise_avc import (
    carregar_dados,
    preparar_dados,
    gerar_visualizacoes_gerais,
    gerar_heatmap_correlacao,
    detectar_outliers,
    executar_agrupamento,
    analisar_jovens_saudaveis
)

df = carregar_dados()
df = preparar_dados(df)
gerar_visualizacoes_gerais(df)
gerar_heatmap_correlacao(df)
detectar_outliers(df)
executar_agrupamento(df)
analisar_jovens_saudaveis(df)