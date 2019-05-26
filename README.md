# Analiza Danych Maturalnych
<<<<<<< HEAD
Projekt ma na celu analizę danych zawierających liczbę osób, które przystąpiły/zdały egzamin maturalny, pochodzących ze strony (https://dane.gov.pl/dataset/1567/resource/17363). Zawierają one informacje zebrane w latach 2010-2018 dla wszystkich polskich województw, oraz zbiorcze dla całego kraju. 

## Uruchamianie skryptu
W celu rozpoczęcia korzystania ze skrytpu, należy pobrać folder ```Scripts``` a następnie uruchomić w konsoli plik ```myscript.py```. Do poprawnego działania programu konieczne jest aby w tym samym folderze znajdował się plik 
*Liczba_osób_które_przystapiły_lub_zdały_egzamin_maturalny.csv* 

### Dostępne komendy
**Uwagi :** 
* Nazwy wszystkich województw należy wpisywać wielką literą.
* Dla każdej z komend dostępny jest filtr, umożliwiający wybór zakresu danych: kobiet, mężczyzn oraz całego zbioru.

1. ```average``` - dla podanego roku oraz województwa pozwala na obliczenie średniej liczby osób, które przystąpiły do egzaminu dla danego województwa na przestrzeni lat, do podanego roku włącznie.

2. ```pass_rate_for_province```- pozwala na obliczenie procentowej zdawalności dla danego województwa na przestrzeni lat.

3. ```best_province``` - umożlwia znalezienie województwa o największej zdawalności dla podanego roku.

4. ```regression_detection``` - pozwala na wykrycie województw, które zanotowały regresję (mniejszy współczynnik zdawalności w kolejnym roku), jeżeli takowe znajdują się w zbiorze.

5. ```province_compare``` - dla dwóch podanych województw oblicza, które z nich miało lepszą zdawalność na przestrzeni lat.

### Testy jednostkowe
W katalogu głównym ```Scripts``` znajduje się plik ```test_for_all_data.py``` testujący metody wykonujące główne komendy dla całego zbioru danych, wykorzystując bibliotekę  *Pytest*. Do poprawnego działania programu konieczne jest aby w tym samym folderze znajdował się plik *Liczba_osób_które_przystapiły_lub_zdały_egzamin_maturalny.csv* 

### Uwagi dodatkowe
* Folder ```Data from database``` zawiera plik ```data_from_database.py```, który pozwala na jednorazowe zaimportowanie danych pochodzących z pliku *Liczba_osób_które_przystapiły_lub_zdały_egzamin_maturalny.csv* do pliku *database.sql* z wykorzystaniem biblioteki *Pandas*. Poprzez problem z dekodowaniem dane w bazie nie wyświetlają się poprawnie.
* Plik ```myscript_api.py``` znajujący się w folderze ```Data from API``` umożliwia na pobranie danych z API znajdujących się pod linkiem (https://api.dane.gov.pl/resources/17363). 
* Niestety nie udało mi się w pełni wykonać zadań bonusowych. W miarę dalszego rozwijania tego projektu, w pierwszej kolejności planuję:
    - dodać więcej testów, obejmujących wszystkie metody oraz poszczególne zbiory danych, dla każdego z dostępnyh filtrów,
    - naprawić problem z niepoprawnym dekodowaniem danych w bazie SQL oraz stworzyć metody na nich operujące,
    - przekształcić dane pobrane z API tak, aby móc zaimplementować dla nich metody znajdujące się w skrypcie.
    
=======
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
>>>>>>> 3cfc95693c6e18e7824378a45cff48be62508893
