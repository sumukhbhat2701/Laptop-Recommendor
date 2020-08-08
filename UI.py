import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity
df=pd.read_csv('laptop.csv')
specs=['HDD','SSD','RAM','Processor','Weight','Price']
for column in specs:
    df[column]=df[column].apply(str)
#End-User input for the specifications of laptop he is looking for
userspecs=input("Enter the HHD(GB),SSD(GB),RAM(GB),max weight(kg),Processor,max price(in Rs):\n").split(',')
#Picking the laptops which exactly match the end-user specifications
laptop_info_list=[]
laptops_list=[]
laptop_popular_list=[]
for row_number in range(0,len(df)):
    for laptop_info in df.iloc[row_number]:
        laptop_info_list.append(laptop_info)
    laptops_list.append(laptop_info_list)
    laptop_info_list=[]
for laptops_list_ele in laptops_list:
    if laptops_list_ele[2]==userspecs[0] and laptops_list_ele[3]==userspecs[1] and laptops_list_ele[4]==userspecs[2] and laptops_list_ele[5]==userspecs[3] and laptops_list_ele[6]<=userspecs[4] and laptops_list_ele[7]<=userspecs[5]:
        laptop_popular_list.append(laptops_list_ele[1])
print(laptop_popular_list)



