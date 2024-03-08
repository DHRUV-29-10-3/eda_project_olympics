import pandas as pd


def medal_tally(df):
    region = df.groupby('region')

    table = region.agg(
        {
            'Gold': sum,
            'Silver': sum,
            'Bronze': sum,
            'total': sum
        }
    ).sort_values(['Gold', 'total'], ascending=False)

    return table


def year(df, Year):
    year_region = df[df['Year'] == Year].groupby('region')
    table = year_region.agg(
        {
            'Gold': sum,
            'Silver': sum,
            'Bronze': sum,
            'total': sum

        }
    ).sort_values(['Gold', 'total'], ascending=False)
    return table


def Country_performance(df, region):
    year_region = df[df['region'] == region].groupby('Year')
    table = year_region.agg(
        {
            'Gold': sum,
            'Silver': sum,
            'Bronze': sum,
            'total': sum

        }
    ).sort_values(['Gold', 'total'], ascending=False)
    return table


def year_country(df, year, country):
    year_region = df[(df['Year'] == year) & (df['region'] == country)]
    table = year_region.agg(
        {
            'Gold': sum,
            'Silver': sum,
            'Bronze': sum,
            'total': sum
        }
    )
    table = pd.DataFrame(table)
    table['Country'] = country
    table.reset_index(inplace=True)
    table.rename(columns={0: 'Medals Count'}, inplace=True)
    table = table.pivot_table(index='Country', values='Medals Count', columns='index')

    return table


def nations_over_time(df):
    data_countries_year = df.groupby('Year')['region'].nunique().reset_index()
    return data_countries_year


def event_over_time(df):
    data_event_year = df.groupby('Year')['Event'].nunique().reset_index()
    return data_event_year

def best_athletes_sport(df,sport):
    data = df[df['Sport']==sport].groupby(['Name','region']).agg(
        {
            'Gold':sum,
            'Silver':sum,
            'Bronze':sum,
            'total':sum
        }
    ).sort_values(by=['Gold','total'],ascending = False)
    return data

def best_athlete(df):

    data = df.groupby(['Sport', 'Name']).agg(
        {
            'Gold': sum,
            'Silver': sum,
            'Bronze': sum,
            'total': sum
        }
    ).sort_values(by=['Gold', 'total'], ascending=False)
    return data


def country_medal(df, country):
    data = df[df['region']==country].groupby('Year').agg(
        {
            'total':sum
        }
    )
    return data


def best_athlete_country(df, country):
    data = df[df['region'] == country].groupby(['Name', 'Sport']).agg(
        {
            'Gold': sum,
            'Silver': sum,
            'Bronze': sum,
            'total': sum,
        }
    ).sort_values(['Gold', 'total'], ascending=False).reset_index().head(10)
    return data

def heat_map_medal_country(df,country):
    temp_df = df[df['Medal'].isna() == False]
    temp_df = temp_df[temp_df['region'] == country]
    return temp_df

def sport_age_distribution(df,sport):
    temp_df = df[df['Sport'] == sport]
    temp_df[temp_df['Medal'] == 'Gold']['Age'].dropna()
    return temp_df

def weight_height_distribution(df,sport):

    df['Medal'].fillna('No Medal',inplace = True)

    data1 = df[df['Sport'] == sport]
    return data1



