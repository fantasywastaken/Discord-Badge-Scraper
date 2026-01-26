# Discord Badge Scraper

<img src="https://i.imgur.com/iGOhBr5.png">

---

### ⚙️ How It Works

- **Proxyless Operation**: Operates directly through Discord's API without any proxy requirements, using your user token for authentication.
- **Two-Phase Scanning**: First rapidly scans all members for rare badges using public flags (no API calls), then fetches detailed profiles only for matched users.
- **Rare Badge Detection**: Identifies users with valuable badges like Discord Employee, Partner, Bug Hunter, Early Supporter, Verified Bot Developer, and more.
- **Complete Profile Extraction**: Once a rare badge holder is found, extracts ALL their badges including Nitro tenure, Server Boost levels, and HypeSquad houses.
- **Webhook Integration**: Sends beautifully formatted embeds to your Discord webhook with user details, avatar, and complete badge list.
- **Rate Limit Handling**: Intelligent retry mechanism with automatic backoff when hitting Discord's rate limits.
- **Multi-Profile Support**: Processes all server members automatically with progress tracking.

---

## 📁 Setup

### 1. Requirements

Install required libraries using pip:
```bash
pip install discord.py-self aiohttp colorama
```

### 2. Configuration

You will need:
- **Discord User Token**: Your personal Discord account token
- **Server ID**: Target server's ID to scan
- **Webhook URL**: Discord webhook URL for receiving results

---

### 🚀 Usage

Run the script:
```bash
python badgescraper.py
```

You will be prompted to enter:
```
Token: [Your Discord Token]
Server ID: [Target Server ID]
Webhook: [Your Webhook URL]
```

#### 📊 Console Output
```
Guild: Example Server
Fetching members...
✓ 8341 members

Phase 1: Finding RARE badge users...
Target badges: Discord Employee, Partner, HypeSquad Events, Bug Hunter, Early Supporter, Bug Hunter Gold, Verified Bot Dev, Certified Mod
✓ Found 47 users with RARE badges

Phase 2: Fetching ALL badges & sending...
✓ [1/47] Username (5 badges)
   Early Supporter, HypeSquad Bravery, Diamond Nitro, Boost Level 4, Active Developer
✓ [2/47] AnotherUser (3 badges)
   Verified Bot Dev, Platinum Nitro, HypeSquad Balance
...
```

---

### 🎯 Target Badges (Rare)

These badges trigger a full profile scan:

| Badge | Flag Value |
|-------|------------|
| Discord Employee | `1 << 0` |
| Partner | `1 << 1` |
| HypeSquad Events | `1 << 2` |
| Bug Hunter | `1 << 3` |
| Early Supporter | `1 << 9` |
| Bug Hunter Gold | `1 << 14` |
| Verified Bot Developer | `1 << 17` |
| Certified Moderator | `1 << 19` |

---

### 🏅 Extracted Badges

Once a rare user is found, these badges are extracted:

**Flag Badges:**
- Discord Employee, Partner, HypeSquad Events
- Bug Hunter (Level 1 & 2)
- HypeSquad Houses (Bravery, Brilliance, Balance)
- Early Supporter, Verified Bot Developer
- Active Developer, Certified Moderator

**Profile Badges (via API):**
- Nitro Tenure (Bronze → Fire)
- Server Boost Levels (1-9)

---

### 🛠️ Technical Features

| Feature | Description |
|---------|-------------|
| **Selfbot Architecture** | Uses `discord.py-self` for user account authentication |
| **Async Operations** | Built with `asyncio` and `aiohttp` for non-blocking requests |
| **Public Flags Parsing** | Bitwise operations for instant badge detection without API calls |
| **Profile API Integration** | Fetches `/users/{id}/profile` for complete badge data |
| **Retry Mechanism** | 3 retry attempts with exponential backoff on failures |
| **Rate Limit Compliance** | Automatic detection and waiting for rate limit resets |

---

### 📨 Webhook Output

Each rare user is sent as an embed containing:

- **Rank**: Discovery order number
- **User ID**: With clickable mention
- **Avatar**: Thumbnail image
- **Badge Count**: Total badges found
- **Badge Emojis**: Visual representation
- **Badge Names**: Full list of badge names

---

### ⚡ Performance

| Server Size | Phase 1 (Scan) | Phase 2 (per user) |
|-------------|----------------|-------------------|
| 1,000 members | ~instant | ~0.5s |
| 10,000 members | ~1-2s | ~0.5s |
| 100,000 members | ~5-10s | ~0.5s |

*Phase 2 time depends on number of rare badge holders found*

---

### 📋 Dependencies

| Package | Version | Purpose |
|---------|---------|---------|
| `discord.py-self` | Latest | Discord selfbot client |
| `aiohttp` | Latest | Async HTTP requests |
| `colorama` | Latest | Colored console output |

---

### ⚠️ Disclaimer

This tool is developed for educational and research purposes only. Using selfbots violates Discord's Terms of Service and may result in account termination. The developer is not responsible for any misuse or consequences arising from the use of this tool. Use at your own risk.
