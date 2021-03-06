
#Tabela de normalidade para o percentual de gordura

def tabela_percent_gordura(dobras, pessoa):
#Tabela de Deurenberg - Sexo Masculino de 17 a 17 anos
    if(pessoa.sexo == 1 and pessoa.idade >= 7 and pessoa.idade <= 17 and dobras.resultado <= 6.0):
        return "Excessivamente baixa"
    elif(pessoa.sexo == 1 and pessoa.idade >= 7 and pessoa.idade <= 17 and dobras.resultado > 6.0 and dobras.resultado <= 10.0):
        return "Baixa"
    elif(pessoa.sexo == 1 and pessoa.idade >= 7 and pessoa.idade <= 17 and dobras.resultado > 10.0 and dobras.resultado <= 20.0):
        return "Adequada"
    elif(pessoa.sexo == 1 and pessoa.idade >= 7 and pessoa.idade <= 17 and dobras.resultado > 20.0 and dobras.resultado <= 25.0):
        return "Moderadamente alta"
    elif(pessoa.sexo == 1 and pessoa.idade >= 7 and pessoa.idade <= 17 and dobras.resultado > 25.0 and dobras.resultado <= 31.0):
        return "Alta"
    elif(pessoa.sexo == 1 and pessoa.idade >= 7 and pessoa.idade <= 17 and dobras.resultado > 31.0):
        return "Excessivamente alta"
        
#Tabela de Deurenberg - Sexo Feminino de 17 a 17 anos
    elif(pessoa.sexo == 2 and pessoa.idade >= 7 and pessoa.idade <= 17 and dobras.resultado <= 12.0):
        return "Excessivamente baixa"
    elif(pessoa.sexo == 2 and pessoa.idade >= 7 and pessoa.idade <= 17 and dobras.resultado > 12.0 and dobras.resultado <= 15.0):
        return "Baixa"
    elif(pessoa.sexo == 2 and pessoa.idade >= 7 and pessoa.idade <= 17 and dobras.resultado > 15.0 and dobras.resultado <= 25.0):
        return "Adequada"
    elif(pessoa.sexo == 2 and pessoa.idade >= 7 and pessoa.idade <= 17 and dobras.resultado > 25.0 and dobras.resultado <= 30.0):
        return "Moderadamente alta"
    elif(pessoa.sexo == 2 and pessoa.idade >= 7 and pessoa.idade <= 17 and dobras.resultado > 30.0 and dobras.resultado <= 36.0):
        return "Alta"
    elif(pessoa.sexo == 2 and pessoa.idade >= 7 and pessoa.idade <= 17 and dobras.resultado > 36.0):
        return "Excessivamente alta"
        
#Tabela de Pollock e Wilmore - Sexo Masculino de 18 a 25 anos
    if(pessoa.sexo == 1 and pessoa.idade >= 18 and pessoa.idade <= 25 and dobras.resultado >= 4.0 and dobras.resultado <= 6.0):
        return "Excelente"
    elif(pessoa.sexo == 1 and pessoa.idade >= 18 and pessoa.idade <= 25 and dobras.resultado >= 8.0 and dobras.resultado <= 10.0):
        return "Bom"
    elif(pessoa.sexo == 1 and pessoa.idade >= 18 and pessoa.idade <= 25 and dobras.resultado >= 12.0 and dobras.resultado <= 13.9):
        return "Acima da média"
    elif(pessoa.sexo == 1 and pessoa.idade >= 18 and pessoa.idade <= 25 and dobras.resultado >= 14.0 and dobras.resultado <= 16.9):
        return "Média"
    elif(pessoa.sexo == 1 and pessoa.idade >= 18 and pessoa.idade <= 25 and dobras.resultado >= 17.0 and dobras.resultado <= 20.9):
        return "Abaixo da média"
    elif(pessoa.sexo == 1 and pessoa.idade >= 18 and pessoa.idade <= 25 and dobras.resultado >= 20.0 and dobras.resultado <= 24.0):
        return "Ruim"
    elif(pessoa.sexo == 1 and pessoa.idade >= 18 and pessoa.idade <= 25 and dobras.resultado >= 26.0):
        return "Muito Ruim"
        
