### 1. GENERAL SETUP

### 1.1 BIN INSTALLATION
bin:
	cd ../bin; make

### 1.2 COMMON OPTIONS
SRILM_PATH=/opt/srilm/bin/i686-m64
export PATH := ../../bin:.:${SRILM_PATH}:${PATH} # Binaries in the bin directory
SEED=1  # Random seed
NCPU=20 # Number of threads/processes to use for parallel computations

### 1.3 INPUT files:
TRAIN=../data/tokenized/ukwac-25.tok.gz # ukWaC Corpus wc=88214600 2247153469 12385653002

### 2. COMMON FILES

### 2.1 GOLD answers:

#wsj.words.gz: ${GOLD}  ## time=1s, wc=1173766 1173766 6412448
	#zcat $< | perl -lane 'print $$F[0] if /\S/' | gzip > $@

#wsj.pos.gz: ${GOLD}  ## time=1s, wc=1173766 1173766 3793947
	#zcat $< | perl -lane 'print $$F[1] if /\S/' | gzip > $@

### 2.2 SRILM options:
LM_NGRAM=4  # n-gram order
LM_VOCAB=20 # words seen less than this in GETTRAIN will be replaced with <unk>
LM_MTYPE=i686-m64 # architecture for compiling srilm

#TODO: Time ve wc'ler daha duzeltilmedi

ukwac.tokenize: # time=1h30m,
	tokenize.py


ukwac.vocab.gz: ${TRAIN}  ## LM_VOCAB=20: time=1m16s, wc=78498   78498  672284
	zcat ${TRAIN} | ngram-count -write-order 1 -text - -write - | \
	perl -lane 'print $$F[0] if $$F[1] >= ${LM_VOCAB}' | gzip > $@

ukwac.lm.gz: ukwac.vocab.gz ${TRAIN} ## LM_NGRAM=4, LM_VOCAB=20: time=6m10s, wc=27427373 118077512 847912087
	${GETTRAIN} | ngram-count -order ${LM_NGRAM} -kndiscount -interpolate -unk -vocab $< -text - -lm $@


### 2.3 FASTSUBS options:
FS_NSUB=100 # go until you have this many substitutes
FS_PSUB=1.0 # or this much cumulative probability
FS_OPTIONS=-n ${FS_NSUB} -p ${FS_PSUB}

ukwac.sub.gz: ${TEST} ukwac.lm.gz  ## FS_NSUB=100 FS_PSUB=1: time=4h47m, wc=1222974 245817774 2350067125
	zcat $< | fastsubs ${FS_OPTIONS} wsj.lm.gz | gzip > $@


