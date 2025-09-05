
library(httr)
library(jsonlite)

api_key <- "0a4b6aa50a754c90e3745ceb90854eb0"
cidade <- "Piracicaba,BR"

url <- paste0("https://api.openweathermap.org/data/2.5/weather?q=", cidade, "&appid=", api_key, "&units=metric&lang=pt_br")

print("Buscando dados do clima para Piracicaba...")

resposta <- GET(url)

if (status_code(resposta) == 200) {
  
  dados_clima <- fromJSON(content(resposta, "text"))
  
  descricao_clima <- dados_clima$weather$description
  temperatura_atual <- dados_clima$main$temp
  sensacao_termica <- dados_clima$main$feels_like
  umidade <- dados_clima$main$humidity
  
  cat("\n--- CONDIÇÕES DO TEMPO EM PIRACICABA ---\n")
  cat("Clima:", Hmisc::capitalize(descricao_clima), "\n")
  cat("Temperatura Atual:", temperatura_atual, "°C\n")
  cat("Sensação Térmica:", sensacao_termica, "°C\n")
  cat("Umidade:", umidade, "%\n")
  cat("----------------------------------------\n")
  
} else {
  print("Erro ao buscar os dados do clima. Verifique sua chave de API ou a conexão.")
  print(content(resposta, "text"))
}
