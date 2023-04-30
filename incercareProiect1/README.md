# _Abordare Proiect_

## Cerinta
1. Server-ul asculta pachetele venite pe adresa de
loopback a subretelei pe un anumit port si tine o lista cu
toti clientii activi; 

2. Clientii cand pornesc trimit un pachet pe adresa de loopback si portul pe care asculta server-ul prin care se inregistreaza in lista clientilor activi;
3. Fiecare aplicatie client deschide un port pe care asteapta cereri de procesare, la inregistrarea cu server-ul comunicandu-i acest port; 
4. Inainte de inchidere, aplicatia client trimite un mesaj pe adresa de loopback si portul pe care asculta server-ul pentru stergerea clientului din lista clientilor activi;
5. Server-ul asculta pe un port cereri de procesare de la clienti care constau in executia unui task custom furnizat la momentul cererii impreuna cu argumentele de apel, rezultatul executiei intors de server clientului constand in exit code-ul executiei task-ului;
6. La primirea unui task de procesare, server-ul alege urmatorul client de procesare la rand, ii trimite pe portul de procesare codul binar al task-ului si argumentele de apel, clientul de procesare lansand in executie task-ul primit in local cu argumentele date, intorcand dupa terminarea executiei exit code-ul procesului care a rulat task-ul, care este apoi trimit de server clientului ce a solicitat excutia task-ului respectiv.
***

**Abodare** - modul in care voi incerca sa rezolv pasii proiectului enuntat mai sus

- conexiune o voi face de tip tcp
- voi implementa si tcp tunneling; din modul in care sunt formulate 2 si 3 trebuie tcp tunneling