#Tabela de Pollock e Wilmore - Sexo Masculino de 26 a 35 anos
    if(pessoa.sexo == 1 and pessoa.idade >= 26 and pessoa.idade <= 35 and dobras.resultado >= 8.0 and dobras.resultado <= 11.9):
        return "Excelente"
    elif(pessoa.sexo == 1 and pessoa.idade >= 26 and pessoa.idade <= 35 and dobras.resultado >= 12.0 and dobras.resultado <= 15.9):
        return "Bom"
    elif(pessoa.sexo == 1 and pessoa.idade >= 26 and pessoa.idade <= 35 and dobras.resultado >= 16.0 and dobras.resultado <= 17.9):
        return "Acima da média"
    elif(pessoa.sexo == 1 and pessoa.idade >= 26 and pessoa.idade <= 35 and dobras.resultado >= 18.0 and dobras.resultado <= 20.9):
        return "Média"
    elif(pessoa.sexo == 1 and pessoa.idade >= 26 and pessoa.idade <= 35 and dobras.resultado >= 22.0 and dobras.resultado <= 23.9):
        return "Abaixo da média"
    elif(pessoa.sexo == 1 and pessoa.idade >= 26 and pessoa.idade <= 35 and dobras.resultado >= 24.0 and dobras.resultado <= 27.9):
        return "Ruim"
    elif(pessoa.sexo == 1 and pessoa.idade >= 26 and pessoa.idade <= 35 and dobras.resultado >= 28.0):
        return "Muito Ruim"

#Tabela de Pollock e Wilmore - Sexo Masculino de 36 a 45 anos
    if(pessoa.sexo == 1 and pessoa.idade >= 36 and pessoa.idade <= 45 and dobras.resultado >= 10.0 and dobras.resultado <= 14.9):
        return "Excelente"
    elif(pessoa.sexo == 1 and pessoa.idade >= 36 and pessoa.idade <= 45 and dobras.resultado >= 16.0 and dobras.resultado <= 18.9):
        return "Bom"
    elif(pessoa.sexo == 1 and pessoa.idade >= 36 and pessoa.idade <= 45 and dobras.resultado >= 19.0 and dobras.resultado <= 20.9):
        return "Acima da média"
    elif(pessoa.sexo == 1 and pessoa.idade >= 36 and pessoa.idade <= 45 and dobras.resultado >= 21.0 and dobras.resultado <= 23.9):
        return "Média"
    elif(pessoa.sexo == 1 and pessoa.idade >= 36 and pessoa.idade <= 45 and dobras.resultado >= 24.0 and dobras.resultado <= 25.9):
        return "Abaixo da média"
    elif(pessoa.sexo == 1 and pessoa.idade >= 36 and pessoa.idade <= 45 and dobras.resultado >= 27.0 and dobras.resultado <= 29.9):
        return "Ruim"
    elif(pessoa.sexo == 1 and pessoa.idade >= 36 and pessoa.idade <= 45 and dobras.resultado >= 30.0):
        return "Muito Ruim"

#Tabela de Pollock e Wilmore - Sexo Masculino de 46 a 55 anos
    if(pessoa.sexo == 1 and pessoa.idade >= 46 and pessoa.idade <= 55 and dobras.resultado >= 12.0 and dobras.resultado <= 16.9):
        return "Excelente"
    elif(pessoa.sexo == 1 and pessoa.idade >= 46 and pessoa.idade <= 55 and dobras.resultado >= 18.0 and dobras.resultado <= 20.9):
        return "Bom"
    elif(pessoa.sexo == 1 and pessoa.idade >= 46 and pessoa.idade <= 55 and dobras.resultado >= 21.0 and dobras.resultado <= 23.9):
        return "Acima da média"
    elif(pessoa.sexo == 1 and pessoa.idade >= 46 and pessoa.idade <= 55 and dobras.resultado >= 24.0 and dobras.resultado <= 25.9):
        return "Média"
    elif(pessoa.sexo == 1 and pessoa.idade >= 46 and pessoa.idade <= 55 and dobras.resultado >= 26.0 and dobras.resultado <= 27.9):
        return "Abaixo da média"
    elif(pessoa.sexo == 1 and pessoa.idade >= 46 and pessoa.idade <= 55 and dobras.resultado >= 28.0 and dobras.resultado <= 30.9):
        return "Ruim"
    elif(pessoa.sexo == 1 and pessoa.idade >= 46 and pessoa.idade <= 55 and dobras.resultado >= 32.0):
        return "Muito Ruim"
        
