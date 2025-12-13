# Instagram AI Avatar Automation - User Guide

Welcome! This guide will help you use the Instagram AI Avatar Automation app to create content for your Instagram posts.

## Quick Start

### Step 1: Start the Backend Server

1. Open a terminal/command prompt
2. Navigate to the project folder
3. Run the backend server:
   ```bash
   ./run_backend.sh
   ```
   Or if that doesn't work:
   ```bash
   uvicorn backend.main:app --reload --host 0.0.0.0 --port 8000
   ```

4. You should see: `Uvicorn running on http://0.0.0.0:8000`

**Keep this terminal window open** - the server needs to keep running.

### Step 2: Open the App in Your Browser

1. Open `frontend/index.html` in your web browser
   - You can double-click the file, or
   - Right-click → "Open with" → Your browser

2. The app should load and show the main interface

## Using the App

### 1. Configure API Settings

At the top of the page, you'll see two fields:

- **API Key**: Enter your API key
  - For OpenAI: Get from https://platform.openai.com/api-keys
  - For Anthropic: Get from https://console.anthropic.com/
  - For Google: Get from https://makersuite.google.com/app/apikey

- **API Model**: Select which AI model to use
  - Recommended: `gpt-4o-mini` (good balance of quality and cost)
  - For best quality: `gpt-4o` or `claude-3-5-sonnet-20241022`

### 2. Create Content

1. **Enter Topic**: Type what you want to create content about
   - Example: "Productivity tips for entrepreneurs"
   - Example: "5 ways to grow your Instagram following"

2. **Select Content Type**: Choose from:
   - **Reel**: Short video script (25 seconds)
   - **Carousel**: Multi-slide post content
   - **Story**: Story content
   - **Post**: Regular post content

3. **Click "Generate Content"**: Wait a few seconds while the AI creates your content

### 3. Review Generated Content

After generation, you'll see several sections:

- **Script**: The main content/script for your post
- **Caption**: Ready-to-use Instagram caption with emojis
- **Hashtags**: 10-12 relevant hashtags
- **Alt Text**: Accessibility description for your image/video
- **Avatar Dialogue**: Script formatted for AI avatar videos (if applicable)

**Copy any content** you want to use by selecting the text and copying it.

### 4. Use the Checklist

Below the generated content, you'll see a checklist showing:

- ✅ **Completed**: Tasks the app completed automatically
- ⏳ **Pending**: Tasks not yet done
- ❌ **Failed**: Tasks that encountered errors
- 🔧 **Manual**: Tasks you need to do manually

**For each checklist item**, you can:
- Click **"Mark Manual"** if the automation didn't work and you'll do it yourself
- Click **"Mark Complete"** when you've finished that task

### 5. What to Do Next

The app generates text content only. You still need to:

1. **Create the Visual Content**:
   - Use CapCut, HeyGen, or other tools to create your video/avatar
   - Use Canva to create carousel slides
   - Get stock footage from Pexels/Pixabay

2. **Post to Instagram**:
   - Upload your video/image
   - Paste the generated caption
   - Add the hashtags
   - Add the alt text in Instagram's accessibility settings

3. **Engage**:
   - Reply to comments
   - Share to your Story
   - Track engagement metrics

See `manual_tasks.md` for a complete list of manual tasks.

## Complete Workflow: Automated vs Manual Tasks

Here's the complete step-by-step workflow showing which tasks are **automated** (done by the app) and which are **manual** (you do using external tools):

### Phase 1: Content Planning & Generation (Automated ✅)

**Step 1: Generate Idea** ✅ **AUTOMATED**
- You provide: Topic (e.g., "Productivity tips")
- App does: Generates content idea based on your topic
- Status: Completed automatically

**Step 2: Generate Script/Content** ✅ **AUTOMATED**
- App does: Creates script for Reels or content for Carousels
- Output: Ready-to-use script with hook, key points, and CTA
- Status: Completed automatically

**Step 3: Generate Caption** ✅ **AUTOMATED**
- App does: Creates catchy Instagram caption with emojis
- Output: 3 caption options (usually use the first one)
- Status: Completed automatically

