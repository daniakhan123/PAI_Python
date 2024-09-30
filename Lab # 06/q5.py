df = {
    'Year': [1987, 1986, 1985, 1990, 1991, 1992, 1993, 1994, 1995, 1996, 1997, 1998, 1999, 2000, 2001, 2002, 2003, 2004],
    'WHO_Region': ['Western Pacific', 'Americas', 'Africa', 'Europe', 'Africa', 'Americas', 'Western Pacific', 'Europe', 'Eastern Mediterranean', 'Africa', 'Americas', 
                   'Western Pacific', 'Europe', 'Africa', 'Americas', 'Western Pacific', 'Europe', 'Eastern Mediterranean'],
    'Country': ['Viet Nam', 'Uruguay', "Cte d'lvoire", 'France', 'Nigeria', 'Brazil', 'Japan', 'Germany', 'Egypt', 'Kenya', 'Argentina', 'Australia', 
                'Italy', 'Ghana', 'Chile', 'New Zealand', 'Netherlands', 'Sweden'],
    'Beverage_Types': ['Wine', 'Other', 'Wine', 'Beer',  'Wine', 'Spirits', 'Beer', 'Wine',  'Other', 'Beer', 'Spirits', 'Wine', 
                       'Beer', 'Other', 'Wine', 'Spirits', 'Beer', 'Wine'],
    'Display_Value': [0, 0.5, 1.62, 2.5,  1.8, 1.2, 2.3, 3.1,  0.9, 1.4, 1.7, 2.0,  1.5, 0.6, 1.3, 2.2,  2.1, 1.8]
}
df=pd.DataFrame(df)

Columns=list(df.columns)
print(Columns)

df.to_csv(r'Wine Consumption',index=False,header=True)
