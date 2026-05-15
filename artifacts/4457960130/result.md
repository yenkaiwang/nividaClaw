## 任務完成：將 gpt-oss-120b 換成 stable-diffusion-xl

### 修改內容
已將專案設定檔 `githubclaw.json` 中所有 `gpt-oss-120b` 替換為 `stable-diffusion-xl`，同時更新對應的顯示名稱（label）。

### 異動檔案
- **`githubclaw.json`**

### 具體修改項目

| # | 位置 | 原內容 | 新內容 |
|---|------|--------|--------|
| 1 | Cloudflare Workers AI → models | `@cf/openai/gpt-oss-120b` | `@cf/openai/stable-diffusion-xl` |
|   |   | `GPT OSS 120B` | `Stable Diffusion XL` |
| 2 | Groq → defaultModel | `openai/gpt-oss-120b` | `openai/stable-diffusion-xl` |
| 3 | Groq → models | `openai/gpt-oss-120b` | `openai/stable-diffusion-xl` |
|   |   | `GPT OSS 120B` | `Stable Diffusion XL` |

### 驗證結果
- JSON 格式檢查：**通過**
- 專案程式碼中已無殘留 `gpt-oss-120b`（歷史記錄檔如 `issue.jsonl` 與 `artifacts` 內的執行日誌未更動）