#Tabela de Pollock e Wilmore - Sexo Masculino de 56 a 65 anos
    if(pessoa.sexo == 1 and pessoa.idade >= 56 and pessoa.idade <= 65 and dobras.resultado >= 13.0 and dobras.resultado <= 18.9):
        return "Excelente"
    elif(pessoa.sexo == 1 and pessoa.idade >= 56 and pessoa.idade <= 65 and dobras.resultado >= 20.0 and dobras.resultado <= 21.9):
        return "Bom"
    elif(pessoa.sexo == 1 and pessoa.idade >= 56 and pessoa.idade <= 65 and dobras.resultado >= 22.0 and dobras.resultado <= 23.9):
        return "Acima da média"
    elif(pessoa.sexo == 1 and pessoa.idade >= 56 and pessoa.idade <= 65 and dobras.resultado >= 24.0 and dobras.resultado <= 25.9):
        return "Média"
    elif(pessoa.sexo == 1 and pessoa.idade >= 56 and pessoa.idade <= 65 and dobras.resultado >= 26.0 and dobras.resultado <= 27.9):
        return "Abaixo da média"
    elif(pessoa.sexo == 1 and pessoa.idade >= 56 and pessoa.idade <= 65 and dobras.resultado >= 28.0 and dobras.resultado <= 30.9):
        return "Ruim"
    elif(pessoa.sexo == 1 and pessoa.idade >= 56 and pessoa.idade <= 65 and dobras.resultado >= 32.0):
        return "Muito Ruim"

#Tabela de Pollock e Wilmore - Sexo Masculino acima de 65 anos
    if(pessoa.sexo == 1 and pessoa.idade >= 65 and dobras.resultado >= 14.0 and dobras.resultado <= 18.9):
        return "Excelente"
    elif(pessoa.sexo == 1 and pessoa.idade >= 65 and dobras.resultado >= 19.0 and dobras.resultado <= 21.9):
        return "Bom"
    elif(pessoa.sexo == 1 and pessoa.idade >= 65 and dobras.resultado >= 22.0 and dobras.resultado <= 23.9):
        return "Acima da média"
    elif(pessoa.sexo == 1 and pessoa.idade >= 65 and dobras.resultado >= 24.0 and dobras.resultado <= 24.9):
        return "Média"
    elif(pessoa.sexo == 1 and pessoa.idade >= 65 and dobras.resultado >= 25.0 and dobras.resultado <= 26.9):
        return "Abaixo da média"
    elif(pessoa.sexo == 1 and pessoa.idade >= 65 and dobras.resultado >= 27.0 and dobras.resultado <= 29.9):
        return "Ruim"
    elif(pessoa.sexo == 1 and pessoa.idade >= 65 and dobras.resultado >= 31.0):
        return "Muito Ruim"

