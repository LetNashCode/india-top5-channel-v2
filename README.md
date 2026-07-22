# 🎬 AI YouTube Shorts Automation

An end-to-end fully automated YouTube Shorts generation pipeline powered by Gemini AI, TikTok TTS, Whisper alignment, MoviePy, Pixabay, Pexels and the YouTube Data API.

The goal of this project is to generate high-retention YouTube Shorts completely automatically and publish them without any manual editing.

---

# Current Status

## ✅ Implemented

### 🤖 AI Script Generation

- Google Gemini Flash Lite
- Story-driven scripts
- Hook → Story → Twist → Ending structure
- 40–45 second narration
- SEO title generation
- SEO description generation
- 15 optimized tags
- Emotional scene planning
- Cinematic scene breakdown
- Open-loop endings
- High-retention writing prompt

---

### 🎥 Visual Engine

Each scene generates

- 4 shots

Each shot generates

- 5 alternative search queries

Visual sources

- Pixabay Videos
- Pexels Videos

Features

- Automatic fallback search
- Duplicate clip prevention
- Quality ranking
- Portrait preference
- HD preference
- Long clip preference
- Multi-source search
- Automatic downloading

---

### 🎙 Narration

Current Engine

- TikTok TTS
- Ghostface Voice

Features

- Automatic chunking
- UTF-8 safe splitting
- MP3 merging
- Automatic cleanup
- Emotion-ready pipeline

---

### 📝 Captions

- Whisper Alignment
- Word-level timestamps
- Automatic subtitles
- Burned into video

---

### 🎬 Video Assembly

MoviePy based editor

Features

- Dynamic scene durations
- Auto scaling
- Center crop
- Vertical format
- Motion zoom
- Background music
- Caption overlay
- Automatic timeline creation

---

### 📺 YouTube Upload

- OAuth Authentication
- Automatic upload
- Title
- Description
- Tags
- Shorts support

---

### 🔄 Automation

GitHub Actions

Runs automatically on schedule

Pipeline

Topic
↓

Script
↓

Narration
↓

Visual Search
↓

Download Assets
↓

Assemble Video
↓

Upload to YouTube

---

# Story Pipeline

```
Topic
      │
      ▼
Gemini AI
      │
      ▼
Hook
      │
      ▼
Story
      │
      ▼
Twist
      │
      ▼
Ending
      │
      ▼
Scene Planner
      │
      ▼
Visual Searches
```

---

# Video Pipeline

```
Script
      │
      ▼
TikTok TTS
      │
      ▼
Whisper Alignment
      │
      ▼
Pixabay
      │
      ▼
Pexels
      │
      ▼
MoviePy
      │
      ▼
Final Short
      │
      ▼
YouTube Upload
```

---

# Tech Stack

## AI

- Google Gemini Flash Lite

## Speech

- TikTok TTS

## Alignment

- Whisper

## Editing

- MoviePy

## Visual Sources

- Pixabay API
- Pexels API

## Upload

- YouTube Data API v3

## Automation

- GitHub Actions

---

# Project Structure

```
.
├── assemble.py
├── generate_script.py
├── visuals.py
├── tts.py
├── whisper_align.py
├── upload_youtube.py
├── main.py
├── config.yaml
├── requirements.txt
├── publish.yml
└── README.md
```

---

# Features

- AI-generated storytelling
- High-retention script writing
- Emotional scene planning
- Cinematic visual search
- Multi-source stock footage
- Automatic narration
- Word-level captions
- Motion effects
- Background music
- Automatic uploads
- Scheduled publishing
- Fully automated pipeline

---

# Environment Variables

```
GEMINI_API_KEY

PIXABAY_API_KEY

PEXELS_API_KEY

YOUTUBE_TOKEN_JSON

YOUTUBE_CLIENT_SECRET_JSON
```

---

# Current Workflow

```
Generate Topic
        │
        ▼
Generate Story
        │
        ▼
Generate Scene Plan
        │
        ▼
Generate Visual Searches
        │
        ▼
Download Videos
        │
        ▼
Generate Narration
        │
        ▼
Generate Captions
        │
        ▼
Assemble Video
        │
        ▼
Upload to YouTube
```

---

# Planned Improvements

## Script Engine

- 500+ categorized viral hooks
- Better emotional pacing
- Topic memory
- Retention scoring
- Hook optimization
- Multi-language support

---

## Visual Engine

- Better visual matching
- Documentary-style motion graphics
- Public-domain archives
- Maps
- Timelines
- Animated infographics
- Evidence board effects
- Dynamic camera movement
- Color grading

---

## Narration

- Emotion-aware TTS
- Better voice options
- Dynamic pacing
- Natural pauses

---

## Automation

- Multiple uploads per day
- Automatic topic queue
- Upload history
- Duplicate detection
- Scheduled YouTube publishing
- Retry failed uploads
- Analytics-driven scheduling

---

# Vision

Build a fully autonomous AI-powered YouTube Shorts production system capable of generating, editing, and publishing high-retention videos every day with zero manual intervention.
