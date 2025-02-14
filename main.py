class ConversorCNAB400:
    def __init__(self, mapeamento=None):
        self.mapeamento = mapeamento or {
            "90": "10",
            # Adicione aqui outros códigos e suas respectivas substituições
        }

    def substituir_codigo(self, codigo):
        """
        Substitui códigos específicos na coluna de retorno CNAB 400.
        """
        if codigo in self.mapeamento:
            return self.mapeamento[codigo]
        else: 
            return codigo
    
    def processar_arquivo_cnab(self, nome_arquivo_entrada, nome_arquivo_saida):
        """
        Processa o arquivo CNAB 400, realizando as substituições na coluna 109-110
        """
        try:
            with open(nome_arquivo_entrada, "r") as arquivo_entrada:
                linhas = arquivo_entrada.readlines()

            with open(nome_arquivo_saida, "w") as arquivo_saida:
                for linha in linhas:
                    codigo = linha[108:110]
                    novo_codigo = self.substituir_codigo(codigo)
                    nova_linha = linha[:108] + novo_codigo + linha[110:]
                    arquivo_saida.write(nova_linha)
            
            print(f"Arquivo '{nome_arquivo_entrada}' processado com sucesso para '{nome_arquivo_saida}'.")
        
        except FileNotFoundError:
            print(f"Erro: Arquivo '{nome_arquivo_entrada}' não encontrado.")
        except Exception as e:
            print(f"Ocorreu um erro: {e}")
    
    def main():
        import argparse

        parser = argparse.ArgumentParser(description="Converte arquivo CNAB 400 (layout Bradesco).")
        parser.add_argument("arquivo_entrada", help="Nome do arquivo CNAB 400  de entrada.")
        parser.add_argument("arquivo_saida", help="Nome do arquivo de saída.")
        args = parser.parse_args()

        conversor = ConversorCNAB400() # Instancia a classe ConversorCNAB400
        conversor.processar_arquivo_cnab(args.arquivo_entrada, args.arquivo_saida)
    
    if __name__=="__main__":
        main()