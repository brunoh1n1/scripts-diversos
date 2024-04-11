## Script de Captura e Envio de Imagem via Telegram

Este script Python permite capturar uma imagem com a câmera usando fswebcam e enviar a imagem juntamente com uma mensagem para um grupo do Telegram.

# Dependências

Python 3
Biblioteca requests
Comando fswebcam
Instalação das Dependências

Certifique-se de ter o Python 3 instalado em seu sistema. Você pode instalar a biblioteca requests via pip:
´´´
pip install requests
´´´
Além disso, você precisa ter o comando fswebcam instalado em seu sistema. Você pode instalá-lo em sistemas baseados em Debian/Ubuntu com o seguinte comando:

´´´
sudo apt-get install fswebcam
´´´
# Utilização

Antes de executar o script, você precisa definir o token do seu bot do Telegram e o ID do seu grupo do Telegram nas variáveis token e chat_id, respectivamente.

´´´
token = 'seu_token_aqui'
chat_id = 'seu_chat_id_aqui'
´´´
Após definir o token e o chat ID, você pode executar o script:

´´´
python capture_and_send_telegram.py
´´´
Isso capturará uma imagem com a câmera, enviará a imagem junto com uma mensagem (contendo a data e hora do login) para o seu grupo do Telegram e exibirá uma mensagem de sucesso ou erro, conforme apropriado.

# Adicionando ao /etc/profile
Para garantir que o script seja executado automaticamente ao iniciar o sistema, adicione a seguinte linha ao final do arquivo /etc/profile:

´´´
python3 /caminho/scripts-diversos/telegram-login2.py &
´´
Certifique-se de substituir '/dados/laboratorios/scripts-diversos/telegram-login2.py' pelo caminho real do seu script.
