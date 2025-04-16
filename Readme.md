# 🎵 AI Music Composer

An interactive web app powered by Meta's **MusicGen** model that lets you generate original music based on **genre, mood, tempo**, and **duration**. No musical skills needed — just your creativity!

![screenshot](https://imgur.com/your-app-screenshot.png) <!-- Optional if you have one -->

---

## 🚀 Features

- 🎶 **Generate AI music** from scratch based on your inputs
- ✨ Choose genre, mood, and tempo
- 🕒 Select duration (5–30 seconds)
- 📥 Download generated music in WAV format
- ⚡ GPU support for faster generation (if available)

---

## 🛠 Tech Stack

- [Streamlit](https://streamlit.io/) - Web interface
- [TorchAudio](https://pytorch.org/audio/) - Audio I/O
- [PyTorch](https://pytorch.org/) - Deep learning framework
- [MusicGen (Meta)](https://github.com/facebookresearch/audiocraft) - Pretrained generative music model

---

## 📦 Installation

> ⚠️ Requires Python 3.9+ and a working PyTorch environment.

### 1. Clone the repository

```bash
git clone https://github.com/your-username/ai-music-composer.git
cd ai-music-composer
