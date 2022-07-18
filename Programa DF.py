
import pandas as pd
import numpy as np

df = pd.read_csv("C://p1/Planilha_antes.csv", sep = ";")
dados=pd.DataFrame(data=df)


df['média']= (df['nota_1']+df['nota_2'])/2

df['status']=np.where((df['média']<=7) & (df['faltas']>5),'Reprovado','Aprovado')
print(df)
    

conditionlist = [
    (df['média'] >= 7) & (df['faltas'] <5),
    (df['média'] < 7) & (df['faltas'] >=5)]
choicelist = ['Aprovado', 'Reprovado']
df['Status'] = np.select(conditionlist, choicelist, default='Not Specified')


print("Maior número de faltas:", df['faltas'].max())
print("Maior média:", df['média'].max())
print("Média da turma:", df['média'].mean())

dados.to_excel('Planilha_depois.xlsx', index=False)
