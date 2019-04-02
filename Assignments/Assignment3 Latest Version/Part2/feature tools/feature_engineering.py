import featuretools as ft
import pandas as pd

loan = pd.read_csv('csv/loan_info.csv')
person = pd.read_csv('csv/person.csv')

es = ft.EntitySet(id='data')
es = es.entity_from_dataframe(entity_id='loan', dataframe=loan, index='id')
es = es.entity_from_dataframe(entity_id='person', dataframe=person, index='id')

relationship = ft.Relationship(es['loan']['id'], es['person']['id'])
es = es.add_relationship(relationship)
print(es)

features, feature_names = ft.dfs(entityset=es, target_entity='loan', max_depth=2)
print(features)

features.to_csv('csv/featuretools_result.csv')
