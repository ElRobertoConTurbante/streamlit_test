import pymongo
import pandas as pd
import streamlit as st


client = pymongo.MongoClient("mongodb://bigdata-mongodb-04.virtual.uniandes.edu.co:8087")
db = client.bigdata09
collection=db.results_preg1


def first_result(year_low,year_hi,month_low,month_hi,day_low,day_hi):
    query_1 = {"Year":{'$gt' :year_low, '$lt':year_hi},"Month":{'$gt':month_low, '$lt':month_hi},"Day":{'$gt':day_low, '$lt':day_hi}}
    df1 = pd.DataFrame(list(collection.find(query_1))) 
    state_out=df1.loc[df1['count'].idxmax()]['State']
    amount_out=df1.loc[df1['count'].idxmax()]['count']
    return(state_out)



def main():
    #titulo
    st.title('Most ')
    #titulo de sidebar
    st.sidebar.header('User Input Parameters')

    #funcion para poner los parametrso en el sidebar
    def user_input_parameters():
        min_year = st.sidebar.number_input('Min year', 2017, 2021, 2018)
        max_year = st.sidebar.number_input('Max year', 2017, 2021, 2020)
        min_month = st.sidebar.number_input('Min Month', 1, 12, 6)
        max_month = st.sidebar.number_input('Max Month', 1, 12, 6)
        min_day = st.sidebar.number_input('Min Day', 1, 31, 13)
        max_day = st.sidebar.number_input('Max Day', 1, 31, 13)
        data = {'Min year': min_year,
                'Max year': max_year,
                'Min month': min_month,
                'Max month': max_month,
                'Min day': min_day,
                'Max day': max_day
                }
        features = [min_year,max_year,min_month,max_month,min_day,max_day]
        return features

    input_list = user_input_parameters()


    st.subheader('User Input Parameters')
    st.write(input_list)

    if st.button('RUN'):
        st.success(first_result(input_list[0],input_list[1],input_list[2],input_list[3],input_list[4],input_list[5]))


if __name__ == '__main__':
    main()






