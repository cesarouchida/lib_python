.DEFAULT_GOAL := help

NAME = libconexaobd

help:
	@echo "make run"
	@echo "			Executa docker compose e suas dependencias"
	@echo "make clean"
	@echo "			Limpa arquivos temporarios"

run:
	docker compose up -d

clean:
	rm -rf *egg-info
	rm -rf dist
	rm -rf build
	
build: clean
	python3 setup.py sdist bdist_wheel

install: build remove_build
	pip install .

remove_build:
	pip uninstall ${NAME} -y

publish: 
	python3 setup.py sdist register -r local upload -r local

all: docker publish
	echo "Executando localmente"
	
	
