import os
import ctypes
from screeninfo import get_monitors


# Функция для изменения заголовка консоли
def set_console_title(title):
    ctypes.windll.kernel32.SetConsoleTitleW(title)

set_console_title("SM: WOS BUILDER")

# Получение частоты экрана через Windows API
def get_screen_refresh_rate():
    class DEVMODE(ctypes.Structure):
        _fields_ = [
            ("dmDeviceName", ctypes.c_wchar * 32),
            ("dmSpecVersion", ctypes.c_ushort),
            ("dmDriverVersion", ctypes.c_ushort),
            ("dmSize", ctypes.c_ushort),
            ("dmDriverExtra", ctypes.c_ushort),
            ("dmFields", ctypes.c_ulong),
            ("dmOrientation", ctypes.c_short),
            ("dmPaperSize", ctypes.c_short),
            ("dmPaperLength", ctypes.c_short),
            ("dmPaperWidth", ctypes.c_short),
            ("dmScale", ctypes.c_short),
            ("dmCopies", ctypes.c_short),
            ("dmDefaultSource", ctypes.c_short),
            ("dmPrintQuality", ctypes.c_short),
            ("dmColor", ctypes.c_short),
            ("dmDuplex", ctypes.c_short),
            ("dmYResolution", ctypes.c_short),
            ("dmTTOption", ctypes.c_short),
            ("dmCollate", ctypes.c_short),
            ("dmFormName", ctypes.c_wchar * 32),
            ("dmLogPixels", ctypes.c_short),
            ("dmBitsPerPel", ctypes.c_ulong),
            ("dmPelsWidth", ctypes.c_ulong),
            ("dmPelsHeight", ctypes.c_ulong),
            ("dmDisplayFlags", ctypes.c_ulong),
            ("dmDisplayFrequency", ctypes.c_ulong),
            ("dmICMMethod", ctypes.c_ulong),
            ("dmICMIntent", ctypes.c_ulong),
            ("dmMediaType", ctypes.c_ulong),
            ("dmDitherType", ctypes.c_ulong),
            ("dmReserved1", ctypes.c_ulong),
            ("dmReserved2", ctypes.c_ulong),
            ("dmPanningWidth", ctypes.c_ulong),
            ("dmPanningHeight", ctypes.c_ulong)
        ]

    ENUM_CURRENT_SETTINGS = -1
    devmode = DEVMODE()
    devmode.dmSize = ctypes.sizeof(DEVMODE)
    if ctypes.windll.user32.EnumDisplaySettingsW(None, ENUM_CURRENT_SETTINGS, ctypes.byref(devmode)):
        return devmode.dmDisplayFrequency
    return 60  # fallback

# Получение количества ядер CPU
def get_cpu_cores():
    return os.cpu_count() or 4  # fallback

# Получение разрешения вручную
def get_resolution_from_user():
    res_input = input("Введите ваше разрешение экрана в формате ШИРИНА, ВЫСОТА (например, 1920, 1080): ")
    try:
        width, height = [x.strip() for x in res_input.split(",")]
        return width, height
    except ValueError:
        print("❌ Ошибка: Введите разрешение строго в формате '1920, 1080'")
        exit(1)

# Получение разрешения автоматически
def get_auto_resolution():
    monitor = get_monitors()[0]
    return str(monitor.width), str(monitor.height)

# Получение частоты монитора вручную
def get_refresh_rate_from_user():
    refresh_rate_input = input("Введите частоту экрана в герцах (например, 60): ")
    try:
        refresh_rate = int(refresh_rate_input.strip())
        return refresh_rate
    except ValueError:
        print("❌ Ошибка: Введите частоту экрана корректно")
        exit(1)

# Получение количества ядер процессора вручную
def get_cpu_cores_from_user():
    cpu_cores_input = input("Введите количество потоков процессора (например, 8): ")
    try:
        cpu_cores = int(cpu_cores_input.strip())
        return cpu_cores
    except ValueError:
        print("❌ Ошибка: Введите количество потоков корректно")
        exit(1)

