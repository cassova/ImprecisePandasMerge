# ImprecisePandasMerge
This will perform an imprecise merge of two pandas dataframes

### Function `imprecise_exact_merge` Example

This was created by Nicholas Miller (nmill@umich.edu) based on a bonus/fun problem proposed by Prof. Christopher Brooks (brooksch@umich.edu).

The function expects a `1:1` relationship with two datasets expected to be merged.  It uses [Levenshtein distance](https://en.wikipedia.org/wiki/Levenshtein_distance) algorithm to calculate the distance (simularity) between two words or word phrases.

"How does Levenshtein distance work? I'll leave the details to wikipedia, but essentially it is a measure of the minumum number of characters in a string of characters which must be changed in order to transform the string to a given new value. For instance, the Levenshtein distance of "U.S." when compared to "US" is 2, as you only need to remove two characters, while the comparison of "U.S." and "Canada" is 6, since many (all) of the characters need to change. There's an example of how to calculate this distance using a library in the next cell." Prof. Christopher Brooks

```
from merge import imprecise_exact_merge

new_df = imprecise_exact_merge(df1, df1, left_on='Id', right_on='Id')
```

Some future improvements:
 - support multiple columns
 - support indexes
 
In this example, we are using [faker-maker](https://github.com/cassova/Faker-Maker) to generate fake data.
