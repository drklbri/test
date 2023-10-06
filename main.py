import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

# Функция для генерации сигнала
def generate_signal(frequency, duration, sampling_rate, signal_type="harmonic"):
    t = np.arange(0, duration, 1 / sampling_rate)
    if signal_type == "harmonic":
        signal = np.sin(2 * np.pi * frequency * t)
    elif signal_type == "square":
        signal = np.sign(np.sin(2 * np.pi * frequency * t))
    return t, signal

# Функция для вычисления спектра сигнала
def compute_spectrum(signal, sampling_rate):
    spectrum = np.fft.fft(signal)
    frequencies = np.fft.fftfreq(len(signal), 1 / sampling_rate)
    return frequencies, spectrum

# Параметры
frequencies = [1, 2, 4, 8]
duration = 1.0
sampling = 1000

# Создание сетки графиков
fig, axs = plt.subplots(len(frequencies), 2, figsize=(12, 2 * len(frequencies)))

for idx, frequency in enumerate(frequencies):
    t_harmonic, harmonic_signal = generate_signal(frequency, duration, sampling, signal_type="harmonic")
    t_square, square_signal = generate_signal(frequency, duration, sampling, signal_type="square")

    freq_harmonic, spectrum_harmonic = compute_spectrum(harmonic_signal, sampling)
    freq_square, spectrum_square = compute_spectrum(square_signal, sampling)

    # Отрисовка гармонического сигнала и его спектра
    axs[idx, 0].plot(t_harmonic, harmonic_signal, color='blue')
    axs[idx, 0].set_title(f"Гармонический сигнал {frequency} Гц")
    axs[idx, 0].set_xlabel('Время (сек)')
    axs[idx, 0].set_ylabel('Амплитуда')

    axs[idx, 1].plot(freq_harmonic, np.abs(spectrum_harmonic), color='blue')
    axs[idx, 1].set_title(f"Спектр гармонического сигнала {frequency} Гц")
    axs[idx, 1].set_xlabel('Частота (Гц)')
    axs[idx, 1].set_ylabel('Амплитуда')

    # Отрисовка цифрового сигнала и его спектра
    axs[idx + len(frequencies), 0].plot(t_square, square_signal, color='green')
    axs[idx + len(frequencies), 0].set_title(f"Цифровой сигнал {frequency} Гц")
    axs[idx + len(frequencies), 0].set_xlabel('Время (сек)')
    axs[idx + len(frequencies), 0].set_ylabel('Амплитуда')

    axs[idx + len(frequencies), 1].plot(freq_square, np.abs(spectrum_square), color='green')
    axs[idx + len(frequencies), 1].set_title(f"Спектр цифрового сигнала {frequency} Гц")
    axs[idx + len(frequencies), 1].set_xlabel('Частота (Гц)')
    axs[idx + len(frequencies), 1].set_ylabel('Амплитуда')

plt.tight_layout()
plt.show()