# ==== Основной запуск ====
print("Выберите способ установки значений:")
print("1 - Использовать автоматическое определение всех значений")
print("2 - Ввести все значения вручную")
choice = input("Введите 1 или 2: ").strip()

if choice == "1":
    # Автоматическое определение значений
    set_console_title("SM: WOS BUILDER - ВЫБОР РЕЖИМА")
    print("Автоматическое определение значений...")
    
    width, height = get_auto_resolution()
    set_console_title("SM: WOS BUILDER - ФИНИШ")
    print(f"Автоопределено: {width}x{height}")
    
    refresh_rate = get_screen_refresh_rate()
    print(f"Автоопределена частота экрана: {refresh_rate} Hz")
    
    cpu_cores = get_cpu_cores()
    print(f"Автоопределено количество ядер: {cpu_cores}")
    
elif choice == "2":
    # Ручной ввод значений
    set_console_title("SM: WOS BUILDER - ВЫБОР РАСШИРЕНИЯ ЭКРАНА")
    print("Ввод данных вручную...")
    
    width, height = get_resolution_from_user()
    
    set_console_title("SM: WOS BUILDER - ВЫБОР КОЛИЧЕСТВА ПОТОКОВ")
    refresh_rate = get_refresh_rate_from_user()
    
    set_console_title("SM: WOS BUILDER - ВЫБОР ЧАСТОТЫ ДИСПЛЕЯ")
    cpu_cores = get_cpu_cores_from_user()
    
else:
    print("❌ Неверный выбор")
    exit(1)

# XML-шаблон
xml_content = f'''<?xml version="1.0" encoding="utf-8"?>
<r>
\t<s id="Version">7</s>
\t<s id="VideoDesiredW">0</s>
\t<s id="VideoDesiredH">0</s>
\t<s id="VideoVSync">1</s>
\t<s id="VideoParticles">1</s>
\t<s id="VideoShadows">1</s>
\t<s id="VideoPostProcFx">1</s>
\t<s id="MouseSens">50</s>
\t<s id="ActionLeft">286</s>
\t<s id="ActionRight">288</s>
\t<s id="ActionForward">273</s>
\t<s id="ActionBackward">287</s>
\t<s id="ActionSuit">314</s>
\t<s id="ActionWallCrawl">272</s>
\t<s id="ActionWallSprint">274</s>
\t<s id="ActionTarget">271</s>
\t<s id="ActionSwing">525</s>
\t<s id="ActionJump">313</s>
\t<s id="ActionShoot">300</s>
\t<s id="ActionAttack">524</s>
\t<s id="ActionWebStrike">302</s>
\t<s id="ActionUpgrades">289</s>
\t<s id="ActionAllyPrev">459</s>
\t<s id="ActionAllyNext">461</s>
\t<s id="ActionAllySummon">464</s>
\t<s id="ActionAllyDismiss">456</s>
\t<s id="ActionCenterCamera">526</s>
\t<s id="VideoW">{width}</s>
\t<s id="VideoH">{height}</s>
\t<s id="Windowed">0</s>
\t<s id="MaxCpuCount">{cpu_cores}</s>
\t<s id="VideoHz">{refresh_rate}</s>
\t<s id="MouseMinSens">0.00075</s>
\t<s id="MouseMaxSens">0.00025</s>
</r>
'''

# Создание и сохранение файла
folder_path = os.path.join(os.environ["USERPROFILE"], "AppData", "Local", "Activision", "Spider-Man Web of Shadows")
os.makedirs(folder_path, exist_ok=True)
file_path = os.path.join(folder_path, "Config.xml")

with open(file_path, "w", encoding="utf-8") as f:
    f.write(xml_content)

# Финальное сообщение
print(f"\n💾 Новые данные сохранены.")
print(f"🖼 Разрешение: {width}x{height}")
print(f"💻 Потоков CPU: {cpu_cores}")
print(f"📈 Частота экрана: {refresh_rate} Hz")

# Ожидаем нажатия клавиши, чтобы консоль не закрылась
input("\nНажмите любую клавишу для выхода...")
