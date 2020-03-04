# mini_privacy_in_big_data

This is a mini project based on the article "A Practical Approximation Algorithm for Optimal k-Anonymity".

index :
A - preliminaries
B - main libraries
C - how to run
D - outline of implementation
E - folder structure
F - modules explanation


***A***
preliminaries :

Programming language used - python version 3.6
Operating system used - linux ubuntu 18.04

***B***
main libraries :
-regular expressions(re)
-_functools
-system specific parameters and functions(sys)
-tkinter
-unittest

***C***
how to run :
from within mini_privacy_in_big_data folder - 
in order to run tests one should execute the following command through shell:
$>> ./runtest.sh

in order to run the actual program which is run by the gui one should execute the following command through shell:
$>> ./rungui.sh

note:
one might need to give execution permissions for the above executables in order for them to run - 
$>> chmod +x ./runtests.sh
$>> chmod +x ./rungui.sh
 
***D***
outline of implementation :

The main algorithm in the article to obtain k-anonymity is Algorithm 5(page 13):

Algorithm 5 k-ANON-CF
k -anonymization via set-cover using closed frequent generalized records

Input: Table D, integer k.
Output: Table g(D) that satisfies k−anonymity

1: Find all closed generalized records that have support of size at least k in D (Algorithm 6).
2: Set F_CF to be the set of supports of all the found closed frequent generalized records.
3: Produce a cover γ of D, by using Algorithm 4, with F CF as an input.
4: Convert the resulting [k, 2k − 1]-cover γ into a [k, 2k − 1]-clustering, γ0 , by invoking Algorithm 2
5: Output the k-anonymization g(D) of D that corresponds to γ0 .

explanation :

step 1 is done by module mini.algorithm_6_7 
step 2 is done by module mini.algorithm_6_7 implicitly
step 3 is done by module mini.algorithm_4
step 4 is done by module mini.algorithm_2
step 5 is done by module mini.k_anon

The database on which this algorithm works on is :
Adult Database -
Predicting whether income exceeds $50K/yr base
d on census data. 
48842 instances, 14 attributes (6 continuous and 8 nominal) 

Example for a possible(because there is a random component in the algorithm ) output for the first 3000 records is in file "generalized_database.txt" - 
one can see that not all 3000 records are in the above file and thats because the article does not support partial data for a record - and the missing records are with partial data viewed as "?"(question mark).

Algorithm 6 needs as one of its inputs a list of taxonomies of the database for which k anonymization is needed.
those taxonomies where written by hand and are in module mini.taxonomies.
these were written in a similar way to what was done in the article in pages 23-24.

and the taxonomies for the numeric attributes will replace the written static ones dynamically during runtime.

In short the way this algorithm(algorithm 5) works is based on theorem 1 from page 8 :

Theorem 1 
Let α ≥ 1 , and let γ be a [k, 2k − 1] -clustering with cost at most α times that
of an optimal solution to the [k, 2k − 1] -minimum clustering problem. Then if we replace
each record R ∈ D with the closure of the cluster in γ to which it belongs, we obtain a
2α− approximation to the optimal k -anonymization problem.

and on the monotonicity assumption on the cost function and on lemma 1 from page 7(sub additivity of cost function on 2 intersecting datasets).

outline of the proof presented in page 10 for correctness of the algorithm(5) is that algorithm 4 produces an approximated cover with cost alpha times than that of the optimal , then algorithm 2 unifies intersecting subsets which does not increase cost by lemma 1 or remove a record from a subset which does not increase cost by monotonicity.
then by theorem 1 the k-anonimization is of factor alpha from the optimal.

***E***
folder structure :

mini_privacy_in_big_data folder

	--rungui.sh
	--runtests.sh
	--mini_Src
		----generalized_database.txt
		----README.md
		----algorithm_2.py
		----algorithm_4.py
		----algorithm_6_7.py
		----k_anon.py
		----main.py
		----helper_funcs.py
		----hierarchical_clustering.py
		----make_int_taxonomies.py
		----taxonomies.py
		
		----test_algorithm_2.py
		----test_algorithm_4.py
		----test_algorithm_6_7.py
		----test_helper_funcs.py
		----test_hierarchical_clustering.py

		----result_dbs
		----dbs
			------adult.data
            ------test_db_cover_1
			------test_db_multiple_2.txt
			------test_db_clothing.txt
			------test_db_helper.txt
			------test_db_multiple.txt

***F*** 
modules explanation :

taxonomies.py - this module contains the taxonomies for each database that the program supports k anonimization for
hierarchical_clustering.py - this module implements the single linkage clustering algorithm for the numerical quasi identifiers
make_int_taxonomies.py - the actual building of the numerical taxonomies

algorithm_6_7.py - implementation of algorithms 6,7 in pages 18,19 from the article 
algorithm_4.py - implementation of algorithm 4 in page 13 from the article
algorithm_2.py - implementation of algorithm 2 in page 9 in from article
k_anon.py - implementation of k anonimization from a clustering by the idea presented in article "k-anonymization with minimal loss of information" by Tamir Tassa in page 19
main.py - implementation of algorithm 5 in page 13 from the article , also implements the gui of the program
helper_funcs.py - this module contains the helper functions used in algorithm_6_7.py , algorithm_4.py and k_anon.py

the following are test modules for the corresponding modules above :
test_algorithm_2.py , test_algorithm_4.py , test_algorithm_6_7.py , test_helper_funcs.py , test_hierarchical_clustering.py


