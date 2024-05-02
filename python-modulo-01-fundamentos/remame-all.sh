#!/bin/bash

# Loop pelos arquivos no diretório
for arquivo in *\[*\]*; do
    # Verifica se é um arquivo
    if [ -f "$arquivo" ]; then
        # Remove [DIO] do nome do arquivo
        novo_nome=$(echo "$arquivo" | sed 's/\[Dio\] //')
        # Renomeia o arquivo
        mv "$arquivo" "$novo_nome"
        echo "Arquivo renomeado: $arquivo -> $novo_nome"
    fi
done
