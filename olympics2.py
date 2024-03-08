import streamlit as st
import preprocessor, helper
import pandas as pd
import plotly.express as px
import seaborn as sns
import matplotlib.pyplot as plt
import scipy as sp
import plotly.figure_factory as ff

df = preprocessor.process()
df1 = preprocessor.process2()
df2 = preprocessor.process3()

# Create a sidebar with a dropdown menu

image = open('565-5652007_olympic-lessons-for-better-health-transparent-background-olympic.png', 'rb').read()
st.sidebar.image(image)
st.sidebar.header('Olympic Analysis')
selected_value = st.sidebar.selectbox(
    'Select an option:',
    ['Medal Tally', 'Overall Analysis', 'Country-wise Analysis', 'Athlete-wise Analyis'])


if selected_value == 'Medal Tally':

    df_year = df['Year'].unique().tolist()
    df_year.sort()
    df_year.insert(0, 'overall')
    Year = st.sidebar.selectbox('Select the Year:', df_year)

    df_region = df['region'].unique().tolist()
    df_region.sort()
    df_region.insert(0, 'overall')
    Country = st.sidebar.selectbox(
        'Select the Country:', df_region
    )

    if Country == 'overall' and Year == 'overall':
        original_title = '<p style="font-family:Courier; color:#ADD8E6;font-size:40px;">Overall Data</p>'
        st.markdown(original_title, unsafe_allow_html=True)
        medal = helper.medal_tally(df)
        st.dataframe(medal)

    elif Year != 'overall' and Country == 'overall':
        st.header(f'Olympic data of {Year}')
        answer = helper.year(df, Year)
        st.dataframe(answer)

    elif Year == 'overall' and Country != 'overall':
        st.subheader(f'Olympic data of {Country}')
        answer1 = helper.Country_performance(df, Country)
        st.dataframe(answer1)

    else:
        st.header(f'Olympic data of {Country} in {Year}')
        answer2 = helper.year_country(df, Year, Country)
        st.dataframe(answer2)

if selected_value == 'Overall Analysis':
    Top_stats = '<p style="font-family:Courier; color:#90EE90;font-size:40px;">Top Statistics</p>'
    st.markdown(Top_stats, unsafe_allow_html=True)

    editions = df['Year'].nunique()
    City = df['City'].nunique()
    Events1 = df['Event'].nunique()
    Sports1 = df['Sport'].nunique()
    athletes = df1['Name'].nunique()
    nations = df['region'].nunique()

    col1,col2,col3 = st.columns(3)
    with col1 :
        Editions = '<p style="font-family:Courier; color:#FFDAB9;font-size:25px;">Editions:</p>'
        st.markdown(Editions, unsafe_allow_html=True)
        st.subheader(editions)

    with col2:
        Hosts = '<p style="font-family:Courier; color:#FFDAB9;font-size:25px;">Hosts:</p>'
        st.markdown(Hosts, unsafe_allow_html=True)
        st.subheader(City)

    with col3:
        Sports = '<p style="font-family:Courier; color:#FFDAB9;font-size:25px;">Sports:</p>'
        st.markdown(Sports, unsafe_allow_html=True)
        st.subheader(Sports1)

    col4, col5, col6 = st.columns(3)
    with col4:
        Events = '<p style="font-family:Courier; color:#FFDAB9;font-size:25px;">Events:</p>'
        st.markdown(Events, unsafe_allow_html=True)
        st.subheader(Events1)

    with col5:
        Nations = '<p style="font-family:Courier; color:#FFDAB9;font-size:25px;">Nations:</p>'
        st.markdown(Nations, unsafe_allow_html=True)
        st.subheader(nations)

    with col6:
        Athletes = '<p style="font-family:Courier; color:#FFDAB9;font-size:25px;">Athletes:</p>'
        st.markdown(Athletes, unsafe_allow_html=True)
        st.subheader(athletes)

    data = helper.nations_over_time(df)


    Nations_Over_Time = '<p style="font-family:Courier; color:#90EE90;font-size:40px;">Nations Over Time</p>'

    st.markdown(Nations_Over_Time, unsafe_allow_html=True)
    dataset = data
    fig = px.line(dataset, x="Year", y="region")
    fig.update_layout(width=800, height=600)
    st.plotly_chart(fig)

    data = helper.event_over_time(df)

    Event_over_time = '<p style="font-family:Courier; color:#90EE90;font-size:40px;">Events Over Time</p>'
    st.markdown(Event_over_time, unsafe_allow_html=True)
    dataset = data
    fig = px.line(dataset, x="Year", y="Event")
    fig.update_layout(width=800, height=600)
    st.plotly_chart(fig)


    n_dataset = df1['Sport'].unique().tolist()
    n_dataset.sort()
    n_dataset.insert(0,'overall')
    Best_athlete = '<p style="font-family:Courier; color:#90EE90;font-size:40px;">Best Athletes Data</p>'
    st.markdown(Best_athlete, unsafe_allow_html=True)

    Sport = st.selectbox(
        'Select an option:', n_dataset)

    if Sport == 'overall':
        best_athlete = helper.best_athlete(df1)
        best_athlete = best_athlete.reset_index().drop_duplicates(subset=['Sport']).reset_index(drop=True)
        st.dataframe(best_athlete)

    else:
        best_athlete = helper.best_athletes_sport(df1,Sport)
        st.dataframe(best_athlete)


