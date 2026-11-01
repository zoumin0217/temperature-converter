# converter.py
def celsius_to_fahrenheit(celsius):
    """摄氏度转华氏度"""
    return celsius * 9 / 5 + 32


def fahrenheit_to_celsius(fahrenheit):
    """华氏度转摄氏度"""
    return (fahrenheit - 32) * 5 / 9


if __name__ == "__main__":
    c = float(input("请输入摄氏温度："))
    print(f"{c}°C = {celsius_to_fahrenheit(c)}°F")
