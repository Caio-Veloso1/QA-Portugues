import re
import pandas as pd
import matplotlib.pyplot as plt

# Carregar o arquivo
distiroberta_extended = "c:/Users/Caio/Desktop/IC/Resultados/Distilroberta-Extended.txt"
distiroberta_base = "c:/Users/Caio/Desktop/IC/Resultados/Distiroberta-Base.txt"

# Listas para armazenar os dados extraídos
data_extended = []
data_base = []

epoch_pattern = re.compile(r'\|\s*epoch\s+(\d+)\s*\|\s*step\s+(\d+)\s*\|\s*dev_acc\s+([\d.]+)\s*\|\s*test_acc\s+([\d.]+)\s*\|')

with open(distiroberta_extended, 'r', encoding='utf-8') as f:
    for line in f:
        match = epoch_pattern.search(line)
        if match:
            # Se a linha corresponder ao padrão, extrai os grupos capturados
            epoch = int(match.group(1))
            step = int(match.group(2))
            dev_acc = float(match.group(3))
            test_acc = float(match.group(4))
            
            # Adiciona os dados como um dicionário à nossa lista
            data_extended.append({
                'epoch': epoch,
                'step': step,
                'dev_acc': dev_acc,
                'test_acc': test_acc
            })
with open(distiroberta_base, 'r', encoding='utf-8') as f:
    for line in f:
        match = epoch_pattern.search(line)
        if match:
            # Se a linha corresponder ao padrão, extrai os grupos capturados
            epoch = int(match.group(1))
            step = int(match.group(2))
            dev_acc = float(match.group(3))
            test_acc = float(match.group(4))
            
            # Adiciona os dados como um dicionário à nossa lista
            data_base.append({
                'epoch': epoch,
                'step': step,
                'dev_acc': dev_acc,
                'test_acc': test_acc
            })

#dataframe para plotar o grafico
df_epochs_base = pd.DataFrame(data_base)
#df_epochs_base.to_csv('Dados Distilroberta-Base.csv', index=False)
print("==================================")
df_epochs_extended = pd.DataFrame(data_extended)
#df_epochs_extended.to_csv('Dados Distilroberta-Extended.csv', index=False)


print("Dados Distilroberta-Base")
print(df_epochs_base)
print("Grafico Distilroberta-Base")

#Grafico Distilroberta-Base

plt.style.use('seaborn-v0_8-whitegrid')
fig, ax = plt.subplots(figsize=(10, 6))
''''
ax.plot(
        df_epochs_base['epoch'], 
        df_epochs_base['dev_acc'], 
        linestyle=':',  #Pontilhado
        marker='o',     
        markersize=4,
        color='royalblue',
        label='Acurácia de Desenvolvimento (dev_acc)'
    )
ax.plot(
        df_epochs_base['epoch'], 
        df_epochs_base['test_acc'], 
        linestyle='-',  
        marker='s',     
        markersize=4,
        color='black',  
        label='Acurácia de Teste (test_acc)'
    )

ax.set_title('Distilroberta-Base', fontsize=16)
ax.set_xlabel('Época', fontsize=12)
ax.set_ylabel('Acurácia', fontsize=12)

ax.legend()

plt.tight_layout()

#plt.savefig('Grafico distilroberta-base.png', dpi=300)
'''
print("Dados Distilroberta-Extended")
print(df_epochs_extended)
print("Grafico Distilroberta-Extended")

#Grafico Distilroberta-Extended
ax.plot(
        df_epochs_extended['epoch'], 
        df_epochs_extended['dev_acc'], 
        linestyle=':',  #Pontilhado
        marker='o',     
        markersize=4,
        color='royalblue',
        label='Acurácia de Desenvolvimento (dev_acc)'
    )
ax.plot(
        df_epochs_extended['epoch'], 
        df_epochs_extended['test_acc'], 
        linestyle='-',  
        marker='s',     
        markersize=4,
        color='black',  
        label='Acurácia de Teste (test_acc)'
    )

plt.savefig('Grafico distilroberta-extended.png', dpi=300)

