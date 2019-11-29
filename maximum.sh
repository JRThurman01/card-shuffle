awk 'BEGIN {max=0} $4 > max && NR > 1 {max=$4} END {print max}'  'result2019-11-23 19:09:36.656860.csv'

