Para executar: uvicon \workout_api.main:app --reload
Se o programa estiver na pasta raiz: uvicon main:app --reload

Outra forma
Crie o arquivo Makefile
insira este conteúdo:

    run:
	    @uvicorn workout_api.main:app --reload

No prompt de comando, execute: make run