#Tabela de Pollock e Wilmore - Sexo Feminino de 18 a 25 anos
    if(pessoa.sexo == 2 and pessoa.idade >= 18 and pessoa.idade <= 25 and dobras.resultado >= 13.0 and dobras.resultado <= 16.9):
        return "Excelente"
    elif(pessoa.sexo == 2 and pessoa.idade >= 18 and pessoa.idade <= 25 and dobras.resultado >= 17.0 and dobras.resultado <= 19.9):
        return "Bom"
    elif(pessoa.sexo == 2 and pessoa.idade >= 18 and pessoa.idade <= 25 and dobras.resultado >= 20.0 and dobras.resultado <= 22.9):
        return "Acima da média"
    elif(pessoa.sexo == 2 and pessoa.idade >= 18 and pessoa.idade <= 25 and dobras.resultado >= 23.0 and dobras.resultado <= 25.9):
        return "Média"
    elif(pessoa.sexo == 2 and pessoa.idade >= 18 and pessoa.idade <= 25 and dobras.resultado >= 26.0 and dobras.resultado <= 28.9):
        return "Abaixo da média"
    elif(pessoa.sexo == 2 and pessoa.idade >= 18 and pessoa.idade <= 25 and dobras.resultado >= 29.0 and dobras.resultado <= 31.0):
        return "Ruim"
    elif(pessoa.sexo == 2 and pessoa.idade >= 18 and pessoa.idade <= 25 and dobras.resultado >= 33.0):
        return "Muito Ruim"
        
#Tabela de Pollock e Wilmore - Sexo Feminino de 26 a 35 anos
    if(pessoa.sexo == 2 and pessoa.idade >= 26 and pessoa.idade <= 35 and dobras.resultado >= 14.0 and dobras.resultado <= 16.9):
        return "Excelente"
    elif(pessoa.sexo == 2 and pessoa.idade >= 26 and pessoa.idade <= 35 and dobras.resultado >= 18.0 and dobras.resultado <= 20.9):
        return "Bom"
    elif(pessoa.sexo == 2 and pessoa.idade >= 26 and pessoa.idade <= 35 and dobras.resultado >= 21.0 and dobras.resultado <= 23.9):
        return "Acima da média"
    elif(pessoa.sexo == 2 and pessoa.idade >= 26 and pessoa.idade <= 35 and dobras.resultado >= 24.0 and dobras.resultado <= 25.9):
        return "Média"
    elif(pessoa.sexo == 2 and pessoa.idade >= 26 and pessoa.idade <= 35 and dobras.resultado >= 27.0 and dobras.resultado <= 29.9):
        return "Abaixo da média"
    elif(pessoa.sexo == 2 and pessoa.idade >= 26 and pessoa.idade <= 35 and dobras.resultado >= 31.0 and dobras.resultado <= 33.9):
        return "Ruim"
    elif(pessoa.sexo == 2 and pessoa.idade >= 26 and pessoa.idade <= 35 and dobras.resultado >= 36.0):
        return "Muito Ruim"

#Tabela de Pollock e Wilmore - Sexo Feminino de 36 a 45 anos
    if(pessoa.sexo == 2 and pessoa.idade >= 36 and pessoa.idade <= 45 and dobras.resultado >= 16.0 and dobras.resultado <= 19.9):
        return "Excelente"
    elif(pessoa.sexo == 2 and pessoa.idade >= 36 and pessoa.idade <= 45 and dobras.resultado >= 20.0 and dobras.resultado <= 23.9):
        return "Bom"
    elif(pessoa.sexo == 2 and pessoa.idade >= 36 and pessoa.idade <= 45 and dobras.resultado >= 24.0 and dobras.resultado <= 26.9):
        return "Acima da média"
    elif(pessoa.sexo == 2 and pessoa.idade >= 36 and pessoa.idade <= 45 and dobras.resultado >= 27.0 and dobras.resultado <= 29.9):
        return "Média"
    elif(pessoa.sexo == 2 and pessoa.idade >= 36 and pessoa.idade <= 45 and dobras.resultado >= 30.0 and dobras.resultado <= 32.9):
        return "Abaixo da média"
    elif(pessoa.sexo == 2 and pessoa.idade >= 36 and pessoa.idade <= 45 and dobras.resultado >= 33.0 and dobras.resultado <= 36.9):
        return "Ruim"
    elif(pessoa.sexo == 2 and pessoa.idade >= 36 and pessoa.idade <= 45 and dobras.resultado >= 38.0):
        return "Muito Ruim"

