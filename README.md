# simple_cli
A Simple Command Line Interactive Sample Code

![](screen.gif)

Generate key:
```python3
>>> import hashlib
>>> m = hashlib.sha1()

>>> a = '4d06afae5bd24751b148cb02f23ab6d2'
>>> a += 'oaZADXDzb2aY16H3o2aFEA=='
>>> m.update(a.encode('utf-8'))
>>> m.hexdigest()
'23b24155fe34b4c2a5bcc15379d8e83efbc9c7f2'
```
AES CBC key iv:
```
key: +iZ+17kxM3HS/s8g9Nyr4g==
iv: mNPogOSSY79BRifl2T1S7g==
```