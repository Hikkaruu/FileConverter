# Media Converter Toolkit

![Python](https://img.shields.io/badge/Python-3.10+-blue.svg)
![FFmpeg](https://img.shields.io/badge/FFmpeg-Required-red)

Media conversion tool for images, audio, and video.

## 📦 System Requirements

---

#### Essential Components

- [Python 3.10+](https://www.python.org/downloads/)
- [FFmpeg (Latest Release)](https://github.com/GyanD/codexffmpeg/releases)

#### FFmpeg installation

- Download [FFmpeg](https://github.com/GyanD/codexffmpeg/releases)
- Extract it to `C:\`
- Change folder's name to <b>ffmpeg</b>
- Add `C:\ffmpeg\bin` to <b>PATH</b>

#### Check installation

```bash
python --version
```

```bash
ffmpeg -version
```

#### Package Installation

```bash
pip install -r requirements.txt
```

<br>

## ✨ Core Features

---

#### 🖼️ Image Conversion

**Supported Formats:**  
`PNG`, `JPEG`, `BMP`, `TIFF`, `WEBP`, `ICO`

**Features:**

- 🖌️ Dynamic resizing with aspect ratio control
- 🔄 Rotation transformations
- 💎 Quality optimization (1–100 scale)
- 🧹 Complete metadata stripping

---

#### 🔊 Audio Processing

**Supported Formats:**  
`MP3`, `WAV`, `FLAC`, `OGG`, `AAC`

**Features:**

- 🔊 Bitrate conversion (128k–320k)
- 🎚️ Volume normalization (+/-)
- ⏩ Tempo/pitch adjustment
- ✂️ Precise sample-accurate trimming

---

#### 🎥 Video Transformation

**Supported Formats:**  
`MP4`, `WEBM`, `AVI`, `MOV`, `MKV`, `FLV`

**Features:**

- ⚡ Hardware-accelerated codec transcoding
- 📏 Resolution scaling
- 🎞️ Frame rate conversion (24–60fps)
- 🎵 Audio track extraction, removing, volume normalization
- ✂️ Trimming
- ⏩ Tempo/pitch adjustment

---

## 📝 Usage

#### Show help in console

```python
py main.py -h
```

```python
py main.py image/audio/video -h
```
