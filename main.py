import numpy as np
import matplotlib.pyplot as plt
import matplotlib

matplotlib.use('TkAgg')

def generate_sig(frequency, duration, sample_rate, waveform_type='harmonic'):
    time_values = np.arange(0, duration, 1 / sample_rate)
    if waveform_type == 'harmonic':
        waveform = np.sin(2 * np.pi * frequency * time_values)
    elif waveform_type == 'square':
        waveform = np.sign(np.sin(2 * np.pi * frequency * time_values))
    else:
        raise ValueError("Недопустимый тип сигнала")
    return time_values, waveform

def compute_frequency_spectrum(waveform, sample_rate):
    spectrum = np.fft.fft(waveform)
    frequencies = np.fft.fftfreq(len(waveform), 1 / sample_rate)
    return frequencies, spectrum

freq_values = [1, 2, 4, 8]
duration_time = 1.0
sample_rate = 1000

plt.figure(figsize=(14, 8 * len(freq_values)))

for idx, freq in enumerate(freq_values, 1):
    time_harmonic, harmonic_waveform = generate_sig(freq, duration_time, sample_rate, waveform_type='harmonic')
    time_square, square_waveform = generate_sig(freq, duration_time, sample_rate, waveform_type='square')

    freq_harmonic, spectrum_harmonic = compute_frequency_spectrum(harmonic_waveform, sample_rate)
    freq_square, spectrum_square = compute_frequency_spectrum(square_waveform, sample_rate)

    freq_harmonic_positive = freq_harmonic[freq_harmonic >= 0]
    spectrum_harmonic_positive = np.abs(spectrum_harmonic[freq_harmonic >= 0])
    freq_square_positive = freq_square[freq_square >= 0]
    spectrum_square_positive = np.abs(spectrum_square[freq_square >= 0])

    plt.subplot(len(freq_values), 4, idx * 4 - 3)
    plt.plot(time_harmonic, harmonic_waveform, color='green')
    plt.title(f"Сигнал {freq} Гц")
    plt.xlabel('Время (сек)')
    plt.ylabel('Амплитуда')

    plt.subplot(len(freq_values), 4, idx * 4 - 2)
    plt.plot(freq_harmonic_positive, spectrum_harmonic_positive, color='green')
    plt.title(f"Спектр сигнала {freq} Гц")
    plt.xlabel('Частота (Гц)')
    plt.ylabel('Амплитуда')
    plt.xlim(0, 15)

    plt.subplot(len(freq_values), 4, idx * 4 - 1)
    plt.plot(time_square, square_waveform, color='green')
    plt.title(f"Сигнал {freq} Гц")
    plt.xlabel('Время (сек)')
    plt.ylabel('Амплитуда')

    plt.subplot(len(freq_values), 4, idx * 4)
    plt.plot(freq_square_positive, spectrum_square_positive, color='green')
    plt.title(f"Спектр сигнала {freq} Гц")
    plt.xlabel('Частота (Гц)')
    plt.ylabel('Амплитуда')
    plt.xlim(0, 15)

plt.subplots_adjust(wspace=0.5, hspace=0.5)
plt.show()