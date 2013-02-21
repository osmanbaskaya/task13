### 1. GENERAL SETUP

### 1.1 BIN INSTALLATION
bin:
	cd ../bin; make

### 1.2 COMMON OPTIONS
SRILM_PATH=/opt/srilm/bin/i686-m64
export PATH := ../../bin:.:${SRILM_PATH}:${PATH} # Binaries in the bin directory
SEED=1  # Random seed
NCPU=7 # Number of threads/processes to use for parallel computations

DATA=../data/tokenized/
### 1.3 INPUT files:
TRAIN=${DATA}train.ukwac.tok.gz # ukWaC Corpus wc=88214600 2247153469 12385653002
TEST=${DATA}test.ukwac.tok.gz  # ukWaC Test Corpus wc= 39203 998193 5509360


### 2. COMMON FILES

### 2.1 GOLD answers:

#wsj.words.gz: ${GOLD}  ## time=1s, wc=1173766 1173766 6412448
	#zcat $< | perl -lane 'print $$F[0] if /\S/' | gzip > $@

#wsj.pos.gz: ${GOLD}  ## time=1s, wc=1173766 1173766 3793947
	#zcat $< | perl -lane 'print $$F[1] if /\S/' | gzip > $@

### 2.2 SRILM options:
LM_NGRAM=4# n-gram order
LM_VOCAB=100 # words seen less than this in GETTRAIN will be replaced with <unk>
LM_MTYPE=i686-m64 # architecture for compiling srilm

ukwac.split: #splitting data into training and test for perplexity calc.
	../bin/data_splitter.py

#TODO: Time ve wc'ler daha duzeltilmedi
ukwac.tokenize: ## time=1h30m, wc=88214600 2247153469 12385653002
	tokenize.py

trial.all.gz: trial.gz trial.ngram.gz trial.gold.gz trial.pos.gz trial.word.gz trial.id.gz
	

trial.tok.gz: ../trial
	../bin/trial_data_parser.py | gzip > $@

#TODO prepare.% #training/test
trial.gz: ../trial/data/semeval-2013-task-10-trial-data.xml
	../bin/trial_data_parser.py | gzip > $@

trial.ngram.gz: trial.gz
	zcat $< | cut -f2 | gzip > $@

trial.gold.gz: trial.gz
	zcat $< | cut -f3 | gzip > $@

trial.pos.gz: trial.gz
	zcat $< | perl -lane 'print $$F[2]' | gzip > $@
	
trial.word.gz: trial.gz
	zcat $< | perl -lane 'print $$F[1]' | gzip > $@

trial.id.gz: trial.gz
	zcat $< | perl -lane 'print $$F[0]' | gzip > $@

%.vocab.gz: ${DATA}%.tok.gz  ## LM_VOCAB=100: time=2219s wc=672335 672009 5983977
	#awk '{if ($2 >= 20) {print $0}}' | gzip > $@
	zcat $< | ngram-count -write-order 1 -text - -write - | awk '{if ($$2 >= ${LM_VOCAB}) {print $1}}' | gzip > $@ 
	#zcat $< | ngram-count -write-order 1 -text - -write - | \
	#perl -lane 'print $$F[0] if $$F[1] >= ${LM_VOCAB}' | gzip > $@

ukwac.lm.gz: ukwac.vocab.gz ${TRAIN}
	zcat ${TRAIN} | ngram-count -order ${LM_NGRAM} -kndiscount -interpolate -unk -vocab $< -text - -lm $@

ukwac.ppl.gz: 
	#zcat $*.tok.gz | \
	#ngram -order ${LM_NGRAM} -unk -lm $< -ppl - -debug 2 | gzip > $@
	zcat ${TEST} | ngram -order ${LM_NGRAM} -unk -lm ukwac.lm${LM_NGRAM}.gz -ppl - -debug 2 | gzip > $@

trial.ppl.gz:
	zcat trial.tok.gz | ngram -order ${LM_NGRAM} -unk -lm ukwac.lm${LM_NGRAM}.gz -ppl - -debug 2 | gzip > $@


### 2.3 FASTSUBS options:
FS_NSUB=100 # go until you have this many substitutes
FS_PSUB=1.0 # or this much cumulative probability
FS_OPTIONS=-n ${FS_NSUB} -p ${FS_PSUB}

%.sub.gz: %.ngram.gz ukwac.lm4.gz  ## FS_NSUB=100 FS_PSUB=1 
	zcat $< | fastsubs ${FS_OPTIONS} | grep -P '^__XX__\t' | gzip > $@
