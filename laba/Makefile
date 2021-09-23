SMC = java -jar ./utils/Smc.jar
SMC_FLAGS = -python 

sm:
	${SMC} ${SMC_FLAGS} -d ./utils ./utils/laba1.sm 

graph:
	${SMC} -graph -d ./utils ./utils/laba1.sm

graph-create:
	dot -Tpng ./utils/laba1_sm.dot -o ./utils/laba1_graph.png

clean:
	rm -f ./utils*_sm.*