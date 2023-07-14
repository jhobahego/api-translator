# api-translator
Backend de FastApi que conecta con la api de openai para traducir un texto y usarla en el [frontend](https://github.com/jhobahego/google-translate-clone)

## Uso de la api
```
git clone https://github.com/jhobahego/api-translator.git

cd api-translator

pip install -r requirements.txt

uvicorn main:app
```

## Requisitos
Debes definir un archivo .env dentro de la carpeta del proyecto con la [apikey de openai](https://platform.openai.com/account/api-keys)
```env
OPENAI_API_KEY="your-api-key"
```

## Recomendaciones
- Ide [pycharm](https://www.jetbrains.com/pycharm/download/?section=windows)
- Formateador PEP8
