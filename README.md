# DoS-attacker
## ❕ Atenção
* Não ataque sites privados. isso é ilegal.

## 🖥️ Pré-requisitos
* Ultima versão do `Python3`.
para verificar isto, é bem simples. Basta digitar:

```powershell
python --version
```

## ☕ Utilização
`Clone` o repositorio usando:

```
git clone https://github.com/DioBruh/Dos-Attack/
```

`Navegue` até a pasta do scanner utilizando:

```
cd tools-hacking
```

```
cd dos
```

`Usage:`

```
python dos.py --help 
```

```powershell
usage: dos.py [-h] [--http [HTTP ...]] [-i [IP]] [-p PORT] [-s SOCKETS]

optional arguments:
  -h, --help            show this help message and exit
  --http [HTTP ...]     Attack https://<host>
  -i [IP], --ip [IP]    Host to attack.
  -p PORT, --port PORT  Port of webserver, usually 80
  -s SOCKETS, --sockets SOCKETS
                        Number of sockets to use in the test
```

#### Uso para ip. 

```cmd
python dos.py --ip <ip> -p <port> -s 500
```

#### Em outro terminal, abra um ping no ip que está atacando.

### Windows

```bat
ping <ip> -t
```

### Linux
```bash
ping <ip> 
```



### Uso para site.

```cmd
python dos.py --http <web_site> -p <port> -s 500
```

A porta padrão é: 80<br>
O número de socks padrão é: 150

Existem 2 modos possiveis para os ataques.
* IP attack. (para atacar ip)
* WebSite attack. (para atacar sites, esse funciona melhor)
