all: scripts 

scripts: check
	test -e $@ || ln -s ../src/scripts/* .

check:
	true

clean:
	-rm *.pl *.py *.gp fastsubs dists scode wkmeans wordsub
