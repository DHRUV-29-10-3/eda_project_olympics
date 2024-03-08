import pandas as pd

df = pd.read_csv('athlete_events.csv')
region_df = pd.read_csv('noc_regions.csv')


def process():
    global df,region_df
    df = df[df['Season'] == 'Summer']
    new_df = df.merge(region_df,on = 'NOC', how = 'left')
    new_df.drop_duplicates(inplace = True)
    new_df = pd.concat([new_df,pd.get_dummies(new_df['Medal']).astype(int)],axis = 1)
    new_df = new_df[new_df['Year'] != 1906]
    new_df['total'] = new_df['Gold']+new_df['Silver']+new_df['Bronze']
    new_df.drop_duplicates(subset=['Team', 'NOC', 'Games', 'Year', 'Season', 'City', 'Sport', 'Event', 'Medal'],inplace = True)

    new_df.dropna(subset=['region'], inplace=True)

    return new_df


def process2():
    global df, region_df
    df = df[df['Season'] == 'Summer']
    new_df = df.merge(region_df, on='NOC', how='left')
    new_df.drop_duplicates(inplace=True)
    new_df = pd.concat([new_df, pd.get_dummies(new_df['Medal']).astype(int)], axis=1)
    new_df = new_df[new_df['Year'] != 1906]
    new_df['total'] = new_df['Gold'] + new_df['Silver'] + new_df['Bronze']
    new_df.drop_duplicates(subset=['Name','Team', 'NOC', 'Games', 'Year', 'Season', 'City', 'Sport', 'Event', 'Medal'],
                           inplace=True)

    return new_df

def process3():
    global df, region_df
    df = df[df['Season'] == 'Summer']
    new_df = df.merge(region_df, on='NOC', how='left')
    new_df.drop_duplicates(inplace=True)
    new_df = pd.concat([new_df, pd.get_dummies(new_df['Medal']).astype(int)], axis=1)
    new_df = new_df[new_df['Year'] != 1906]
    new_df['total'] = new_df['Gold'] + new_df['Silver'] + new_df['Bronze']
    new_df.drop_duplicates(subset=['Name', 'Team', 'NOC', 'Games', 'Year', 'Season', 'City', 'Sport', 'Event', 'Medal'],
                           inplace=True)

    sport_count = new_df['Sport'].value_counts().reset_index()
    sport_count = sport_count.query('count>1000')

    return sport_count