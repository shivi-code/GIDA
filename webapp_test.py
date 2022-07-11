import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from streamlit_folium import folium_static
import folium
import plotly.express as px
from plotly.subplots import make_subplots
import plotly.graph_objects as go
import chart_studio.plotly as py
import plotly.graph_objs as go
import plotly.express as px
import base64

#Gender Discrimination and Inequality analysiss

df= pd.read_csv('C:\\Users\\dell\\crimeproject\\crime1.csv')
st.markdown("<h1 style='text-align:left; color:Black;'><u><b>Gender Discrimination and Inequality<center> Analysis</center></b></u></h1>",unsafe_allow_html=True)
st.sidebar.title("FIELDS")
select1 = st.sidebar.selectbox('Domains',options=['Choose a field','Education','Workforce','Crime'])
st.sidebar.write('You selected: ',select1)
if select1!="Crime":
    st.sidebar.title("Visualisation")
    select2=st.sidebar.selectbox('Domains',options=['Choose the type of visualisation you want to see','Bar style','Line style','Scatter style'])
    st.sidebar.write('You selected: ',select2) 
else:
    data_url=('C:\\Users\\dell\\crimeproject\\crime_processed_data.csv')
    data=pd.read_csv(data_url)
    st.sidebar.title("Visualisation")
    select3=st.sidebar.selectbox('Domains',options=['Choose the type of visualisation you want to see','Bar style','Map style'])
    #if select3=='Map style':
        #st.sidebar.title("Choose the state")
        #select2=st.sidebar.selectbox('State',options=df["STATE/UT"])

def get_base64_of_bin_file(bin_file):
    with open(bin_file,'rb') as f:
        data = f.read()
    return base64.b64encode(data).decode()

def set_png_as_page_bg(png_file):
    bin_str = get_base64_of_bin_file(png_file)
    page_bg_img = '''
    <style>
    body {
        background-image: url("data:/png;base64,%s");
        background-size: cover;
        }
    </style>
    ''' % bin_str

    st.markdown(page_bg_img,unsafe_allow_html=True)
    return
set_png_as_page_bg('purp.png')


side_bg = "whi.jpg"
side_bg_ext = "jpg"

st.markdown(

    f"""
<style>
.sidebar .sidebar-content {{
   background: url(data:{side_bg_ext};base64,{base64.b64encode(open(side_bg, "rb").read()).decode()}) 
    
    }}
background-size:cover;

</style>

    
""",unsafe_allow_html=True)


