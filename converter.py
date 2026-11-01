# converter.py
def celsius_to_fahrenheit(celsius):
    """摄氏度转华氏度"""
    return celsius * 9 / 5 + 32


def fahrenheit_to_celsius(fahrenheit):
    """华氏度转摄氏度"""
    return (fahrenheit - 32) * 5 / 9

def kelvin_to_celsius(kelvin):
    """开尔文转摄氏度"""
    return kelvin - 273.15


if __name__ == "__main__":
    while True:
        raw = input("请输入温度（如 25C 或 77F，输入 q 退出）：")
        if raw == "q":
            print("再见！")
            break
        unit = raw[-1].upper()
        value = float(raw[:-1])
        if unit == "C":
            print(f"{value}°C = {celsius_to_fahrenheit(value)}°F")
        elif unit == "F":
            print(f"{value}°F = {fahrenheit_to_celsius(value)}°C")
	elif unit == "K":
            print(f"{value}K = {kelvin_to_celsius(value)}°C")
        else:
            print("单位无效，请以 C 或 F 结尾")

