#importing required modules and reading the csv file called 'laptop'
import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity
df=pd.read_csv('laptop.csv')

#list of specifications of laptops to work on
specs=['HDD','SSD','RAM','Processor','Weight','Price']

#converting all integer values to string so that they can be concattinated later in the program
for column in specs:
    df[column]=df[column].apply(str)

#Comma-separated End-User input of the specifications of laptop he is looking for(Case sensitivity to be taken care)
userspecs=input("Enter the HHD(GB),SSD(GB),RAM(GB),maximum weight(kg),Processor,maximum affordable price(in Rs) of the required Laptop:\n").split(',')

#Picking the laptops which exactly match the end-user specifications from dataframe
laptop_info_list=[]
laptops_list=[]
req_laptop_list=[]
for row_number in range(0,len(df)):
    for laptop_info in df.iloc[row_number]:
        laptop_info_list.append(laptop_info)
    laptops_list.append(laptop_info_list)
    laptop_info_list=[]

for laptops_list_ele in laptops_list:
    if laptops_list_ele[2]==userspecs[0] and laptops_list_ele[3]==userspecs[1] and laptops_list_ele[4]==userspecs[2] and int(laptops_list_ele[5])<=int(userspecs[3]) and laptops_list_ele[6]==userspecs[4] and int(laptops_list_ele[7])<=int(userspecs[5]):
        req_laptop_list.append(laptops_list_ele[1])

#a function to combine the values of the different columns into a single string
def combined_specs(row):
    return(row['HDD']+" "+row['SSD']+" "+row['RAM']+" "+row['Processor']+" "+row['Weight']+" "+row['Price'])

#a function to get the 'Name' from 'Index'
def get_name_from_index(index):
    return df[df.Index==index]['Name'].values[0]

#a function to get the 'Index' from 'Name'
def get_index_from_name(name):
    return df[df.Name==name]['Index'].values[0]

#apply the function to each row in the dataframe to store the combined strings into a new column called combimed_specs
df['combined_specs']=df.apply(combined_specs,axis=1)

#convert a collection of data into count_matrix
count_matrix=CountVectorizer()
count_matrix=count_matrix.fit_transform(df['combined_specs'])

#convert a the count_matrix into cosine similarity matrix
cosine_sim_mat=cosine_similarity(count_matrix)

#Find laptop index of req_laptop_list
if len(req_laptop_list)==0:
    print("""We are sorry :(
    We couldn't find the laptops with such specifications in our source!!
    We recommend you take care of case sensitivity of your input""")
else:
    lap = req_laptop_list[0]
    laptop_index=get_index_from_name(lap)

#Enumerating through all the similarity scores of req_laptop_list
#making a ordered pair of laptop index and similarity scores
#and returning a list of such ordered pairs in the form of (laptop_index,similarity_scores)
if len(req_laptop_list)!=0:
    similar_laptops=list(enumerate(cosine_sim_mat[laptop_index]))

#Sort similar_laptops in descending order of similarity scores and exclude the laptop with exact specifications itself
    sorted_similar_laptops=sorted(similar_laptops,key=lambda x:x[1],reverse=True)[1:]

#Laptops which exactly meet specifications given by the End-User
    print('\n')
    print("*Laptop(s) with exact specifications you have entered:","\n",end="")
    for ele in req_laptop_list:
        print(ele)
    print('\n')

#Recommendation of laptops with similairarities w.r.t specifications given by the End-User
    count=0
    print("*You can also check out these laptops:")
    for element in sorted_similar_laptops:
            if count<10:
                print(get_name_from_index(element[0]))
                count+=1