class education:
    @staticmethod
    def literacy_rate(vis):
        data= pd.read_csv('C:\\Users\\dell\\crimeproject\\literacy rate 15 years and above.csv')
        df = data.loc[data['Country Name'] =='India']
        df.dropna(axis=1,inplace=True)
        dat = df.iloc[0, 4:]
        daf = pd.DataFrame(dat).reset_index()
        daf.columns = ['years', 'literacy_rate_of_15years_ above']
        fig1 = px.scatter(daf, x="years", y="literacy_rate_of_15years_ above", color="years")
        fig2 = px.line(daf, x="years", y="literacy_rate_of_15years_ above")
        fig3 = px.bar(daf, x="years", y="literacy_rate_of_15years_ above",color="years")
        st.markdown("<h2 style='text-align:left; color:Black;'><b><center>LITERACY RATE</center></b></h2>",unsafe_allow_html=True)
        #st.title("<h2 style='text-align:left; color:Red;'><center>LITERACY RATE</center> </h2>",unsafe_allow_html=True")
        if vis=="Bar style":
            st.plotly_chart(fig3)
            st.write("<h2 style='text-align:left; color:Tomato;'><b>The literacy rate is defined by the percentage of the population of a given age group that can read and write</b></h2>",unsafe_allow_html=True)
            st.write("<h2 style='text-align:left; color:Tomato;'><b>After analysing the literacy rate of year 1981 to 2018  ..we reached to the conclusion that  literacy rate in india for the adults have been increasing'</b></h2>",unsafe_allow_html=True)
        elif vis=="Line style":
            st.plotly_chart(fig2)
            st.write("<h2 style='text-align:left; color:Tomato;'><b>The literacy rate is defined by the percentage of the population of a given age group that can read and write</b></h2>",unsafe_allow_html=True)
            st.write("<h2 style='text-align:left; color:Tomato;'><b>After analysing the literacy rate of year 1981 to 2018  ..we reached to the conclusion that  literacy rate in india for the adults have been increasing'</b></h2>",unsafe_allow_html=True)
        else:
            st.plotly_chart(fig1)
            st.write("<h2 style='text-align:left; color:Tomato;'><b>The literacy rate is defined by the percentage of the population of a given age group that can read and write</b></h2>",unsafe_allow_html=True)
            st.write("<h2 style='text-align:left; color:Tomato;'><b>After analysing the literacy rate of year 1981 to 2018  ..we reached to the conclusion that  literacy rate in india for the adults have been increasing'</b></h2>",unsafe_allow_html=True)

    @staticmethod
    def high_schooledu(vis):
        data= pd.read_csv('C:\\Users\\dell\\crimeproject\\Progression to high school female.csv')
        df = data.loc[data['Country '] =='India']
        df.dropna(axis=1,inplace=True)
        dat = df.iloc[0, 4:]
        daf = pd.DataFrame(dat).reset_index()
        daf.columns = ['years', 'count']
        fig1 = px.bar(daf, x="years", y="count",color="years")
        fig2 = px.line(daf, x="years", y="count")
        fig3 = px.scatter(daf, x="years", y="count", color="years")
        st.markdown("<h2 style='text-align:left; color:Black;'><b><center>HIGH SCHOOL EDUCATION</center></b></h2>",unsafe_allow_html=True)
        if vis=="Bar style":
            st.plotly_chart(fig1)
            st.write("<h2 style='text-align:left; color:Tomato;'><b>Progression to secondary school refers to the number of new entrants to the first grade of secondary school in a given year as a percentage of the number of students enrolled in the final grade of primary school in the previous year </b></h2>",unsafe_allow_html=True)
            st.write("<h2 style='text-align:left; color:Tomato;'><b>After analysing the Progression to high School  from year 1986 to 2017  ..we reached to the conclusion that  progression to high schook  in india for females  after the 2002 yr have been decreasing.</b></h2>",unsafe_allow_html=True)
        elif vis=="Line style":
            st.plotly_chart(fig2)
            st.write("<h2 style='text-align:left; color:Tomato;'><b>Progression to secondary school refers to the number of new entrants to the first grade of secondary school in a given year as a percentage of the number of students enrolled in the final grade of primary school in the previous year </b></h2>",unsafe_allow_html=True)
            st.write("<h2 style='text-align:left; color:Tomato;'><b>After analysing the Progression to high School from  year 1986 to 2017  ..we reached to the conclusion that  progression to high schook  in india for females  after the 2002 yr have been decreasing.</b></h2>",unsafe_allow_html=True)
        else:
            st.plotly_chart(fig3)
            st.write("<h2 style='text-align:left; color:Tomato;'><b>Progression to secondary school refers to the number of new entrants to the first grade of secondary school in a given year as a percentage of the number of students enrolled in the final grade of primary school in the previous year </b></h2>",unsafe_allow_html=True)
            st.write("<h2 style='text-align:left; color:Tomato;'><b>After analysing the Progression to high School from year 1986 to 2017  ..we reached to the conclusion that  progression to high schook  in india for females  after the 2002 yr have been decreasing.</b></h2>",unsafe_allow_html=True)
    @staticmethod
    def primary_edu(vis):
        data= pd.read_csv('C:\\Users\\dell\\crimeproject\\Primary education female.csv')
        df = data.loc[data['Country Name'] == 'India']
        df.dropna(axis=1,inplace=True)
        dat = df.iloc[0, 4:]
        daf = pd.DataFrame(dat).reset_index()
        daf.columns = ['years', 'count']
        fig1 = px.bar(daf, x="years", y="count",color="years")
        fig2 = px.line(daf, x="years", y="count")
        fig3 = px.scatter(daf, x="years", y="count", color="years")
        st.markdown("<h2 style='text-align:left; color:Black;'><b><center>PRIMARY EDUCATION</center></b></h2>",unsafe_allow_html=True)
        if vis=="Bar style":
            st.plotly_chart(fig1)
            st.write("<h2 style='text-align:left; color:Tomato;'><b>Primary education is typically the first stage of formal education, coming after preschool/kindergarten and before secondary school.</b></h2>",unsafe_allow_html=True)
            st.write("<h2 style='text-align:left; color:Tomato;'><b>After analysing the primary education  rate of year 1971 to 2017  ..we reached to the conclusion that primary education in india has been increasing by the time.</b></h2>",unsafe_allow_html=True)
        elif vis=="Line style":
            st.plotly_chart(fig2)
            st.write("<h2 style='text-align:left; color:Tomato;'><b>Primary education is typically the first stage of formal education, coming after preschool/kindergarten and before secondary school.</b></h2>",unsafe_allow_html=True)
            st.write("<h2 style='text-align:left; color:Tomato;'><b>After analysing the primary education  rate of year 1971 to 2017  ..we reached to the conclusion that primary education in india has been increasing by the time.</b></h2>",unsafe_allow_html=True)
        else:
            st.plotly_chart(fig3)
            st.write("<h2 style='text-align:left; color:Tomato;'><b>Primary education is typically the first stage of formal education, coming after preschool/kindergarten and before secondary school.</b></h2>",unsafe_allow_html=True)
            st.write("<h2 style='text-align:left; color:Tomato;'><b>After analysing the primary education  rate of year 1971 to 2017  ..we reached to the conclusion that primary education in india has been increasing by the time.</b></h2>",unsafe_allow_html=True)
    @staticmethod
    def GPI_primary(vis):
        data= pd.read_csv('C:\\Users\\dell\\crimeproject\\Parity Index (primary).csv')
        main=data[data["Country Name"]=="India"]
        main.dropna(axis=1,inplace=True)
        main.drop(["Indicator Code"],axis=1)
        main.iloc[[0]]
        temp = main.iloc[0, 4:]
        final= pd.DataFrame(temp).reset_index()
        final.columns = ['Years', 'Gender Parity Index']
        fig1 = px.scatter(final, x="Years", y="Gender Parity Index", color="Years")
        fig2 = px.line(final, x="Years", y="Gender Parity Index")
        fig3 = px.bar(final, x="Years", y="Gender Parity Index",color="Years")
       
        st.markdown("<h2 style='text-align:left; color:Black;'><b><center>GENDER PARITY INDEX PRIMARY EDUCATION</center></b></h2>",unsafe_allow_html=True)
        if vis=="Bar style":
            st.plotly_chart(fig3)
            st.write("<h2 style='text-align:left; color:Tomato;'><b>The gender parity index in primary education is the ratio of the number of female students enrolled at the primary level of education to the number of male students.</b></h2>",unsafe_allow_html=True)
            st.write("<h2 style='text-align:left; color:Tomato;'><b>After analysing the Gender parity index in primary education  from year 1971 to 2020..we reached to the conclusion that  gender parity index in primary education in india had  been increasing from 1971 to 2016 yr then it is decreasing.  </b></h2>",unsafe_allow_html=True)
        elif vis=="Line style":
            st.plotly_chart(fig2)
            st.write("<h2 style='text-align:left; color:Tomato;'><b>The gender parity index in primary education is the ratio of the number of female students enrolled at the primary level of education to the number of male students.</b></h2>",unsafe_allow_html=True)
            st.write("<h2 style='text-align:left; color:Tomato;'><b>After analysing the Gender parity index in primary education  from year 1971 to 2020..we reached to the conclusion that  gender parity index in primary education in india had  been increasing from 1971 to 2016 yr then it is decreasing.  </b></h2>",unsafe_allow_html=True)
        else:
            st.plotly_chart(fig1)
            st.write("<h2 style='text-align:left; color:Tomato;'><b>The gender parity index in primary education is the ratio of the number of female students enrolled at the primary level of education to the number of male students.</b></h2>",unsafe_allow_html=True)
            st.write("<h2 style='text-align:left; color:Tomato;'><b>After analysing the Gender parity index in primary education  from year 1971 to 2020..we reached to the conclusion that  gender parity index in primary education in india had  been increasing from 1971 to 2016 yr then it is decreasing.  </b></h2>",unsafe_allow_html=True)
    @staticmethod
    def GPI_secondary(vis):
        data= pd.read_csv('C:\\Users\\dell\\crimeproject\\Gender Parity Index(primary and secondary).csv')
        main=data[data["Country Name"]=="India"]
        main.dropna(axis=1,inplace=True)
        main.drop(["Indicator Code"],axis=1)
        main.iloc[[0]]
        temp = main.iloc[0, 4:]
        final= pd.DataFrame(temp).reset_index()
        final.columns = ['Years', 'Gender Parity Index']
        fig1 = px.scatter(final, x="Years", y="Gender Parity Index", color="Years")
        fig2 = px.line(final, x="Years", y="Gender Parity Index")
        fig3 = px.bar(final, x="Years", y="Gender Parity Index",color="Years")

        st.markdown("<h2 style='text-align:left; color:Black;'><b><center>GENDER PARITY INDEX SECONDARY EDUCATION</center></b></h2>",unsafe_allow_html=True)
        if vis=="Bar style":
            st.plotly_chart(fig3)
            st.write("<h2 style='text-align:left; color:Tomato;'><b>The gender parity index in secondary education is the ratio of the number of female students enrolled at the secondary level of education to the number of male students.</b></h2>",unsafe_allow_html=True)
            st.write("<h2 style='text-align:left; color:Tomato;'><b>After analysing the Gender parity index in secondary education  from year 1971 to 2020..we reached to the conclusion that  gender parity index in secondary education in india had  been increasing from 1971 to 2016 yr then it is decreasing till now.   </b></h2>",unsafe_allow_html=True)
            
        elif vis=="Line style":
            st.plotly_chart(fig2)
            st.write("<h2 style='text-align:left; color:Tomato;'><b>The gender parity index in secondary education is the ratio of the number of female students enrolled at the secondary level of education to the number of male students.</b></h2>",unsafe_allow_html=True)
            st.write("<h2 style='text-align:left; color:Tomato;'><b>After analysing the Gender parity index in secondary education  from year 1971 to 2020..we reached to the conclusion that  gender parity index in secondary education in india had  been increasing from 1971 to 2016 yr then it is decreasing till now.   </b></h2>",unsafe_allow_html=True)
        else:
            st.plotly_chart(fig1)
            st.write("<h2 style='text-align:left; color:Tomato;'><b>The gender parity index in secondary education is the ratio of the number of female students enrolled at the secondary level of education to the number of male students.</b></h2>",unsafe_allow_html=True)
            st.write("<h2 style='text-align:left; color:Tomato;'><b>After analysing the Gender parity index in secondary education  from year 1971 to 2020..we reached to the conclusion that  gender parity index in secondary education in india had  been increasing from 1971 to 2016 yr then it is decreasing till now.   </b></h2>",unsafe_allow_html=True)

