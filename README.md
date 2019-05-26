# Analiza Danych Maturalnych
Projekt ma na celu analizę danych zawierających liczbę osób, które przystąpiły/zdały egzamin maturalny, pochodzących ze strony https://dane.gov.pl/dataset/1567/resource/17363. Zawierają one informacje pochodzące z lat 2010-2018 dla wszystkich polskich województw, oraz zbiorcze dla całego kraju. 

## Uruchamianie skryptu
W celu rozpoczęcia korzystania ze skrytpu, należy pobrać folder ```Scripts``` a następnie uruchomić w konsoli plik ```myscript.py```.

### Dostępne komendy
* Nazwy wszystkich województw należy wpisywać wielką literą.

```average``` - dla podanego roku oraz województwa pozwala na obliczenie średniej liczby osób, które przystąpiły do egzaminu dla danego województwa na przestrzeni lat, do podanego roku włącznie.

```pass_rate_for_province```- pozwala na obliczenie procentowej zdawalności dla danego województwa na przestrzeni lat.

```best_province``` - umożlwia znalezienie województwa o największej zdawalności dla podanego roku.

```regression_detection``` - pozwala na wykrycie województw, które zanotowały regresję (mniejszy współczynnik zdawalności w kolejnym roku), jeżeli takowe znajdują się w zbiorze.

```province_compare``` - dla dwóch podanych województw oblicza, które z nich miało lepszą zdawalność na przestrzeni lat.

###
