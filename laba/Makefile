SMC = java -jar ./utils/Smc.jar
SMC_FLAGS = -python 

sm:
	${SMC} ${SMC_FLAGS} -d ./utils ./utils/laba1.sm 

graph:
	${SMC} -graph -glevel 2 -d ./utils ./utils/laba1.sm

graph-create:
	dot -Tpng ./utils/laba1_sm.dot -o ./utils/laba1_graph.png

graph-createsvg:
	dot -Tsvg ./utils/laba1_sm.dot -o ./utils/laba1_graph.svg

clean:
	rm -f ./utils*_sm.*