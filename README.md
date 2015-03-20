# ocr-placas-mexico

Repo para pruebas de OCR con placas de México usando openalpr (https://github.com/openalpr/openalpr)

Instalar openalpr en Ubuntu:

```
wget -O - http://deb.openalpr.com/openalpr.gpg.key | sudo apt-key add -
echo "deb http://deb.openalpr.com/master/ openalpr main" | sudo tee /etc/apt/sources.list.d/openalpr.list
sudo apt-get update
sudo apt-get install openalpr openalpr-daemon openalpr-utils libopenalpr-dev
```
Probar con placas de México:

```python prueba_reconocimiento.py```

