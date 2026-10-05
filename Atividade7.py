from datetime import datetime

# a) data e hora atuais
agora = datetime.now()
print(f"Data e hora atuais (padrão do Python): {agora}")

# b) formatada no padrão brasileiro
print(f"Data e hora (padrão brasileiro): {agora.strftime('%d/%m/%Y %H:%M:%S')}")