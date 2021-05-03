import pandas as pd

country_index = {}

df = pd.read_csv("tour_cap_nat.tsv", sep="\t")
data_dict = df.to_dict(orient="index")
for key in data_dict:
    sub_dict = data_dict[key]
    bed_data = sub_dict['2016 ']
    vocab_array = data_dict[key]['accommod,unit,nace_r2,geo\\time'].split(",")
    if(vocab_array[0]=="BEDPL" and vocab_array[1]=="NR" and vocab_array[2]=="I551" and vocab_array[3] not in ["EA","EU27_2007","EU27_2020","EU28"]):country_index[vocab_array[3]] = {
        'bedrooms': "NA" if (":" in bed_data or "u" in bed_data) else ( bed_data.replace("b","") if "b" in bed_data else bed_data ),
        'internet_users': "NA"
    }

internet_users_df = pd.read_csv("tin00083.tsv", sep="\t")
internet_users_dict = internet_users_df.to_dict(orient="index")
for key in internet_users_dict:
    sub_dict = internet_users_dict[key]
    users_data = sub_dict['2016 ']
    vocab_array = sub_dict['indic_is,ind_type,unit,geo\\time'].split(",")
    if(
        vocab_array[1]=="IND_TOTAL" and
        vocab_array[3] not in ["EA","EU27_2007","EU27_2020","EU28"]
    ):
        if vocab_array[3] not in country_index.keys():
            country_index[vocab_array[3]] = {'bedrooms':"NA"}
            
        country_index[vocab_array[3]]['internet_users'] = "NA" if (":" in users_data or "u" in users_data) else ( users_data.replace("b","") if "b" in users_data else users_data )

columns = ["Country Code","Percentage of individuals online","Number of Bed-places"]

final_list = []

for country in country_index:
    final_list.append({
        columns[0]: country,
        columns[2]: country_index[country]['bedrooms'],
        columns[1]: country_index[country]['internet_users']
    })

final_list = sorted(final_list, key=lambda k: k[columns[0]])
final_df = pd.DataFrame.from_dict(final_list)
final_df.to_csv(r'generated.csv', index = False, header=True)

