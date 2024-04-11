import requests
import datetime
import subprocess
import time

# Mensagem a ser enviada com a data e hora do login
current_datetime = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
login_message = f'Login realizado no sistema em {current_datetime}'

def capture_image():
    # Captura da imagem usando o comando fswebcam
    image_path = f"/tmp/image_{current_datetime}.jpg"
    subprocess.run(["fswebcam", "-r", "640x480", "--jpeg", "85", "-D", "1", "-S", "12", image_path])
    return image_path

def send_telegram_message(message, image_path=None):
    # Token do seu bot do Telegram
    token = 'token'
    # ID do seu grupo do Telegram
    chat_id = 'chat_id'
    
    url = f"https://api.telegram.org/bot{token}/sendPhoto"

    # Se houver um caminho de imagem fornecido, envie a foto junto com a mensagem
    if image_path:
        files = {'photo': open(image_path, 'rb')}
        response = requests.post(url, params={'chat_id': chat_id, 'caption': message}, files=files)
    else:
        params = {
            'chat_id': chat_id,
            'text': message
        }
        response = requests.post(f"https://api.telegram.org/bot{token}/sendMessage", json=params)

    if response.status_code == 200:
        print('Mensagem enviada com sucesso!')
    else:
        print(f'Erro ao enviar a mensagem. Código de status: {response.status_code}')

time.sleep(5)

# Captura da imagem
image_path = capture_image()

# Envie a mensagem com a imagem para o seu grupo do Telegram
send_telegram_message(login_message, image_path)
