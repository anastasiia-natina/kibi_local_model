# kibi_local_model
voice_first_design
# SecurityEnhancedVoiceEngine (High-Assurance Edge AI Voice Control)

An implementation of a secure, local neural network voice command recognition engine of the High-Assurance Edge AI class. The project is designed according to the principles of Privacy-by-Design and Zero-Trust Architecture for use in gamified educational platforms (EdTech) and gaming applications where protecting the biometric data of users (children) is critical.

The engine completely isolates audio processing within the user's edge device (Network Air-Gap), preventing voice data leakage to cloud environments.

## Key Security Architecture Systems

*  Zero-Cloud (Complete Autonomy): Local inference powered by offline models of the Vosk neural network core (C++ Kaldi bindings). Network activity during recognition is exactly 0 bytes.

*  Model Integrity Verification: Cryptographic check of critical neural network layers using the SHA-256 algorithm before loading them into volatile memory, protecting against Model Poisoning and Tampering attacks.

*  Input Sanitization & Command Isolation (Allowlist): A strict allowlist of permitted command tokens. Any extraneous speech noise or Command Injection attempts are automatically discarded during the text filtering stage.

*  Volatile Memory Management (RAM Wiping): Forced destruction of audio data references (del audio_bytes) and resetting of internal contextual acoustic buffers (recognizer.Reset()) immediately after inference. Data Time-To-Live (TTL) in memory is ~0 ms.

## Project Structure

* EdTechModul.py — main module containing the secure voice engine and audio stream processing logic.

* benchmark.py — utility for automated performance profiling (measuring cold start time, RAM consumption, and CPU load).

* dos_simulation.py — manual threat simulation script (imitating an Audio Flooding DoS attack with a massive buffer of garbage data).

## System Requirements & Installation

### Dependencies

* **ОС:** Windows 10/11, Linux, macOS
* **Інтерпретатор:** Python 3.13+
* **Основні бібліотеки:** `vosk`, `sounddevice`, `psutil`, `numpy`

### Installation

1. Clone the repository into a local directory:
   bash
## git clone https://github.com/your-repo/kibi_local_model.git
## cd kibi_local_model

2. Install the required packages using the package manager:
   bash
## pip install vosk sounddevice psutil numpy

3. ЗDownload a local Vosk acoustic model (e.g., vosk-model-small-en-us-0.15) and place its contents into the directory specified in the initialization parameters (model_path).

## Execution Instructions

### 1. Running the Voice Engine
To start the system in standard background microphone listening mode:

   bash
## python EdTechModul.py

### 2. Performance Testing (Benchmarking)
To measure the resource footprint of the system (Cold Start and CPU utilization):

   bash
## python benchmark.py

### 3. DoS Attack Simulation (Stress Test)
To verify the resilience of the memory-wiping subsystem under anomalous loads:

   bash
## python dos_simulation.py

## Experimental Results
### Computing Resource Utilization
According to the results from the internal profiler benchmark.py, the engine demonstrates high efficiency on low-end hardware:

| Parameter | Metric Value | Characteristic |
| --- | --- | --- |
| Initialization Time (Cold Start) | 2.1270 sec | Rapid model deployment in RAM |
| Allocated Memory (RAM RSS) | 632.23 MB | Fixed constant, no memory leaks |
| Static CPU Load | < 1.0 % | Minimal background process overhead |
| Network Activity (Wireshark) | 0 bytes | Complete Network Air-Gap |

### Security Verification Matrix (STRIDE)

| Threat Type | Attack Vector | Engine Security Mechanism | Status |
| Data Leakage | Biometric interception | Local Zero-Cloud loop (Air-Gap) | SECURED |
| Model Tampering | Model Poisoning / Modification | SHA-256 blueprint validation | SECURED |
| Audio DoS | RAM buffer exhaustion | ВVolatile memory wiping (TTL 0ms) | SECURED |
| Injection | Instruction injection via voice | Token Allowlist validation | SECURED |

## Residual Risks & Limitations
1. Python Runtime Specifics (Garbage Collector): The del statement only removes the reference to an object. The physical space in RAM is cleared non-deterministically based on internal Garbage Collector algorithms, which leaves a theoretical window for Memory Dump attacks if an attacker gains root/administrator privileges on the host system.

2. Adversarial Audio Attacks: Injecting specialized ultrasonic or low-frequency noise into the audio stream can trick the Vosk neural network core into generating a valid allowlist token (e.g., jump), completely bypassing the text filtering logic. Mitigation is planned through the implementation of low-pass/high-pass spectral audio filters.