# RDN

Obliczanie sredniej stawki cenowej netto FIXING I	dla farm PV w godzinach 5 - 16 (średni czas pracy farm) na podstawie wykresu towarowej giełdy energii cire.pl

Wersja wstępna w trakcie pracy.

Program może służyć do śledzenia cen rynkowych enrgii przed zwieraniem kontraków na odsprzedaż.

Wymagany python3

https://towarowa-gielda-energii.cire.pl/st,8,38,me,0,0,0,0,0,rynek-dnia-nastepnego.html?Day=01&Month=09&Year=2020&button=poka%BF&typ=dzien

Użycie:

python3 RDN.py  srednia dzien 28/07/2019 - obliczanie sredniej z dnia dla godzin 5-16 (Czas pracy farm PV)
python3 RDN.py  srednia miesiac 01/06/2020 - obliczanie sredniej z miesiaca (czerwiec 06/2020) dla godzin 5-16 (Czas pracy farm PV)



python3 RDN.py  srednia dzien 30/07/2019
Srednia RDN cena od 5 do 16 dnia 30/07/2019:
315.1066666666667


RDN.py  srednia miesiac 01/10/2019
Srednia RDN cen z miesiaca miedzy godzinami 5 a 16: 10/2019
237.9039247311828