**Step 4: Generate Hashtags** ✅ **AUTOMATED**
- App does: Suggests 10-12 relevant hashtags
- Output: Comma-separated hashtag list
- Status: Completed automatically

**Step 5: Generate Alt Text** ✅ **AUTOMATED**
- App does: Creates accessibility-friendly alt text
- Output: Descriptive alt text (≤120 chars)
- Status: Completed automatically

**Step 6: Generate Avatar Dialogue** ✅ **AUTOMATED** (Optional)
- App does: Creates formatted script for AI avatar videos
- Output: Script with gesture cues and tone markers
- Status: Completed automatically

---

### Phase 2: Visual & Audio Creation (Manual 🔧)

**Step 7: Create Voiceover (TTS)** 🔧 **MANUAL**
- Tool: TTSMaker / ElevenLabs Free / Narakeet
- You do: 
  1. Copy the generated script or avatar dialogue
  2. Upload to TTS service
  3. Generate voiceover
  4. Download MP3 audio file
- When: After getting script from app
- Status: Mark as "Manual" in checklist

**Step 8: Get Stock Footage** 🔧 **MANUAL** (Optional, for Reels)
- Tool: Pexels / Pixabay / Mixkit
- You do:
  1. Search for relevant footage
  2. Download free commercial videos
  3. Save for video editing
- When: Before or during video creation
- Status: Mark as "Manual" in checklist

**Step 9: Get Music/SFX** 🔧 **MANUAL** (Optional, for Reels)
- Tool: YouTube Audio Library / Instagram Music
- You do:
  1. Browse trending or copyright-free audio
  2. Select appropriate track
  3. Download or note the track name
- When: Before video editing
- Status: Mark as "Manual" in checklist

**Step 10: Build Avatar Video** 🔧 **MANUAL** (For AI Avatar Reels)
- Tool: HeyGen Free / CapCut AI Avatar / Pika Labs
- You do:
  1. Upload your portrait photo
  2. Paste the avatar dialogue script
  3. Adjust tone and language settings
  4. Generate video
  5. Export as 1080x1920 MP4
- When: After getting script and voiceover
- Status: Mark as "Manual" in checklist

**Step 11: Design Assets** 🔧 **MANUAL** (For Carousels)
- Tool: Canva Free
- You do:
  1. Use generated carousel content from app
  2. Create slides in Canva
  3. Design thumbnails/graphics
  4. Export images
- When: After getting carousel content from app
- Status: Mark as "Manual" in checklist

**Step 12: Edit Video** 🔧 **MANUAL** (For Reels)
- Tool: CapCut (Desktop/Web)
- You do:
  1. Import avatar video or stock footage
  2. Add voiceover audio
  3. Add captions (from generated script)
  4. Add emojis and transitions
  5. Add trending audio/music
  6. Ensure first 2 seconds have strong hook
  7. Keep under 30 seconds
  8. Export as 1080x1920 MP4
- When: After creating video and voiceover
- Status: Mark as "Manual" in checklist

---

### Phase 3: Publishing & Engagement (Manual 🔧)

**Step 13: Upload Post** 🔧 **MANUAL**
- Tool: Instagram App/Web
- You do:
  1. Upload your video/image/carousel
  2. Paste the generated caption
  3. Add the generated hashtags
  4. Add alt text in Instagram's accessibility settings
  5. Post during peak times (see timing below)
- When: After all content is ready
- Status: Mark as "Complete" in checklist

**Step 14: Share to Story** 🔧 **MANUAL**
- Tool: Instagram App
- You do:
  1. Immediately after posting, share to Story
  2. Add engaging sticker or text
- When: Right after posting
- Status: Mark as "Complete" in checklist

**Step 15: Engage with Audience** 🔧 **MANUAL**
- Tool: Instagram App
- You do:
  1. Reply to first 5-10 comments within 15 minutes
  2. Reply to DMs
  3. Spend 20 minutes engaging
- When: Within first hour after posting
- Status: Mark as "Complete" in checklist

**Step 16: Track Metrics** 🔧 **MANUAL**
- Tool: Instagram Insights / Metricool Free
- You do:
  1. Monitor saves, comments, shares
  2. Note performance metrics
  3. Identify what worked
