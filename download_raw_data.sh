# download ConceptNet
mkdir -p dataRAW/
#mkdir -p dataRAW/cpnet/
#wget -nc -P dataRAW/cpnet/ https://s3.amazonaws.com/conceptnet/downloads/2018/edges/conceptnet-assertions-5.6.0.csv.gz
#cd dataRAW/cpnet/
#yes n | gzip -d conceptnet-assertions-5.6.0.csv.gz
## download ConceptNet entity embedding
#wget https://csr.s3-us-west-1.amazonaws.com/tzw.ent.npy
#cd ../../




# download CommensenseQA dataRAWset
mkdir -p dataRAW/csqaRAW/
wget -nc -P dataRAW/csqaRAW/ https://s3.amazonaws.com/commensenseqa/train_rand_split.jsonl
wget -nc -P dataRAW/csqaRAW/ https://s3.amazonaws.com/commensenseqa/dev_rand_split.jsonl
wget -nc -P dataRAW/csqaRAW/ https://s3.amazonaws.com/commensenseqa/test_rand_split_no_answers.jsonl

# create output folders
mkdir -p dataRAW/csqaRAW/grounded/
mkdir -p dataRAW/csqaRAW/graph/
mkdir -p dataRAW/csqaRAW/statement/


#
# download OpenBookQA dataRAWset
#wget -nc -P dataRAW/obqa/ https://s3-us-west-2.amazonaws.com/ai2-website/dataRAW/OpenBookQA-V1-Sep2018.zip
#yes n | unzip dataRAW/obqa/OpenBookQA-V1-Sep2018.zip -d dataRAW/obqa/

# create output folders
#mkdir -p dataRAW/obqa/fairseq/official/
#mkdir -p dataRAW/obqa/grounded/
#mkdir -p dataRAW/obqa/graph/
#mkdir -p dataRAW/obqa/statement/
