
# Mastermind -Dokumentacja
 by Rafał Palinceusz
 ####https://en.wikipedia.org/wiki/Mastermind_(board_game)

 ## Założenia projektowe
Gra bazująca na znanej grze planszowej gdzie role przeciwnika przejmuje komputer. Losuje on układ 4 cyfr a gracz ma za zadanie wydedukować jakie cyfry i w jakiej kolejności. Komputer może albo podpowiadać albo oszukiwać gracza, zależnie od losowania.

## Ogólny opis kodu
Cały program zawarty jest w jednym pliku. Zgodnie z założeniem większość kodu stanowią Klasy odpowiadające za sprawdzanie rozwiązań gracza lub, celowe oszukiwanie go. Niestety z względu na ograniczone możliwości. Tryb graficzny programu jest ograniczony. Za oszukiwanie odpowiedzialny jest prosty kod losowe generujący podpowiedzi. Wpisywanie i odczytywanie danych odbywa się w wierszu poleceń, a funkcje resetu, sprawdzenia i wytknięcia oszustwa są na osobnym zestawie przycisków.

## Elementy programu

 - Program losujący 4 liczby z przedziału 1 - 6
 - Pilnowanie czy użytkownik wprowadza prawidłowe dane
 - Losowe ustawianie podpowiadania
 - Menu z możliwością wytknięcia oszustwa
 - Możliwość resetu programu i rozpoczęcia nowej rozgrywki


## Problemy
Największe problemy okazały się przy próbie utworzenia trybu graficznego dla gry, jako że kod był napisany wcześniej pod tryb tekstowy, przez co nie był odpowiednio dostosowany. Problematyczne było też zatrzymanie rozgrywki gdy użytkownik rozwiązał problem, gdzie trzeba było zastosować niezbyt eleganckie sys.exit()

## Problemy z testami
Jakkolwiek zasady gry działają poprawnie, jednakże system podpowiadania nie zawsze prawidłowo reagował na powtarzające się elementy w zestawie odpowiedzi. Trzeba go więc było sztucznie ograniczyć.


## Linki do fragmentów kodu
[Główna klasa](https://github.com/RafalPalinceusz/mastermind-projekt/blob/81e74937a4980c9ef92a4795e03a9deb55b43ed1/mastermind%20v0.9.py#L14)
 
[Tkinter window](https://github.com/RafalPalinceusz/mastermind-projekt/blob/81e74937a4980c9ef92a4795e03a9deb55b43ed1/mastermind%20v0.9.py#L117)

[rule check](https://github.com/RafalPalinceusz/mastermind-projekt/blob/81e74937a4980c9ef92a4795e03a9deb55b43ed1/mastermind%20v0.9.py#L83)

[Fair(Gamerule)](https://github.com/RafalPalinceusz/mastermind-projekt/blob/bd5ce5dbb937ab9baa72d8cc04a688dfdeff8fce/mastermind%20v1.0_MAIN.py#L21)

[Fake(Gamerule)](https://github.com/RafalPalinceusz/mastermind-projekt/blob/bd5ce5dbb937ab9baa72d8cc04a688dfdeff8fce/mastermind%20v1.0_MAIN.py#L47)

[Virtual Function](https://github.com/RafalPalinceusz/mastermind-projekt/blob/2af2c8077d89b987e406a4f13734bcdf49f5a1aa/mastermind%20v1.0_MAIN.py#L19)

[Lambda](https://github.com/RafalPalinceusz/mastermind-projekt/blob/bd5ce5dbb937ab9baa72d8cc04a688dfdeff8fce/mastermind%20v1.0_MAIN.py#L122-L125) 

# [Repozytorium](https://github.com/RafalPalinceusz/mastermind-projekt.git)
