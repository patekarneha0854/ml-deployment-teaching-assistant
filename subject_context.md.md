# Subject Teaching Assistant Instructions
You are an expert academic teaching assistant for digital communication  
Your objective is to guide students step-by-step using precise pedagogical principles, technical definitions, and clear examples based strictly on the course context. Avoid hallucination and maintain a supportive tone.
# Digital Communication - Course Notes

## 1. What is Digital Communication?
Digital communication is the transfer of information (binary bits: 0s and 1s) from a transmitter to a receiver over a physical communication channel. Unlike analog communication, digital signals are discrete in time and amplitude, offering higher immunity to noise, better data security, and easier error detection/correction.

## 2. Key Elements of a Digital Communication System
* **Information Source:** Generates the original message (audio, video, text).
* **Source Encoder:** Compresses the data to remove redundancy.
* **Channel Encoder:** Adds error-correcting codes to protect data against channel noise.
* **Modulator:** Converts digital bits into analog carrier waveforms (e.g., ASK, FSK, PSK, QAM) suitable for transmission over the channel.
* **Communication Channel:** The physical medium (coaxial cable, optical fiber, wireless air).
* **Demodulator & Detector:** Recovers the carrier signals and estimates the original bits.
* **Channel Decoder & Source Decoder:** Detects/corrects errors and reconstructs the final message for the user.

Digital Communication System Block Diagram
Source -> Source Encoder -> Channel Encoder -> Digital Modulator -> Passband Channel
                                                                          |
Destination <- Source Decoder <- Channel Decoder <- Digital Demodulator <-+
Sampling and Pulse Code Modulation (PCM)To convert an analog continuous-time signal into a digital bitstream, we use the digitization process:Sampling Theorem (Nyquist-Shannon)A band-limited signal with highest frequency $f_{max}$ can be completely reconstructed from its samples if the sampling frequency $f_s$ satisfies:$$f_s \ge 2 f_{max}$$The minimum rate $f_s = 2 f_{max}$ is called the Nyquist rate.

Baseband Formatting and Line CodingLine coding maps binary bits into electrical pulses for baseband transmission.Unipolar NRZ: High level represents $1$, zero level represents $0$. Has a non-zero DC component and lacks synchronization capability for long strings of zeros or ones.Polar NRZ: Positive voltage represents $1$, negative voltage represents $0$. Reduces power consumption compared to unipolar.Bipolar (AMI - Alternate Mark Inversion):$0$ is represented by zero voltage.$1$s are represented by alternating positive and negative pulses.Property: Has no DC component and provides error detection capabilities for single errors.Manchester Coding (Bi-phase):$1$ is represented by a high-to-low transition in the middle of the bit interval.$0$ is represented by a low-to-high transition.Property: Self-clocking (contains embedded timing information), but requires twice the bandwidth of NRZ.

Matched Filter: Maximizes the Output Signal-to-Noise Ratio (SNR) at the sampling instant in the presence of Additive White Gaussian Noise (AWGN). The impulse response of a matched filter is a time-reversed and delayed version of the input signal pulse:$$h(t) = s(T - t)$$Bit Error Rate (BER): The probability that a transmitted bit is incorrectly decoded at the receiver. For BPSK in AWGN channels, the BER is expressed using the Q-function:$$P_b = Q\left(\sqrt{\frac{2E_b}{N_0}}\right)$$where $E_b$ is energy per bit and $N_0/2$ is the two-sided power spectral density of white noise.

Binary Modulation SchemesAmplitude Shift Keying (ASK): Carrier amplitude is switched between discrete levels.Phase Shift Keying (PSK): Carrier phase is shifted. In BPSK, binary $1$ is mapped to $0\degree$ and $0$ to $180\degree$.Frequency Shift Keying (FSK): Carrier frequency is switched between two discrete frequencies ($f_1$ and $f_2$).Higher-Order and Advanced ModulationQuadrature Phase Shift Keying (QPSK): Encodes $2$ bits per symbol by utilizing four phase states ($0\degree, 90\degree, 180\degree, 270\degree$).Quadrature Amplitude Modulation (QAM): Combines amplitude and phase modulation (e.g., $16$-QAM, $64$-QAM) to achieve higher spectral efficiency ($\text{bps/Hz}$).
