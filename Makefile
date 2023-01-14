lint:
	poetry run flake8 brain_games

brain-games:
	poetry run brain-games

brain-even:
	poetry run brain-even

brain-calc:
	poetry run brain-calc

build:
	poetry build

publish:
	poetry publish --dry-run


#Установка пакета из Операционной Системы (добавим --user после install)
package-install:
	python3 -m pip install dist/*.whl

package-uninstall:
	python3 -m pip uninstall hexlet-code


