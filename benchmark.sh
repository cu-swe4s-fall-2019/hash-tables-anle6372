python hash_functions.py --input_file rand_words.txt --function ascii | python scatter.py --output_file_name ascii_hash_function.png --xlabel 'Hashed Word' --ylabel 'Hashed Value'
python hash_functions.py --input_file rand_words.txt --function rolling | python scatter.py --output_file_name rolling_hash_function.png --xlabel 'Hashed Word' --ylabel 'Hashed Value'
python hash_functions.py --input_file rand_words.txt --function asciisq | python scatter.py --output_file_name asciisq_hash_function.png --xlabel 'Hashed Word' --ylabel 'Hashed Value'
python hash_functions.py --input_file non_rand_words.txt --function ascii | python scatter.py --output_file_name ascii_hash_function_non.png --xlabel 'Hashed Word' --ylabel 'Hashed Value'
python hash_functions.py --input_file non_rand_words.txt --function rolling | python scatter.py --output_file_name rolling_hash_function_non.png --xlabel 'Hashed Word' --ylabel 'Hashed Value'
python hash_functions.py --input_file non_rand_words.txt --function asciisq | python scatter.py --output_file_name asciisq_hash_function_non.png --xlabel 'Hashed Word' --ylabel 'Hashed Value'

for M in $( seq  1000 1000 10000 ); do
    python hash_tables.py --table_size 10000 --hash_alg rolling --res_strat linear --input_file rand_words.txt --num_keys $M >  rolling_linear_rand.$M.txt
done

grep insert rolling_linear_rand.*.txt | cut -d " " -f2,3 | python scatter.py --output_file_name linear_insert_time.png --xlabel "Load factor" --ylabel "Insert time"

(for M in $( seq  1000 1000 10000 ); do
    load_factor=$(bc -l <<< "$M/10000")
    echo -n "$load_factor "
    grep search rolling_linear_rand.$M.txt | cut -d " " -f2 | python mean.py
done) | python scatter.py --output_file_name linear_search_time.png --xlabel "Load factor" --ylabel "Search time"



for M in $( seq  1000 1000 10000 ); do
    python hash_tables.py --table_size 10000 --hash_alg rolling --res_strat chain --input_file rand_words.txt --num_keys $M >  rolling_chain_rand.$M.txt
done

grep insert rolling_chain_rand.*.txt | cut -d " " -f2,3 | python scatter.py --output_file_name chain_insert_time.png --xlabel "Load factor" --ylabel "Insert time"

(for M in $( seq  1000 1000 10000 ); do
    load_factor=$(bc -l <<< "$M/10000")
    echo -n "$load_factor "
    grep search rolling_chain_rand.$M.txt | cut -d " " -f2 | python mean.py
done) | python scatter.py --output_file_name chain_search_time.png --xlabel "Load factor" --ylabel "Search time"



for M in $( seq  1000 1000 10000 ); do
    python hash_tables.py --table_size 10000 --hash_alg rolling --res_strat quadratic --input_file rand_words.txt --num_keys $M >  rolling_quadratic_rand.$M.txt
done

grep insert rolling_quadratic_rand.*.txt | cut -d " " -f2,3 | python scatter.py --output_file_name quadratic_insert_time.png --xlabel "Load factor" --ylabel "Insert time"

(for M in $( seq  1000 1000 10000 ); do
    load_factor=$(bc -l <<< "$M/10000")
    echo -n "$load_factor "
    grep search rolling_quadratic_rand.$M.txt | cut -d " " -f2 | python mean.py
done) | python scatter.py --output_file_name quadratic_search_time.png --xlabel "Load factor" --ylabel "Search time"