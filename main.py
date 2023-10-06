import numpy as np
import matplotlib.pyplot as plt
import matplotlib

matplotlib.use('TkAgg')
# гармонический


def generate_harmonic_signal(frequency, duration, sampling_rate):
    t = np.arange(0, duration, 1 / sampling_rate)
    signal = np.sin(2 * np.pi * frequency * t)
    return t, signal


# цифровой
def generate_square_wave(frequency, duration, sampling_rate):
    t = np.arange(0, duration, 1 / sampling_rate)
    signal = np.sign(np.sin(2 * np.pi * frequency * t))
    return t, signal


def compute_spectrum(signal, sampling_rate):
    spectrum = np.fft.fft(signal)
    frequencies = np.fft.fftfreq(len(signal), 1 / sampling_rate)
    return frequencies, spectrum


#Параметры
frequencies = [1, 2, 4, 8]
duration = 1.0
sampling = 1000

plt.figure(figsize=(14, 8 * len(frequencies)))

for idx, frequency in enumerate(frequencies, 1):

    t_harmonic, harmonic_signal = generate_harmonic_signal(frequency, duration, sampling)

    t_square, square_signal = generate_square_wave(frequency, duration, sampling)

    freq_harmonic, spectrum_harmonic = compute_spectrum(harmonic_signal, sampling)
    freq_square, spectrum_square = compute_spectrum(square_signal, sampling)

    freq_harmonic_positive = freq_harmonic[freq_harmonic >= 0]
    spectrum_harmonic_positive = np.abs(spectrum_harmonic[freq_harmonic >= 0])
    freq_square_positive = freq_square[freq_square >= 0]
    spectrum_square_positive = np.abs(spectrum_square[freq_square >= 0])

    plt.subplot(len(frequencies), 4, idx * 4 - 3)
    plt.plot(t_harmonic, harmonic_signal, color='green')
    plt.title(f"Гармонический сигнал {frequency} Гц")
    plt.xlabel('Время (сек)')
    plt.ylabel('Амплитуда')

    plt.subplot(len(frequencies), 4, idx * 4 - 2)
    plt.plot(freq_harmonic_positive, spectrum_harmonic_positive, color='green')
    plt.title(f"Спектр гармонического сигнала {frequency} Гц")
    plt.xlabel('Частота (Гц)')
    plt.ylabel('Амплитуда')
    plt.xlim(0, 15)

    plt.subplot(len(frequencies), 4, idx * 4 - 1)
    plt.plot(t_square, square_signal, color='green')
    plt.title(f"Цифровой сигнал {frequency} Гц")
    plt.xlabel('Время (сек)')
    plt.ylabel('Амплитуда')

    plt.subplot(len(frequencies), 4, idx * 4)
    plt.plot(freq_square_positive, spectrum_square_positive, color='green')
    plt.title(f"Спектр цифрового сигнала {frequency} Гц")
    plt.xlabel('Частота (Гц)')
    plt.ylabel('Амплитуда')
    plt.xlim(0, 15)

plt.subplots_adjust(wspace=0.5, hspace=0.5)
plt.show()