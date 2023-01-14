import numpy as np
from constants import Constants


# TODO: импорт Nm из файла с зависимостью от частоты + поддержка этой фичи в коде

# параметры в СГС
class InputVariables:
    #### Input ####

    N0: float = 1e10  # концентрация свободных носителей заряда

    m: float = 1  # масса свободных носителей заряда в массах свободного электрона

    Gamma0: float = 30  # затухание колебаний свободного заряда

    eps_inf: float = 2  # диэлектрическая проницаемость для частот много больше фотонных

    freq_max: float = 4500  # макс частота

    freq_min: float = 100

    # n: int = 100 # количество точек

    K: int = 2  # количество мод связанных зарядов

    d: float = 100  # толщина плёнки d (в сантиметрах). ВАЖО: ПОЛЬЗОВАТЕЛЬ ВВОДИТ В НАНОМЕТРАХ. УМНОЖАЕМ ВВОД НА 1E-7

    Nm: np.complex64 = 1 + 0j  # комплексный показатель преломления среды за плёнкой

    N_air: np.complex64 = 1 + 0j  # комплексный показатель преломления воздуха

    Ni: np.array = np.zeros(K)  # концентрация свободных носителей заряда

    mi: np.array = np.ones(
        K)  # масса связанного носителя заряда. ВАЖНО: ПОЛЬЗОВАТЕЛЬ ЗАДАЕТ В А.Е.М. НУЖНО ДОМНОЖИТЬ ВВОД НА 1.66E-24

    ei: np.array = np.ones(
        K)  # эффективный заряд в зарядах электрона. ВАЖНО: ПОЛЬЗОВАТЕЛЬ ЗАДАЕТ В ГОВНЕ. НУЖНО ДОМНОЖИТЬ ВВОД НА 4.8E-10

    vi: np.array = np.ones(K) * 1100  # частота колебаний связанного заряда (в обратных сантиметрах)

    Gamma_i: np.array = np.ones(K) * 30  # затухание колебаний связанного заряда (в обратных сантиметрах)

    N = 1000

    def get_freqs(self):
        return np.linspace(self.freq_min, self.freq_max, self.N)

    def get_d(self):
        return self.d * 1e-7

    def get_m(self):
        return self.m * Constants.m0

    def get_mi(self):
        return self.mi * 1.66 * 1e-24

    def get_ei(self):
        return self.ei * 4.8 * 1e-10


# Все функции считают в СГС, однако пользователь задает величины фиг знает в чем, нужно сперва их все перевести

# Плазменная частота свободных колебаний
# возвращает float - частоту в СГС (TODO: нужно перевести в обратные сантиметры)
# принимаемые величины задаются пользователем
# N0 - концентрация свободных носителей заряда, в СГС.
# eps_inf - диэлектрическая проницаемость для частот много больше фотонных
def plasma_freq_of_free_oscillations(N0: float, eps_inf: float, m: float):
    return Constants.e / (2 * np.pi * Constants.c) * np.sqrt(4 * np.pi * N0 / (m * eps_inf))


# все плазменные частоты для связных зарядов
# все принимаемые величины задаются пользователем
# ei - массив зарядов для каждой моды
# Ni - концентрация свободных носителей зарядов для каждой моды
# mi - масса масса свзанного носителя заряда для каждой моды
# eps_inf - диэлектрическая проницаемость для частот много больше фотонных
# возвращает массив частот
def plasma_freq_of_connected_charges(ei: np.array, Ni: np.array, mi: np.array, eps_inf: float):
    dim = ei.size
    assert (dim == Ni.size and mi.size == dim)
    return ei / (2 * np.pi * Constants.c) * np.sqrt(4 * np.pi * Ni / (3 * mi * eps_inf))


# диэлектрическая проницаемость от частоты
# freq_p0 считается функцией plasma_freq_of_free_oscillations
# freq_pi считается функцией plasma_freq_of_connected_charges
# vi - частота колебаний связн заряда, задается пользователем
# Gamma0 (Г0 из задания) - затухание колебаний свободного заряда, задается пользователем
# Gamma_i (Гi из задания) - затухание колебаний связного заряда, задается пользователем
# eps_inf - диэлектрическая проницаемость для частот много больше фотонных, задается пользователем
# v - частота, аргумент функции (хз откуда берется)
# возращает float - значение диэоектрической проницаемости
def dielectric_from_freq(freq_p0: float, freq_pi: np.array, vi: np.array, Gamma0: float, Gamma_i: np.array,
                         eps_inf: float, v: np.array):
    # TODO: знаменатель в сумме. Там мнимая единица или номер??

    func = lambda x: eps_inf * (1 - freq_p0 ** 2 / (x ** 2 + x * Gamma0 * 1j) + np.sum(
        freq_pi ** 2 / (vi ** 2 - x ** 2 - x * Gamma_i * 1j)))
    vect = np.vectorize(func)
    return vect(v)


# N(v) - показатель преломления
# возвращает реальную и мнимую части
# epsilon = dielectric_from_freq
def N_from_freq(epsilon: np.array):
    N = np.sqrt(epsilon)
    return N


# коэффициент поглощения
# v - частоты
# k - мнимая часть N(v)
def alpha_from_freq(v: np.array, k: np.array):
    return 4 * np.pi * v * k


# оптическая плотность пленки
# d -толщина пленки
def optical_Density(alpha: np.array, d: float):
    return alpha * d


# комплексный коэф отражения по амплитуде воздух-пленка
# N_air - показ преломл воздуха
# N_v - N(v) - показ преломления
def r12(N_air: np.complex64, N_v: np.array):
    up = -N_v + N_air
    down = N_air + N_v
    return up / down


# компл коэф отр по ампл пленка - среда
# N_m - показ преломл среды
def r23(N_v: np.array, N_m: float):
    up = N_v - N_m
    down = N_v + N_m
    return up / down


# коэф отраж по интенсивнойсти
def R(r: np.array):
    # return np.abs(r)**2
    return np.abs(r) ** 2  # r*np.conj(r)


# набег фазы
def delta(n_v: np.array, d: float):
    return 2 * d * n_v


# пропускание пленки
def T(R12: np.array, R23: np.array, alpha: np.array, d: float, v: np.array, delta: np.array):
    up = (1 - R12) * (1 - R23) * np.exp(-alpha * d)
    down_1 = 1 + R12 * R23
    down_2 = 2 * np.sqrt(R12 * R23) * np.exp(-2 * alpha * d) * np.cos(delta * v)
    return up / (down_1 + down_2)


# оптическая плотность пленки с учетом интерференции
def A(T: np.array):
    return -np.log(T)


def normalize(values: np.array):
    up = (values - np.min(values))
    down = (np.max(values) - np.min(values))
    if down == 0:
        return values / np.max(values)
    return up / down


def set_mins_maxes_dict(minsDict: dict, maxesDict: dict, mins: np.array, maxes:np.array):
    for i in range(1,12):
        minsDict[i] = mins[i-1]
        maxesDict[i] = maxes[i-1]

#
# def get_mins_maxes(plotData: dict):
#     mins = np.zeros(11)
#     maxes = np.zeros(11)
#     for i in range(1,12):
#         min,max = getMinMax(plotData[i][1])
#         mins[i-1] = min
#         maxes[i-1] = max
#     return mins, maxes
#
# def get_global_min_max(mins: np.array, maxes: np.array):
#     return np.min(mins), np.max(maxes)
#
# def getMinMax(idxData):
#     return np.min(idxData), np.max(idxData)