class Workforce:
    @staticmethod
    def wagensalaries(vis):
        data1= pd.read_csv('C:\\Users\\dell\\crimeproject\\Wage and salaried workers, female.csv') 
        data2= pd.read_csv('C:\\Users\\dell\\crimeproject\\Wage and salaried workers, male.csv') 
        main1=data1[data1["Country Name"]=="India"]
        main2=data2[data2["Country Name"]=="India"]
        main1.dropna(axis=1,inplace=True)
        main2.dropna(axis=1,inplace=True)
        temp1 = main1.iloc[0, 4:]
        temp2 = main2.iloc[0, 4:]
        final1= pd.DataFrame(temp1).reset_index()
        final1.columns = ['Years', 'Wage and salaried workers(female)']  
        final2= pd.DataFrame(temp2).reset_index()
        final2.columns = ['Years', 'Wage and salaried workers(male)']
        merged_inner = pd.merge(left=final1, right=final2, left_on='Years', right_on='Years')
        fig1 = px.line(merged_inner,x="Years", y=["Wage and salaried workers(female)","Wage and salaried workers(male)"])
        fig2 = px.scatter(merged_inner,x="Years", y=["Wage and salaried workers(female)","Wage and salaried workers(male)"])
        fig3 = px.bar(final1, x="Years", y="Wage and salaried workers(female)",color="Years")
        fig4 = fig = go.Figure(data=[
        go.Bar(name='Wage and salaried workers(female)', x=merged_inner["Years"], y=merged_inner["Wage and salaried workers(female)"]),
        go.Bar(name='Wage and salaried workers(male)', x=merged_inner["Years"], y=merged_inner["Wage and salaried workers(male)"])
        ])
        # Change the bar mode
        fig.update_layout(barmode='group')  
       
        st.markdown("<h2 style='text-align:left; color:Black;'><b><center>WAGE AND SALARIED WORKERS</center></b></h2>",unsafe_allow_html=True)
        if vis=="Bar style":
            st.plotly_chart(fig3)
            st.write("<h2 style='text-align:left; color:Tomato;'><b>Wage and salaried workers are those who work for employers in the public or private sector and receive compensation in forms of salary, wage, commission or in kind etc</b></h2>",unsafe_allow_html=True)
            st.write("<h2 style='text-align:left; color:Tomato;'><b>After analysing the wages and salaried of female workers from year 1991 to 2019..we reached to the conclusion that  wages and salaries of female workers in india has  been increasing by the time.   </b></h2>",unsafe_allow_html=True)
            st.plotly_chart(fig4)
            st.write("<h2 style='text-align:left; color:Tomato;'><b>It is showing the comparison of female worker salaries and male workers salaries.</b></h2>",unsafe_allow_html=True)
            st.write("<h2 style='text-align:left; color:Tomato;'><b>After analysing the wages and salaried of female workers and male workers  from year 1991 to 2019...we reached to the conclusion that there is huge gap between the salary of females and males from 1971 to 2016 yr and after 2017 year ,we seen equality in male and women worker salaries.... </b></h2>",unsafe_allow_html=True)

        elif vis=="Line style":
            st.plotly_chart(fig1)
            st.write("<h2 style='text-align:left; color:Tomato;'><b>It is showing the comparison of female worker salaries and male workers salaries.</b></h2>",unsafe_allow_html=True)
            st.write("<h2 style='text-align:left; color:Tomato;'><b>After analysing the wages and salaried of female workers and male workers  from year 1991 to 2019...we reached to the conclusion that there is huge gap between the salary of females and males from 1971 to 2016 yr and after 2017 year ,we seen equality in male and women worker salaries.... </b></h2>",unsafe_allow_html=True)
        else:
            st.plotly_chart(fig2)
            st.write("<h2 style='text-align:left; color:Tomato;'><b>It is showing the comparison of female worker salaries and male workers salaries.</b></h2>",unsafe_allow_html=True)
            st.write("<h2 style='text-align:left; color:Tomato;'><b>After analysing the wages and salaried of female workers and male workers  from year 1991 to 2019...we reached to the conclusion that there is huge gap between the salary of females and males from 1971 to 2016 yr and after 2017 year ,we seen equality in male and women worker salaries.... </b></h2>",unsafe_allow_html=True)
    @staticmethod
    def ratio_labourforce(vis):
        data= pd.read_csv('C:\\Users\\dell\\crimeproject\\Ratio of female to male labor force participation rate.csv')
        main=data[data["Country Name"]=="India"]
        main.dropna(axis=1,inplace=True)
        temp = main.iloc[0, 4:]
        final= pd.DataFrame(temp).reset_index()
        final.columns = ['Years', 'Ratio of female to male labor force participation rate']
        fig1 = px.scatter(final, x="Years", y="Ratio of female to male labor force participation rate", color="Years")
        fig2 = px.line(final, x="Years", y="Ratio of female to male labor force participation rate")
        fig3 = px.bar(final, x="Years", y="Ratio of female to male labor force participation rate",color="Years")
    
        st.markdown("<h2 style='text-align:left; color:Black;'><b><center>FEMALE TO MALE LABOUR FORCE PARTICIPATION</center></b></h2>",unsafe_allow_html=True)
        if vis=="Bar style":
            st.plotly_chart(fig3)
           # st.write("<h2 style='text-align:left; color:Red;'><b></b></h2>",unsafe_allow_html=True)
            st.write("<h2 style='text-align:left; color:Tomato;'><b>After analysing the female to male labour force participation from year 1990 to 2019...we reached to the conclusion that  female to male labour force participation in india had  been same from 1991 to 2004 yr then it is decreasing till now.   </b></h2>",unsafe_allow_html=True)
        elif vis=="Line style":
            st.plotly_chart(fig2)
            st.write("<h2 style='text-align:left; color:Tomato;'><b>After analysing the female to male labour force participation from year 1990 to 2019...we reached to the conclusion that  female to male labour force participation in india had  been same from 1991 to 2004 yr then it is decreasing till now.   </b></h2>",unsafe_allow_html=True)
        else:
            st.plotly_chart(fig1)
            st.write("<h2 style='text-align:left; color:Tomato;'><b>After analysing the female to male labour force participation from year 1990 to 2019...we reached to the conclusion that  female to male labour force participation in india had  been same from 1991 to 2004 yr then it is decreasing till now.   </b></h2>",unsafe_allow_html=True)
    @staticmethod
    def labourforce(vis):
        data1= pd.read_csv('C:\\Users\\dell\\crimeproject\\labour male.csv')
        data2= pd.read_csv('C:\\Users\\dell\\crimeproject\\labour female.csv')
        main1=data1[data1["Country Name"]=="India"]
        main2=data2[data2["Country Name"]=="India"]
        main1.dropna(axis=1,inplace=True)
        main2.dropna(axis=1,inplace=True)
        temp1 = main1.iloc[0, 4:]
        temp2 = main2.iloc[0, 4:]
        final1= pd.DataFrame(temp1).reset_index()
        final1.columns = ['Years', 'labour participation(female)']
        final2= pd.DataFrame(temp2).reset_index()
        final2.columns = ['Years', 'labour participation (male)']
        merged_inner = pd.merge(left=final1, right=final2, left_on='Years', right_on='Years')
        fig1 = px.line(merged_inner,x="Years", y=["labour participation(female)","labour participation (male)"])
        fig2 = px.scatter(merged_inner,x="Years", y=["labour participation(female)","labour participation (male)"])
        fig3 = px.bar(final1, x="Years", y="labour participation(female)",color="Years")
        fig4 = go.Figure(data=[
        go.Bar(name='LABOUR PARTICIPATION (FEMALE)', x=merged_inner["Years"], y=merged_inner["labour participation(female)"]),
        go.Bar(name='LABOUR PARTICIPATION (MALE))', x=merged_inner["Years"], y=merged_inner["labour participation (male)"])
        ])
        # Change the bar mode
        fig4.update_layout(barmode='group')
        
        st.markdown("<h2 style='text-align:left; color:Black;'><b><center>LABOUR FORCE PARTICIPATION</center></b></h2>",unsafe_allow_html=True)
        if vis=="Bar style":
            st.plotly_chart(fig3)
            st.write("<h2 style='text-align:left; color:Tomato;'><b>The labor force participation rate represents the number of people in the labor force as a percentage of the civilian noninstitutional population</b></h2>",unsafe_allow_html=True)
            st.write("<h2 style='text-align:left; color:Tomato;'><b>After analysing labour force participation from year 1990 to 2019..we reached to the conclusion that  labour force participation in india had  been same from yr 1990 to 2004 and thwn we can see  that it is decreasing  after 2005 yr tii year 2012 and it is same till now ....   </b></h2>",unsafe_allow_html=True)
            
            st.plotly_chart(fig4)
            st.write("<h2 style='text-align:left; color:Tomato;'><b>It is showing the comparison of  men labour force participation and female labour force paticipation .</b></h2>",unsafe_allow_html=True)
            st.write("<h2 style='text-align:left; color:Tomato;'><b>After analysing  men labour force participation and female labour force paticipation from year 1990 to 2019...we reached to the conclusion that men are more  participating then women  which clearly shows that there is a lack of oppurtunity for the women in workforce .... </b></h2>",unsafe_allow_html=True)
            
        elif vis=="Line style":
            st.plotly_chart(fig1)
            st.write("<h2 style='text-align:left; color:Tomato;'><b>It is showing the comparison of  men labour force participation and female labour force paticipation .</b></h2>",unsafe_allow_html=True)
            st.write("<h2 style='text-align:left; color:Tomato;'><b>After analysing  men labour force participation and female labour force paticipation from year 1990 to 2019...we reached to the conclusion that men are more  participating then women  which clearly shows that there is a lack of oppurtunity for the women in workforce .... </b></h2>",unsafe_allow_html=True)
        else:
            st.plotly_chart(fig2)
            st.write("<h2 style='text-align:left; color:Tomato;'><b>It is showing the comparison of  men labour force participation and female labour force paticipation .</b></h2>",unsafe_allow_html=True)
            st.write("<h2 style='text-align:left; color:Tomato;'><b>After analysing  men labour force participation and female labour force paticipation from year 1990 to 2019...we reached to the conclusion that men are more  participating then women  which clearly shows that there is a lack of oppurtunity for the women in workforce .... </b></h2>",unsafe_allow_html=True)

