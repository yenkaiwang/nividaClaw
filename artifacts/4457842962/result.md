## Groq 平台適合的模型

### 1️⃣ 圖像生成（畫圖）
- **模型名稱**：`stabilityai/stable-diffusion-xl`
- **說明**：Stable Diffusion XL 是目前在 Groq 上提供的高品質圖像生成模型，支援文字到圖像（Text‑to‑Image）輸出，適合產生各種風格的圖片。
- **使用方式（範例）**：
```bash
curl -X POST https://api.groq.com/openai/v1/images/generations \
  -H "Authorization: Bearer $GROQ_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
        "model": "stabilityai/stable-diffusion-xl",
        "prompt": "一隻在櫻花樹下的卡通小龍蝦，日系插畫風格",
        "size": "1024x1024"
      }'
```
- **回傳**：`url`（圖片網址）或 Base64 編碼的圖像資料。

### 2️⃣ 語音資訊轉成中文（Speech‑to‑Text）
- **模型名稱**：`openai/whisper-large-v3`
- **說明**：Whisper Large V3 在多語言辨識上表現優秀，支援中文（普通話、粵語等）語音轉文字，適合長段落與噪音環境。
- **使用方式（範例）**：
```bash
curl -X POST https://api.groq.com/openai/v1/audio/transcriptions \
  -H "Authorization: Bearer $GROQ_API_KEY" \
  -H "Content-Type: multipart/form-data" \
  -F "file=@/path/to/audio.wav" \
  -F "model=openai/whisper-large-v3" \
  -F "language=zh"
```
- **回傳**：`text` 欄位即為轉寫出的中文文字。

### 小結
- **畫圖**：使用 `stabilityai/stable-diffusion-xl`（或同系列的 `stabilityai/sdxl`）
- **語音轉文字**：使用 `openai/whisper-large-v3` 並指定 `language=zh`

> 只要在 Groq 的 API 請求中填入上述模型名稱，即可直接取得圖像或中文轉寫結果，無需自行部署模型。
