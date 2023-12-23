# Dataset
dataset = [
    ['Skirt', 'Sneakers', 'Scarf', 'Pants', 'Hat'],
    ['Sunglasses', 'Skirt', 'Sneakers', 'Pants', 'Hat'],
    ['Dress', 'Sandals', 'Scarf', 'Pants', 'Heels'],
    ['Dress', 'Necklace', 'Earrings', 'Scarf', 'Hat', 'Heels', 'Hat'],
    ['Earrings', 'Skirt', 'Skirt', 'Scarf', 'Shirt', 'Pants']
]




import mlxtend
import pandas as pd
from mlxtend.preprocessing import TransactionEncoder
from mlxtend.frequent_patterns import apriori, association_rules



# Convert the dataset to a one-hot encoded DataFrame
te = TransactionEncoder()
te_ary = te.fit(dataset).transform(dataset)
df = pd.DataFrame(te_ary, columns=te.columns_)



from mlxtend.frequent_patterns import apriori
apriori(df, min_support=0.5)


# Apply Apriori algorithm to find frequent itemsets
frequent_itemsets = apriori(df, min_support=0.2, use_colnames=True)
frequent_itemsets



# Generate association rules
rules = association_rules(frequent_itemsets, metric="confidence", min_threshold=0.7)
# Print the association rules
print(rules)


import csv

with open('Market_Basket_Optimisation.csv', newline='') as f:
    reader = csv.reader(f)
    data = list(reader)

print(data)

te=TransactionEncoder()
te_ary=te.fit(data).transform(data)    
data=pd.DataFrame(te_ary, columns=te.columns_)  
data




from mlxtend.frequent_patterns import apriori
apriori(data, min_support=0.01)


frequent_itemsets=apriori(data, min_support=0.01, use_colnames=True) 
frequent_itemsets



from mlxtend.frequent_patterns import association_rules 
rules_ap=association_rules(frequent_itemsets,metric="confidence",min_threshold=0.2)



result = pd.DataFrame(rules_ap)
result.sort_values(by='lift',inplace=True,ascending=False)
result.head(-5)