class crime:
    @staticmethod
    def search_group(select,data):
        if select=='NONE':
            return
        else:
            for i in range(len(data["STATE/UT"])):
                if select==data["STATE/UT"].iloc[i]:
                    return data.iloc[[i]].reset_index()
    @staticmethod               
    def Crime_map():
        data= pd.read_csv('C:\\Users\\dell\\crimeproject\\crime1.csv')
        st.sidebar.title("Choose the state")
        select=st.sidebar.selectbox('State',options=df["STATE/UT"])
        obj=crime.search_group(select,data)
        obj.drop(['Unnamed: 0','index'], axis = 1,inplace=True)
        obj['avg'] = pd.to_numeric(obj[["Rape","Kidnapping and Abduction","Dowry Deaths","Assault on women with intent to outrage her modesty","Insult to modesty of Women","Cruelty by Husband or his Relatives","Importation of Girls"]].mean(axis=1))
        st.write(obj)
        loc=[]
        loc.append(obj.loc[0,"latitude"])
        loc.append(obj.loc[0,"longitde"])
        m = folium.Map(location=loc, zoom_start=16)
        value=str(obj['avg'])
        folium.Marker(location=loc,popup='See the average number of crimes happening per year '+' WITH '+str(value)+' CRIMES PER YEAR',tooltip='<strong>Click here to see Popup</strong>',icon=folium.Icon(color='red',icon='none')).add_to(m)

        #if int(obj.iloc[0]['avg'])>0 and int(obj.iloc[0]['avg'])<2000:
            #folium.Marker(location=loc,popup='MODERATELY UNSAFE ZONE'+' WITH '+str(value)+' CRIMES PER YEAR',tooltip='<strong>Click here to see Popup</strong>',icon=folium.Icon(color='blue',icon='none')).add_to(m)
        #elif int(obj.iloc[0]>4000) and int(obj.iloc[0])<10000:
            #folium.Marker(location=loc,popup='SAFE'+' WITH '+str(value)+' CRIMES PER YEAR',tooltip='<strong>Click here to see Popup</strong>',icon=folium.Icon(color='green',icon='none')).add_to(m)
        #else:
            #folium.Marker(location=loc,popup='DANGEROUS ZONE'+' WITH '+str(value)+' CRIMES PER YEAR',tooltip='<strong>Click here to see Popup</strong>',icon=folium.Icon(color='red',icon='none')).add_to(m)
        folium_static(m)
    @staticmethod
    def Crime_bar():
        data= pd.read_csv('C:\\Users\\dell\\crimeproject\\crimes_against_women_2001-2014 (2).csv')
        data.drop(['Unnamed: 0','DISTRICT'], axis = 1,inplace=True)
        data.dropna(axis=1,inplace=True)
        data["STATE/UT"]=data["STATE/UT"].apply(lambda x: x.upper())
        group=data.groupby('STATE/UT',as_index=False)["Rape","Kidnapping and Abduction","Dowry Deaths","Assault on women with intent to outrage her modesty","Insult to modesty of Women","Cruelty by Husband or his Relatives","Importation of Girls"].mean()
        #st.title("Number of rape cases per year")
        st.markdown("<h2 style='text-align:left; color:Black;'><b><center>NUMBER OF RAPE CASES PER YEAR </center></b></h2>",unsafe_allow_html=True)
        fig1 = px.bar(group, x="STATE/UT", y="Rape",color="STATE/UT")
        st.plotly_chart(fig1)  
       #st.write("<h2 style='text-align:left; color:Tomato;'><b>It is showing the number of rape cases per year of state of india. </b></h2>",unsafe_allow_html=True)  
        st.write("<h2 style='text-align:left; color:Tomato;'><b>Despite being the capital of the country, it is clearly visible that Delhi has the highest number of rape cases per year thus making it an unsafe place for women to grow and flourish.<br>This forms a barrier to late night work schedules, coachings etc hence affecting the functioning of daily lives of females unlike males.</b></h2>",unsafe_allow_html=True) 
        #st.title("Kidnapping and Abduction cases per year")
        st.markdown("<h2 style='text-align:left; color:Black;'><b><center>KIDNAPPING AND ABDUCTION CASES PER YEAR </center></b></h2>",unsafe_allow_html=True)
        fig2 = px.bar(group, x="STATE/UT", y="Kidnapping and Abduction",color="STATE/UT")
        st.plotly_chart(fig2)
       #st.write("<h2 style='text-align:left; color:Tomato;'><b>It is showing the Kidnapping and Abduction cases per year of state of india. </b></h2>",unsafe_allow_html=True)  
        st.write("<h2 style='text-align:left; color:Tomato;'><b>Delhi again has the highest cases of female kidnapping and abductions per year making it an unconducive place for women to move in the city which ultimately affects their education, workforce participation and efficiency too. <br> For proper functioning of a human it is important that they are free from fear of safety but unfortunately this is not the condition with women in the capital of the country and some other states too like Uttar Pradesh, Assam etc.</b></h2>",unsafe_allow_html=True)
        #st.title("Dowry deaths per year")
        st.markdown("<h2 style='text-align:left; color:Black;'><b><center>DOWRY DEATHS PER YEAR </center></b></h2>",unsafe_allow_html=True)
        fig3 = px.bar(group, x="STATE/UT", y="Dowry Deaths",color="STATE/UT")
        st.plotly_chart(fig3)
        #st.write("<h2 style='text-align:left; color:Tomato;'><b>It is showing the Dowry deaths per year of state of india. </b></h2>",unsafe_allow_html=True)  
        st.write("<h2 style='text-align:left; color:Tomato;'><b>Now coming to the most discussed topic in the Indian society <b>Marriage</b>. As it can be seen clearly that Uttar Pradesh, Telangana, Bihar and Andhra Pradesh stands highest among the number of dowry deaths happening in the country per year.<br> If a women is not safe in the hands of her husband and his family then obviously this creates an inequality in the society against women which is not even existent for males in the country.Also, this is a consequence of lack of education and financial independence.</b></h2>",unsafe_allow_html=True)
       # st.title("Assault on women with intent to outrage her modesty per year")
        st.markdown("<h2 style='text-align:left; color:Black;'><b><center>ASSUALT ON WOMEN WITH INTENT TO OUTRAGE HER MODESTY PER YEAR </center></b></h2>",unsafe_allow_html=True)
        fig4 = px.bar(group, x="STATE/UT", y="Assault on women with intent to outrage her modesty",color="STATE/UT")
        st.plotly_chart(fig4)
        st.write("<h2 style='text-align:left; color:Tomato;'><b>It is showing the  Assault on women with intent to outrage her modesty per year of state of india. </b></h2>",unsafe_allow_html=True)  
        #st.title("Cruelty by Husband or his Relatives per year")
        st.markdown("<h2 style='text-align:left; color:Black;'><b><center>CRUELTY BY HUSBAND OR HIS RELATIVES PER YEAR</center></b></h2>",unsafe_allow_html=True)
        fig5 = px.bar(group, x="STATE/UT", y="Cruelty by Husband or his Relatives",color="STATE/UT")
        st.plotly_chart(fig5)
        st.write("<h2 style='text-align:left; color:Tomato;'><b>It is showing the Cruelty by Husband or his Relatives per year of state of india. </b></h2>",unsafe_allow_html=True)  
        




if select1=="Education" and select2!="Choose the type of visualisation you want to see":
    obj=education()
    obj.literacy_rate(select2)
    obj.high_schooledu(select2)
    obj.primary_edu(select2)
    obj.GPI_primary(select2)
    obj.GPI_secondary(select2)
elif select1=="Workforce" and select2!="Choose the type of visualisation you want to see":
    obj=Workforce()
    obj.wagensalaries(select2)
    obj.ratio_labourforce(select2)
    obj.labourforce(select2)
elif select1=="Crime" and select3!="Choose the type of visualisation you want to see":
    obj=crime()
    if select3=="Map style":
        obj.Crime_map()
    else:
        obj.Crime_bar()



