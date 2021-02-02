# Sette e mezzo AI

Implementazione semplificata del gioco di carte "Sette e mezzo" in cui il ruolo del mazziere viene ricoperto da un'intelligenza artificiale sviluppata in sw-prolog e problog.

Nella cartella “sette_e_mezzo_DTProblog” sono contenuti tutti i files relativi al progetto.  
Si necessita di una versione python 3.8, dei moduli pyswip e problog ed una versione dell’interprete swi-prolog 8.2.  
Tuttavia nelle altre due cartelle sono presenti due versioni differenti di immagini Docker customizzate per l’esecuzione del programma stesso. Le due immagini differiscono in quanto una presenta al suo interno la cartella contenente il progetto, per cui creando un container da quell’imagine si può subito giocare, mentre l’altra contiene solo le dipendenze necessarie al funzionamento dell’applicazione.

Una volta creata una nuova cartella di progetto aprite il prompt dei comandi, muoversi all’interno della cartella in questione e digitare i comandi per clonare la repository:

    $ git init
    $ git clone https://github.com/LorenzoDag/Sette-e-mezzo-AI.git
  
  
### <a id="sem_immagineeseguibile_6"></a>sem_immagine-eseguibile

Questo cartella contiene il Dockerfile da cui si può generare l'immagine docker in grado di eseguire da subito l'applicazione.
Il Dockerfile necessita della cartella contenente il codice, per cui per costruire l'immagine bisogna copiare il Dockerfile nella directory principale.
Una volta copiato il file posizionarsi all'interno della directory principale (sette-e-mezzo-AI) e lanciare il seguente comando:

    $ docker image build . -t [nome immagine]

per versioni del client docker inferiori alla 1.13 il comando di sopra diventa:

    $ docker build . -t [nome immagine]

A questo punto è stata costruita l'immagine su cui si può istanziare un container tramite il comando :

    $ docker run -it --name [nome container] [nome immagine]

A questo punto partirà la versione semplificata del gioco da noi implementata.

Una volta stoppato, per runnare il container digitare:

    $ docker start -i [nome-container]

NOTA: -i è importante per rendere il container interattivo.

### <a id="sem_immaginebase_24"></a>sem_immagine-base

Questa cartella contiene il Dockerfile da cui si può generare l'immagine docker base, cioè contenente unicamente le dipendenze per lo sviluppo del progetto.
Per costruire l'immagine occorre posizionarsi all'interno della cartella "sem_immagine-base" e digitare il comando:
  
    $ docker image build .-t [nome immagine]

per versioni del client docker inferiori alla 1.13 il comando di sopra diventa:

    $ docker build . -t [nome immagine]

A questo punto è possibile creare un contenitore “montando” al suo interno la cartella del progetto che manterrà le modifiche apportate fuori dal contenitore.  
Per fare ciò muoversi all’interno della cartella principale (progetto_AI) e lanciare il comando:

    $ docker run -d -it --name [nome-container] -v "$(pwd)/sette_e_mezzo_DTProblog:/progetto_AI/[path]" [nome immagine]

In questo modo le modifiche apportate ai file saranno visibili anche all’interno del container.

NOTA: nel Dockerfile è stata settata la WORKDIR alla cartella “progetto_AI” per cui è consigliabile “montare” la cartella del progetto all’interno di questa directory.

A questo punto per eseguire l’applicazione all’interno del container appena creato:

    $ docker exec -ti [nome-container] bash

Questo comando aprirà una bash all’interno del container attraverso la quale potremmo esplorare il suo file system.  
In particolare:

    $ cd [path]
    $ python main.py

eseguirà l’applicazione all’interno del container.