if selected_value == 'Country-wise Analysis':
    Country = '<p style="font-family:Courier; color:#FFC0CB;font-size:40px;">Country-Wise Analysis</p>'
    st.markdown(Country, unsafe_allow_html=True)
    countries = df['region'].unique().tolist()
    country = st.selectbox('Select an option:',
    countries)
    st.subheader(f'{country} Medal Tally')

    database1 = helper.country_medal(df, country)
    database1 = database1.reset_index()
    fig = px.line(database1, x="Year", y="total")
    st.plotly_chart(fig)
    st.subheader(f'Top 10 best athlete of {country}')

    database2 = helper.best_athlete_country(df1, country)
    st.dataframe(database2)

    st.subheader(f'{country} total medal count in following years')

    heat_map_data = helper.heat_map_medal_country(df, country)
    fig,ax = plt.subplots(figsize=(25, 25))

    ax = sns.heatmap(heat_map_data.pivot_table(index='Sport', columns='Year', values='total', aggfunc='count').fillna(0),
                annot=True)

    st.pyplot(fig)


if selected_value == 'Athlete-wise Analyis':
    athlete_wise = '<p style="font-family:Courier; color:#FFA500 ;font-size:40px;">Athlete-wise Analyis</p>'
    st.markdown(athlete_wise, unsafe_allow_html=True)

    athlete_df = df.drop_duplicates(subset=['Name', 'region'])
    x1 = athlete_df['Age'].dropna()
    x2 = athlete_df[athlete_df['Medal'] == 'Gold']['Age'].dropna()
    x3 = athlete_df[athlete_df['Medal'] == 'Silver']['Age'].dropna()
    x4 = athlete_df[athlete_df['Medal'] == 'Bronze']['Age'].dropna()
    fig = ff.create_distplot([x1, x2, x3, x4],
                             ['Age Distribution', 'Gold medalist', 'Silver medalist', 'Bronze medalist'],
                             show_hist=False, show_rug=False)
    st.subheader('Distribution Of Age wrt Sports')
    fig.update_layout(autosize = False,width = 700,height = 600,xaxis_title = 'Age')
    st.plotly_chart(fig)

    st.subheader('Distribution Of Age wrt Sports(Gold Medalist)')
    famous_sport_list = df2['Sport'].tolist()
    famous_sport_list = sorted(famous_sport_list)
    sport = st.selectbox('Select the option :', famous_sport_list)
    dataset3 = helper.sport_age_distribution(athlete_df,sport)
    fig1 = ff.create_distplot([dataset3[dataset3['Medal'] == 'Gold']['Age'].dropna()], [sport],
                             show_hist=False, show_rug=False)

    st.plotly_chart(fig1)

    st.subheader('Scatter Plot of weight-height distribution')
    sport2 = st.selectbox('Select an option:', famous_sport_list)
    dataset4 = helper.weight_height_distribution(df1, sport2)
    fig, ax = plt.subplots(figsize=(10, 10))

    ax = sns.scatterplot(data = dataset4, x = 'Weight', y = 'Height', hue = 'Medal', style = 'Sex')

    st.pyplot(fig)
    st.subheader("Male-Female data over years")
    dataset5 = helper.male_female_distribution(df1)
    fig3 = px.line(dataset5, x="Year", y=["F", "M"])
    fig3.update_layout(width=800, height=600)
    st.plotly_chart(fig3)





















