import datetime
import os
from mss import mss
from mss.tools import to_png
import pyautogui

def take_screenshot(save_path='.'):
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    screenshot_filename = f"screenshot_{timestamp}.png"
    screenshot_path = os.path.join(save_path, screenshot_filename)

    with mss() as sct:
        # A biblioteca mss captura a tela como um todo, incluindo todos os monitores
        # Vamos determinar em qual monitor o cursor está e capturar apenas aquele monitor
        x, y = pyautogui.position()
        for monitor_number, monitor in enumerate(sct.monitors[1:], start=1):  # Ignora o primeiro item que é a tela completa
            if monitor["left"] <= x <= monitor["left"] + monitor["width"] and monitor["top"] <= y <= monitor["top"] + monitor["height"]:
                # O cursor está dentro dos limites deste monitor
                sct_img = sct.grab(monitor)
                to_png(sct_img.rgb, sct_img.size, output=screenshot_path)
                break
        else:
            # Se o cursor não estiver em nenhum monitor, captura a tela padrão (geralmente o primeiro monitor)
            sct_img = sct.grab(sct.monitors[1])
            to_png(sct_img.rgb, sct_img.size, output=screenshot_path)

    return screenshot_path