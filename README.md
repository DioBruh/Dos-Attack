# dos-attacker

![GitHub repo size](https://img.shields.io/github/repo-size/DioBruh/tools-hacking?style=for-the-badge)
![GitHub language count](https://img.shields.io/github/languages/count/DioBruh/tools-hacking?style=for-the-badge)
![GitHub forks](https://img.shields.io/github/forks/DioBruh/tools-hacking?style=for-the-badge)
![Bitbucket open issues](https://img.shields.io/bitbucket/issues/DioBruh/tools-hacking?style=for-the-badge)
![Bitbucket open pull requests](https://img.shields.io/bitbucket/pr-raw/DioBruh/tools-hacking?style=for-the-badge)

<p>
  <img src="https://img2.gratispng.com/20180331/piw/kisspng-giant-panda-bear-pixel-art-5ac02cd75add07.0257870115225438313722.jpg"width="250px">
</p>

## ❕ Atenção
* Não ataque sites privados. isto é illegal.

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
```cmd
ping <ip> 
```



### Uso para site.

```cmd
python dos.py --http <web_site> -p <port> -s 500
```

default port is: 80<br>
default socks is: 150

Existem 2 modos possiveis para os ataques.
* IP attack.
* WebSite attack.

## 🤝 Colaboradores.
<table>
    <td align="center">
      <a href="https://github.com/DioBruh/">
        <img src="https://github.com/OnlyFalopas/falopas-painel/blob/main/devs/87872423.jpg" width="100px;" alt="Foto do DIO"/><br>
        <sub>
          <b>Dio Brando</b>
        </sub>
      </a>
    </td>
  </tr>
</table>
