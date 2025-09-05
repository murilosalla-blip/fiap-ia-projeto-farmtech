cat("\014") 

library(dplyr)


dados <- read.csv("dados_fazenda.csv")

analise_por_cultura <- dados %>%
  group_by(cultura) %>%
  summarise(
    quantidade_de_areas = n(),
    area_total = sum(area_m2),
    media_area = mean(area_m2),
    mediana_area = median(area_m2),
    desvio_padrao_area = sd(area_m2),
    area_minima = min(area_m2),
    area_maxima = max(area_m2),
    .groups = 'drop' 
  )

analise_geral <- dados %>%
  summarise(
    area_total = sum(area_m2),
    media_area = mean(area_m2),
    mediana_area = median(area_m2),
    desvio_padrao_area = sd(area_m2),
    area_minima = min(area_m2),
    area_maxima = max(area_m2)
  )


cat("====================================================\n")
cat("=== RELATÓRIO ESTATÍSTICO - FARMTECH SOLUTIONS ===\n")
cat("====================================================\n\n")

cat("--- Análise Geral (Todas as Culturas) ---\n")
cat("Área Total Cultivada:", round(analise_geral$area_total, 2), "m²\n")
cat("Média de Área por Talhão:", round(analise_geral$media_area, 2), "m²\n")
cat("Mediana da Área por Talhão:", round(analise_geral$mediana_area, 2), "m²\n")
cat("Desvio Padrão da Área:", round(analise_geral$desvio_padrao_area, 2), "m²\n")
cat("Menor Área Cadastrada:", round(analise_geral$area_minima, 2), "m²\n")
cat("Maior Área Cadastrada:", round(analise_geral$area_maxima, 2), "m²\n\n")

cat("--- Análise Detalhada por Cultura ---\n")
print(as.data.frame(analise_por_cultura))
cat("\n====================================================\n")