#Tabela de Pollock e Wilmore - Sexo Masculino de 46 a 55 anos
    if(pessoa.sexo == 2 and pessoa.idade >= 46 and pessoa.idade <= 55 and dobras.resultado >= 17.0 and dobras.resultado <= 21.9):
        return "Excelente"
    elif(pessoa.sexo == 2 and pessoa.idade >= 46 and pessoa.idade <= 55 and dobras.resultado >= 23.0 and dobras.resultado <= 25.9):
        return "Bom"
    elif(pessoa.sexo == 2 and pessoa.idade >= 46 and pessoa.idade <= 55 and dobras.resultado >= 26.0 and dobras.resultado <= 28.9):
        return "Acima da média"
    elif(pessoa.sexo == 2 and pessoa.idade >= 46 and pessoa.idade <= 55 and dobras.resultado >= 29.0 and dobras.resultado <= 31.9):
        return "Média"
    elif(pessoa.sexo == 2 and pessoa.idade >= 46 and pessoa.idade <= 55 and dobras.resultado >= 32.0 and dobras.resultado <= 34.9):
        return "Abaixo da média"
    elif(pessoa.sexo == 2 and pessoa.idade >= 46 and pessoa.idade <= 55 and dobras.resultado >= 35.0 and dobras.resultado <= 38.9):
        return "Ruim"
    elif(pessoa.sexo == 2 and pessoa.idade >= 46 and pessoa.idade <= 55 and dobras.resultado >= 39.0):
        return "Muito Ruim"

#Tabela de Pollock e Wilmore - Sexo Feminino de 56 a 65 anos
    if(pessoa.sexo == 2 and pessoa.idade >= 56 and pessoa.idade <= 65 and dobras.resultado >= 18.0 and dobras.resultado <= 22.9):
        return "Excelente"
    elif(pessoa.sexo == 2 and pessoa.idade >= 56 and pessoa.idade <= 65 and dobras.resultado >= 24.0 and dobras.resultado <= 26.9):
        return "Bom"
    elif(pessoa.sexo == 2 and pessoa.idade >= 56 and pessoa.idade <= 65 and dobras.resultado >= 27.0 and dobras.resultado <= 29.9):
        return "Acima da média"
    elif(pessoa.sexo == 2 and pessoa.idade >= 56 and pessoa.idade <= 65 and dobras.resultado >= 30.0 and dobras.resultado <= 32.9):
        return "Média"
    elif(pessoa.sexo == 2 and pessoa.idade >= 56 and pessoa.idade <= 65 and dobras.resultado >= 33.0 and dobras.resultado <= 35.9):
        return "Abaixo da média"
    elif(pessoa.sexo == 2 and pessoa.idade >= 56 and pessoa.idade <= 65 and dobras.resultado >= 36.0 and dobras.resultado <= 38.9):
        return "Ruim"
    elif(pessoa.sexo == 2 and pessoa.idade >= 56 and pessoa.idade <= 65 and dobras.resultado >= 39.0):
        return "Muito Ruim"
        
#Tabela de Pollock e Wilmore - Sexo Feminino acima de 65 anos
    if(pessoa.sexo == 2 and pessoa.idade >= 65 and dobras.resultado >= 16.0 and dobras.resultado <= 20.9):
        return "Excelente"
    elif(pessoa.sexo == 2 and pessoa.idade >= 65 and dobras.resultado >= 22.0 and dobras.resultado <= 26.9):
        return "Bom"
    elif(pessoa.sexo == 2 and pessoa.idade >= 65 and dobras.resultado >= 27.0 and dobras.resultado <= 29.9):
        return "Acima da média"
    elif(pessoa.sexo == 2 and pessoa.idade >= 65 and dobras.resultado >= 30.0 and dobras.resultado <= 32.9):
        return "Média"
    elif(pessoa.sexo == 2 and pessoa.idade >= 65 and dobras.resultado >= 33.0 and dobras.resultado <= 34.9):
        return "Abaixo da média"
    elif(pessoa.sexo == 2 and pessoa.idade >= 65 and dobras.resultado >= 35.0 and dobras.resultado <= 37.9):
        return "Ruim"
    elif(pessoa.sexo == 2 and pessoa.idade >= 65 and dobras.resultado >= 38.0):
        return "Muito Ruim"