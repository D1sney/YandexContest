import sys

def main():
    input = sys.stdin.readline
    n = int(input())
    apps = []  # MRU-список: apps[0] — текущее активное
    for _ in range(n):
        s = input().rstrip('\n')
        parts = s.split(maxsplit=1)
        cmd = parts[0]
        if cmd == "Run":
            # Если нет имени приложения, берём пустую строку
            name = parts[1] if len(parts) > 1 else ""
            apps.insert(0, name)      # O(n)
            print(name)
        else:
            # Переключение Alt+Tab...
            k = s.count("Tab")
            cnt = len(apps)
            if cnt == 0:
                # Нет ни одного запущенного приложения — пропускаем
                continue
            idx = k % cnt             # 0-based
            name = apps.pop(idx)      # O(n)
            apps.insert(0, name)      # O(n)
            print(name)

if __name__ == "__main__":
    main()
