import pandas as pd
from twilio.rest import Client

# Your Account SID from twilio.com/console
account_sid = "AC1e109ea0de179d1b6a73969a8a434b73"
# Your Auth Token from twilio.com/console
auth_token  = "d49ebb8dc5e40f2a111aecc3a5ea5ba6"
client = Client(account_sid, auth_token)

# Passo a passo da solução:

# Abrir os arquivos em excel
lista_meses = ['janeiro', 'fevereiro', 'março', 'abril', 'maio', 'junho']

for mes in lista_meses:
    tabela_vendas = pd.read_excel(f'{mes}.xlsx')

    if (tabela_vendas['Vendas'] > 55000).any():
        vendedor = tabela_vendas.loc[tabela_vendas['Vendas'] > 55000, 'Vendedor'].values[0]
        vendas = tabela_vendas.loc[tabela_vendas['Vendas'] > 55000, 'Vendas'].values[0]
        print(f'No mês {mes} encontrou o vendedor {vendedor} com vendas de R${vendas}')
        message = client.messages.create(
            from_='whatsapp:+14155238886',
            body=f'No mês {mes} encontrou o vendedor {vendedor} com vendas de R${vendas}',
            to='whatsapp:+5511993353666'
        )

        print(message.sid)






# Para cada arquivo:

# Verificar se algum valor na coluna de vendas é maior que 55.000

# Se for maior que 55.000 -> Enviar SMS com o nome o mes e as vendas do vendedor



