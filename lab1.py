"""
Лабораторная работа 1. Основы работы с языком Python
Интеллектуальный анализ данных (Data Mining)
"""


# ==========================================
# Задание 1 (Task 1)
# ==========================================

def task1_process(input_string: str, char: str):
    """
    Ізделетін символға дейінгі ішкі жолды және оның ұзындығын қайтарады.
    Егер символ табылмаса, None қайтарады.

    Возвращает подстроку до указанного символа и её длину.
    Если символ не найден, возвращает None.
    """
    if not char:
        return None
    index = input_string.find(char)
    if index != -1:
        substring = input_string[:index]
        return substring, len(substring)
    return None


def run_task1():
    print("--- Задание 1 ---")
    s = input("Строканы (жолды) енгізіңіз: ")
    c = input("Ізделетін символды (әрiптi) енгізіңіз: ")

    result = task1_process(s, c)
    if result is not None:
        substring, length = result
        print(f"1. Введенный символге дейінгі белгілер (Символы до '{c}'): '{substring}'")
        print(f"2. Алынған жолдың ұзындығы (Длина полученной строки): {length}")
    else:
        print(f"Қате/Сообщение: '{c}' символы жолда табылмады (Символ не встретился в строке).")


# ==========================================
# Задание 2 (Task 2)
# ==========================================

def task2_process(initials: str, birth_day: int):
    """
    Латын алфавиті тізімін жасап, оны біртіндеп өзгертеді:
    1. Аты-жөнінің бастапқы әріптерін өшіру.
    2. Басына 'The truncated Latin Alphabet: ' жолын қосу.
    3. Соңына 0-ден N-ге дейінгі сандарды қосу (N - туған күн).

    Создает список латинского алфавита и последовательно меняет его.
    """
    # Латын алфавитін for циклімен толтыру
    latin_alphabet = []
    for code in range(ord('a'), ord('z') + 1):
        latin_alphabet.append(chr(code))

    history = [("Бастапқы тізім (Исходный список):", list(latin_alphabet))]

    # 1. Инициалдарды өшіру (бас және кіші әріптер ескеріледі)
    initials_lower = [ch.lower() for ch in initials if ch.isalpha()]
    latin_alphabet = [ch for ch in latin_alphabet if ch not in initials_lower]
    history.append((f"1. Инициалдар ('{initials}') өшірілгеннен кейін:", list(latin_alphabet)))

    # 2. Басына жол вставка жасау
    header = 'The truncated Latin Alphabet: '
    latin_alphabet.insert(0, header)
    history.append((f"2. Басына '{header}' вставка жасалғаннан кейін:", list(latin_alphabet)))

    # 3. Соңына 0-ден N-ге дейін сандар қосу
    for i in range(birth_day + 1):
        latin_alphabet.append(i)
    history.append((f"3. Соңына 0-ден N={birth_day}-ге дейін сандар қосылғаннан кейін:", list(latin_alphabet)))

    return latin_alphabet, history


def run_task2():
    print("\n--- Задание 2 ---")
    initials = input("Аты, тегі және әкесінің атының бастапқы әріптерін енгізіңіз (мысалы, АФО): ")
    try:
        birth_day = int(input("Туған күніңізді енгізіңіз (N сандық күн): "))
    except ValueError:
        print("Қате: Туған күн сан болуы керек!")
        return

    final_list, history = task2_process(initials, birth_day)
    for title, lst in history:
        print(title)
        print(lst)


# ==========================================
# Задание 3 (Task 3)
# ==========================================

def MinInt(A: list, N: int) -> int:
    """
    N өлшемді A бүтін сандар тізіміндегі минимумды табады.
    Находит минимум в целочисленном списке A размера N.
    """
    if len(A) != N:
        raise ValueError(f"Тізім өлшемі {len(A)} берілген N={N} мәніне сәйкес емес!")
    if N == 0:
        raise ValueError("Тізім бос болмауы тиіс!")
    min_val = A[0]
    for val in A:
        if val < min_val:
            min_val = val
    return min_val


def MaxFloat(A: tuple, N: int) -> float:
    """
    N өлшемді A нақты сандар кортежіндегі максимумды табады.
    Находит максимум в кортеже вещественных чисел A размера N.
    """
    if len(A) != N:
        raise ValueError(f"Кортеж өлшемі {len(A)} берілген N={N} мәніне сәйкес емес!")
    if N == 0:
        raise ValueError("Кортеж бос болмауы тиіс!")
    max_val = A[0]
    for val in A:
        if val > max_val:
            max_val = val
    return max_val


def Invert(A: list, N: int) -> list:
    """
    N өлшемді A тізімінің элементтер ретін кері өзгертеді.
    Меняет порядок элементов списка A размера N на обратный.
    """
    if len(A) != N:
        raise ValueError(f"Тізім өлшемі {len(A)} берілген N={N} мәніне сәйкес емес!")
    left = 0
    right = N - 1
    while left < right:
        A[left], A[right] = A[right], A[left]
        left += 1
        right -= 1
    return A


def run_task3():
    print("\n--- Задание 3 ---")
    print("1. MinInt функциясын 3 тізімге қолдану:")
    for i in range(1, 4):
        try:
            n = int(input(f"  A{i} тізімінің өлшемін (N{i}) енгізіңіз: "))
            raw_input = input(f"  A{i} үшін {n} бүтін санды бос орын арқылы енгізіңіз: ").split()
            a_list = [int(x) for x in raw_input]
            if len(a_list) != n:
                print(f"  Қате: Еңгізілген элементтер саны ({len(a_list)}) N{i}={n} мәніне тең емес!")
                continue
            min_elem = MinInt(a_list, n)
            print(f"  -> A{i} тізімінің минимум элементі: {min_elem}")
        except ValueError as e:
            print(f"  Қате енгізу: {e}")

    print("\n2. MaxFloat функциясын 3 кортежге қолдану:")
    for i in range(1, 4):
        try:
            n = int(input(f"  T{i} кортежінің өлшемін (N{i}) енгізіңіз: "))
            raw_input = input(f"  T{i} үшін {n} нақты санды бос орын арқылы енгізіңіз: ").split()
            a_tuple = tuple(float(x) for x in raw_input)
            if len(a_tuple) != n:
                print(f"  Қате: Еңгізілген элементтер саны ({len(a_tuple)}) N{i}={n} мәніне тең емес!")
                continue
            max_elem = MaxFloat(a_tuple, n)
            print(f"  -> T{i} кортежінің максимум элементі: {max_elem}")
        except ValueError as e:
            print(f"  Қате енгізу: {e}")

    print("\n3. Invert функциясын 3 тізімге қолдану:")
    for i in range(1, 4):
        try:
            n = int(input(f"  L{i} тізімінің өлшемін (N{i}) енгізіңіз: "))
            raw_input = input(f"  L{i} үшін {n} элементті бос орын арқылы енгізіңіз: ").split()
            if len(raw_input) != n:
                print(f"  Қате: Еңгізілген элементтер саны ({len(raw_input)}) N{i}={n} мәніне тең емес!")
                continue
            inverted = Invert(raw_input, n)
            print(f"  -> L{i} тізімінің төңкерілген реті: {inverted}")
        except ValueError as e:
            print(f"  Қате енгізу: {e}")


def main():
    print("==========================================")
    print("Лабораторная работа 1. Основы работы с Python")
    print("==========================================")
    run_task1()
    run_task2()
    run_task3()


if __name__ == "__main__":
    main()