- When: 24-48 hours after posting
- Status: Mark as "Complete" in checklist

---

### Weekly Tasks (Manual 🔧)

These are ongoing tasks you do weekly:

1. **Analyze Top-Performing Posts** 🔧
   - Review engagement metrics
   - Identify patterns in successful content

2. **Research Trending Reels Audio** 🔧
   - Browse Instagram Reels
   - Note trending audio tracks for future use

3. **Update Hashtags List** 🔧
   - Research new relevant hashtags
   - Update your hashtag strategy

4. **Refresh Avatar/Voice** 🔧 (If using AI avatar)
   - Update avatar appearance
   - Adjust voice settings if needed

---

### Quick Reference: Task Sequence

**For a Reel:**
1. ✅ Generate idea (App)
2. ✅ Generate script (App)
3. ✅ Generate caption (App)
4. ✅ Generate hashtags (App)
5. ✅ Generate alt text (App)
6. ✅ Generate avatar dialogue (App)
7. 🔧 Create voiceover (You - TTSMaker/ElevenLabs)
8. 🔧 Get stock footage (You - Pexels/Pixabay)
9. 🔧 Get music (You - YouTube Audio Library)
10. 🔧 Build avatar video (You - HeyGen/CapCut)
11. 🔧 Edit video (You - CapCut)
12. 🔧 Upload to Instagram (You)
13. 🔧 Share to Story (You)
14. 🔧 Engage with audience (You)
15. 🔧 Track metrics (You)

**For a Carousel:**
1. ✅ Generate idea (App)
2. ✅ Generate carousel content (App)
3. ✅ Generate caption (App)
4. ✅ Generate hashtags (App)
5. ✅ Generate alt text (App)
6. 🔧 Design slides (You - Canva)
7. 🔧 Upload to Instagram (You)
8. 🔧 Share to Story (You)
9. 🔧 Engage with audience (You)
10. 🔧 Track metrics (You)

### Best Posting Times (IST)

- **Monday**: 11 AM (Carousel)
- **Tuesday**: 7 PM (Reel)
- **Wednesday**: 12 PM, 9 PM (Story)
- **Thursday**: 6 PM (Reel)
- **Friday**: 11 AM (Carousel)
- **Saturday**: 1 PM (Reel)
- **Sunday**: 10 AM, 8 PM (Story)

## Tips for Best Results

### Writing Good Topics
- Be specific: "5 morning routines" is better than "routines"
- Include your niche: "Productivity tips for entrepreneurs"
- Think about your audience: What would they want to see?

### Choosing Content Types
- **Reels**: Best for reach and engagement
- **Carousels**: Great for educational content, saves
- **Stories**: Quick updates, behind-the-scenes
- **Posts**: Traditional content, longer captions

### Using Generated Content
- **Scripts**: Use as-is or edit to match your voice
- **Captions**: Add personal touches, your own emojis
- **Hashtags**: Mix with your own niche hashtags
- **Alt Text**: Always add for accessibility

## Troubleshooting

### "Failed to load configuration"
- **Problem**: Backend server isn't running
- **Solution**: Make sure you started the backend server (Step 1)

### "Content creation failed"
- **Problem**: API key might be invalid or expired
- **Solution**: Check your API key, ensure you have credits/quota

### "CORS error" in browser console
- **Problem**: Browser blocking requests
- **Solution**: Make sure backend is running on `http://localhost:8000`

### Generated content seems off
- **Problem**: Topic might be too vague
- **Solution**: Be more specific in your topic description

## Need Help?

- Check `manual_tasks.md` for tasks outside the app
- Review `README.md` for technical details
- Ensure backend server is running before using the app

## Example Workflow

1. **Morning**: Open app, generate 3 content ideas
2. **Select best**: Pick the topic that resonates
3. **Generate**: Create all content (script, caption, hashtags)
4. **Afternoon**: Create video/visuals using external tools
5. **Evening**: Post to Instagram with generated caption
6. **Next day**: Engage with comments, track metrics

Happy creating! 🚀

