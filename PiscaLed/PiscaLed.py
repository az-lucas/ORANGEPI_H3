import OrangePi.GPIO as GPIO
import time

# Configure o modo de numeração de pinos
GPIO.setmode(GPIO.BOARD)

# Configure o pino 12 como saída
LED_PIN = 12
GPIO.setup(LED_PIN, GPIO.OUT)

try:
    while True:
        GPIO.output(LED_PIN, GPIO.HIGH) # Liga o LED
        time.sleep(1) # Espera 1 segundo
        GPIO.output(LED_PIN, GPIO.LOW) # Desliga o LED
        time.sleep(1) # Espera 1 segundo
except KeyboardInterrupt:
    # Limpa a configuração dos pinos quando o script é interrompido
    GPIO.cleanup()
