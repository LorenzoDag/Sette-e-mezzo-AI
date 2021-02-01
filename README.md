# Sette e mezzo AI

Nella cartella “sette_e_mezzo_DTProblog” sono contenuti tutti i files relativi al progetto.  
Si necessita di una versione python 3.8, dei moduli pyswip e problog ed una versione dell’interprete swi-prolog 8.2.  
Tuttavia nelle altre due cartelle sono presenti due versioni differenti di immagini Docker customizzate per l’esecuzione del programma stesso. Le due immagini differiscono in quanto una presenta al suo interno la cartella contenente il progetto, per cui creando un container da quell’imagine si può subito giocare, mentre l’altra contiene solo le dipendenze necessarie al funzionamento dell’applicazione.

### <a id="sem_immagineeseguibile_6"></a>sem_immagine-eseguibile

Questa cartella contiene il Dockerfile e la relativa immagine contenuta nel file .tar in grado di eseguire da subito l’applicazione.  
Per poter caricare l’immagine aprire un prompt dei comandi, muoversi all’iterno della cartella in questione e digitare il comando:

    $ docker load -i sette-e-mezzo_eseguibile.tar

Una volta terminato il caricamento dell’immagine è possibile creare il container digitando:

    $ docker run -it --name [nome-container] sette-e-mezzo_eseguibile

A questo punto partirà la versione semplificata del gioco da noi implementata.

Una volta stoppato, per runnare il container digitare:

    $ docker start -i [nome-container]

NOTA: -i è importante per rendere il container interattivo.

### <a id="sem_immaginebase_24"></a>sem_immagine-base

Questa cartella contiene il Dockerfile e la relativa immagine contenuta nel file .tar contenente unicamente le dipendenze necesarie allo sviluppo dell’applicazione.  
Come prima bisogna caricare l’immagine muovendoci nella cartella sem_immagine-base e digitando il comando:

    $ docker load -i sette-e-mezzo_base.tar

A questo punto è possibile creare un contenitore “montando” al suo interno la cartella del progetto che manterrà le modifiche apportate fuori dal contenitore.  
Per fare ciò muoversi all’interno della cartella principale (progetto_AI) e lanciare il comando:

    $ docker run -d -it --name [nome-container] -v "$(pwd)/sette_e_mezzo_DTProblog:/progetto_AI/[path]" sette-e-mezzo_base

In questo modo le modifiche apportate ai file saranno visibili anche all’interno del container.

NOTA: nel Dockerfile è stata settata la WORKDIR alla cartella “progetto_AI” per cui è consigliabile “montare” la cartella del progetto all’interno di questa directory.

A questo punto per eseguire l’applicazione all’interno del container appena creato:

    $ docker exec -ti [nome-container] bash

Questo comando aprirà una bash all’interno del container attraverso la quale potremmo esplorare il suo file system.  
In particolare:

    $ cd [path]
    $ python main.py

eseguirà l’applicazione all’interno del container.
Implementazione semplificata del gioco di carte "Sette e mezzo" in cui il ruolo del mazziere viene ricoperto da un'intelligenza artificiale sviluppata in sw-prolog e problog
