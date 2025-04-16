# 🎵 AI Music Composer

An interactive web app powered by Meta's **MusicGen** model that lets you generate original music based on **genre, mood, tempo**, and **duration**. No musical skills needed — just your creativity!

To Try out the model [click](https://huggingface.co/spaces/spcool/AI-Music-Composer)

---

## 🚀 Features

- 🎶 Generate AI music from scratch using your text inputs
- 🧠 Powered by Meta's [MusicGen](https://github.com/facebookresearch/audiocraft)
- 🎨 Choose Genre, Mood, Tempo
- ⏱ Select Duration (5–30 seconds)
- 💾 Download generated music in `.wav` format
- ⚡ GPU support for fast generation

---

## 🛠 Tech Stack

- [Streamlit](https://streamlit.io/) - For building the UI
- [TorchAudio](https://pytorch.org/audio/) - For audio I/O
- [PyTorch](https://pytorch.org/) - For model execution
- [Meta’s MusicGen](https://github.com/facebookresearch/audiocraft) - Pretrained generative music model

---

## 📦 Installation

> ⚠️ Requires Python 3.9+ and a working PyTorch environment.

### 1. Clone the repository

```bash
git clone https://github.com/your-username/ai-music-composer.git
cd ai-music-composer
