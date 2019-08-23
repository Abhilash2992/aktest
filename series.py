import databricks.koalas as ks

df = ks.DataFrame({'a': [1, 2, 3, 4, 4, 3, 2, 1],
                           # 'a': pd.Categorical([1, 2, 3, 4, 4, 3, 2, 1]),
                           'b': list('abcdabcd'),
                           # 'c': pd.Categorical(list('abcdabcd')),
                           'c': list('abcdabcd')})

