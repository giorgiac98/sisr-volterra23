## Ripasso
In questa lezione di laboratorio vedremo come utilizzare le primitive di base delle socket per instaurare delle semplici connessioni tra client e server.

Il [modulo socket di Python](https://docs.python.org/3/library/socket.html) fornisce un'interfaccia alle API BSD(Berkeley Software Distribution UNIX, visto anche a lezione. 

Le funzioni e i metodi API socket primari in questo modulo sono:

* `socket()`
* `.bind()`
* `.listen()`
* `.accept()`
* `.connect()`
* `.connect_ex()`
* `.send()`
* `.recv()`
* `.close()`


Python fornisce un'API conveniente e coerente che mappa direttamente alle chiamate di sistema.
Facciamo giusto un refresh della sequenza delle chiamate alle API delle socket per il protocollo TCP:

![sockets-tcp-flow.webp](/home/giorgia/projects/sisr-volterra23/images/sockets-tcp-flow.webp)
[(Fonte)](https://commons.wikimedia.org/wiki/File:InternetSocketBasicDiagram_zhtw.png)