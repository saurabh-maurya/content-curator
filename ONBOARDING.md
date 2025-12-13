# 📚 Instagram Content Creator - Complete Onboarding Guide

Welcome! This guide will walk you through everything you need to know to use the Instagram AI Content Creator app. Follow these steps in order.

---

## 🎯 What This App Does

**The app automatically generates:**
- ✅ Content ideas and scripts
- ✅ Instagram captions
- ✅ Hashtags
- ✅ Alt text for accessibility
- ✅ Avatar dialogue scripts

**You need to do manually (outside the app):**
- 🔧 Create videos/visuals
- 🔧 Edit videos
- 🔧 Post to Instagram
- 🔧 Engage with your audience

---

## 📋 Part 1: Initial Setup (One-Time)

### Step 1: Install the App

**What you do:**
1. Make sure you have Python 3.8 or higher installed
2. Open a terminal/command prompt
3. Navigate to the project folder:
   ```bash
   cd /path/to/content_curator
   ```
4. Create a virtual environment (recommended):
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```
5. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

**Status:** ✅ Setup complete

---

### Step 2: Get Your API Key

**What you do:**
1. Choose an AI provider:
   - **OpenAI**: Go to https://platform.openai.com/api-keys (create account if needed)
   - **Anthropic**: Go to https://console.anthropic.com/ (create account if needed)
   - **Google**: Go to https://makersuite.google.com/app/apikey (create account if needed)
2. Create a new API key
3. Copy the key (you'll paste it in the app later)

**Status:** ✅ API key ready

**Note:** You don't need to save it anywhere - just paste it in the app when you use it.

---

## 🚀 Part 2: Daily Usage - Creating Content

### Step 3: Start the App

**What you do:**
1. Open a terminal/command prompt
2. Navigate to the project folder
3. Start the backend server:
   ```bash
   ./run_backend.sh
   ```
   Or if that doesn't work:
   ```bash
   uvicorn backend.main:app --reload --host 0.0.0.0 --port 8000
   ```
4. **Keep this terminal window open** - the server needs to keep running
5. Open `frontend/index.html` in your web browser (double-click the file)

**Status:** ✅ App is running

---

### Step 4: Configure API Settings (First Time Only)

**What you do in the app:**
1. At the top of the page, find the "API Key" field
2. Paste your API key (from Step 2)
3. Select your API model from the dropdown:
   - **Recommended:** `gpt-4o-mini` (good balance of quality and cost)
   - **Best quality:** `gpt-4o` or `claude-3-5-sonnet-20241022`

**Status:** ✅ API configured

**Note:** The app remembers your settings while it's open, but you'll need to enter them again if you close and reopen.

---

### Step 5: Generate Your Content

**What you do in the app:**
1. **Enter a topic** in the "Topic" field
   - Example: "Productivity tips for entrepreneurs"
   - Example: "5 ways to grow your Instagram following"
   - Be specific - better topics = better content

2. **Select content type** from the dropdown:
   - **Reel**: Short video script (25 seconds) - best for reach
   - **Carousel**: Multi-slide post content - great for educational content
   - **Story**: Story content - quick updates
   - **Post**: Regular post content - traditional format

3. **Click "Generate Content"**
   - Wait 10-30 seconds while the AI creates your content

**What the app does automatically:**
- ✅ Generates a content idea based on your topic
- ✅ Creates a script (for Reels) or content (for Carousels)
- ✅ Generates 3 caption options with emojis
- ✅ Suggests 10-12 relevant hashtags
- ✅ Creates accessibility-friendly alt text
- ✅ Formats avatar dialogue script (if applicable)

**Status:** ✅ Content generated

---

### Step 6: Review and Copy Generated Content

**What you see in the app:**
- **Script**: The main content/script for your post
- **Caption**: Ready-to-use Instagram caption with emojis (usually use the first one)
- **Hashtags**: 10-12 relevant hashtags (comma-separated)
- **Alt Text**: Accessibility description for your image/video
- **Avatar Dialogue**: Script formatted for AI avatar videos (if applicable)

**What you do:**
1. Review each section
2. **Copy the content** you want to use:
   - Select the text
   - Copy it (Ctrl+C / Cmd+C)
   - Save it somewhere (Notes app, Google Doc, etc.)

**Status:** ✅ Content saved

---

### Step 7: Check Your Checklist

**What you see in the app:**
Below the generated content, there's a checklist showing:
- ✅ **Completed**: Tasks the app completed automatically
- ⏳ **Pending**: Tasks not yet done
- ❌ **Failed**: Tasks that encountered errors
- 🔧 **Manual**: Tasks you need to do manually

**What you do:**
- Click **"Mark Manual"** if automation didn't work and you'll do it yourself
- Click **"Mark Complete"** when you've finished that task

**Status:** ✅ Checklist reviewed

---

## 🔧 Part 3: Manual Tasks - Creating Visual Content

Now you have the text content. Next, you need to create the visual/audio content using external tools.

---

### Step 8: Create Voiceover (For Reels with Avatar)

**What you do manually:**
1. **Copy the script** from the app (Step 6)
2. **Go to a TTS (Text-to-Speech) service:**
   - **TTSMaker**: https://ttsmaker.com/ (free)
   - **ElevenLabs Free**: https://elevenlabs.io/ (free tier)
   - **Narakeet**: https://www.narakeet.com/ (free)
3. **Upload/paste your script**
4. **Generate voiceover**
5. **Download the MP3 audio file**
6. **Save it** for later use

**Tool:** TTSMaker / ElevenLabs Free / Narakeet  
**Time:** 5-10 minutes  
**Status:** 🔧 Manual task - mark as complete in checklist when done

---

### Step 9: Get Stock Footage (Optional, for Reels)

**What you do manually:**
1. **Go to a stock footage site:**
   - **Pexels**: https://www.pexels.com/videos/ (free)
   - **Pixabay**: https://pixabay.com/videos/ (free)
   - **Mixkit**: https://mixkit.co/free-stock-video/ (free)
2. **Search for relevant footage** related to your topic
3. **Download free commercial videos**
4. **Save them** for video editing

**Tool:** Pexels / Pixabay / Mixkit  
**Time:** 10-15 minutes  
**Status:** 🔧 Manual task - optional, mark as complete when done

---

### Step 10: Get Music/Sound Effects (Optional, for Reels)

**What you do manually:**
1. **Go to a music library:**
   - **YouTube Audio Library**: https://www.youtube.com/audiolibrary (free, copyright-free)
   - **Instagram Music**: Available in Instagram app (trending audio)
2. **Browse trending or copyright-free audio**
3. **Select appropriate track** for your content
4. **Download or note the track name**

**Tool:** YouTube Audio Library / Instagram Music  
**Time:** 5-10 minutes  
**Status:** 🔧 Manual task - optional, mark as complete when done

---

### Step 11: Build Avatar Video (For AI Avatar Reels)

**What you do manually:**
1. **Take a clear portrait photo** (front-facing, good lighting)
2. **Go to an AI avatar service:**
   - **HeyGen Free**: https://www.heygen.com/ (free tier)
   - **CapCut AI Avatar**: Available in CapCut app
   - **Pika Labs**: https://pika.art/ (free tier)
3. **Upload your portrait photo**
4. **Paste the avatar dialogue script** from the app (Step 6)
5. **Adjust tone and language settings**
6. **Generate video**
7. **Export as 1080x1920 MP4** (Instagram Reels format)

**Tool:** HeyGen Free / CapCut AI Avatar / Pika Labs  
**Time:** 10-15 minutes  
**Status:** 🔧 Manual task - mark as complete when done

---

### Step 12: Design Assets (For Carousels)

**What you do manually:**
1. **Go to Canva**: https://www.canva.com/ (free)
2. **Use the generated carousel content** from the app (Step 6)
3. **Create slides in Canva:**
   - Create a new design (1080x1080 for Instagram)
   - Design each slide based on the content
   - Add graphics, text, and visuals
4. **Design thumbnails/graphics** if needed
5. **Export images** (download as JPG or PNG)

**Tool:** Canva Free  
**Time:** 15-30 minutes  
**Status:** 🔧 Manual task - mark as complete when done

---

### Step 13: Edit Video (For Reels)

**What you do manually:**
1. **Open CapCut**: https://www.capcut.com/ (free, desktop or web)
2. **Import your content:**
   - Avatar video (from Step 11) OR stock footage (from Step 9)
   - Voiceover audio (from Step 8)
   - Music/SFX (from Step 10, if using)
3. **Edit the video:**
   - Add captions (use the script from the app)
   - Add emojis and transitions
   - Add trending audio/music
   - Ensure first 2 seconds have a strong hook
   - Keep under 30 seconds
4. **Export as 1080x1920 MP4** (Instagram Reels format)

**Tool:** CapCut (Desktop/Web)  
**Time:** 20-30 minutes  
**Status:** 🔧 Manual task - mark as complete when done

---

## 📱 Part 4: Publishing to Instagram

### Step 14: Upload Post to Instagram

**What you do manually:**
1. **Open Instagram** (app or web)
2. **Click the "+" button** to create a new post
3. **Upload your content:**
   - Video (from Step 13) for Reels
   - Images (from Step 12) for Carousels
4. **Add the generated content:**
   - Paste the **caption** from the app (Step 6)
   - Add the **hashtags** from the app (Step 6)
   - Add **alt text** in Instagram's accessibility settings (from Step 6)
5. **Post during peak times** (see timing guide below)
6. **Click "Share"**

**Tool:** Instagram App/Web  
**Time:** 5 minutes  
**Status:** 🔧 Manual task - mark as complete in checklist when done

---

### Step 15: Share to Story

**What you do manually:**
1. **Immediately after posting**, go to your post
2. **Click the "Share" button** (paper airplane icon)
3. **Select "Add post to your story"**
4. **Add an engaging sticker or text**
5. **Share to your story**

**Tool:** Instagram App  
**Time:** 2 minutes  
**Status:** 🔧 Manual task - mark as complete in checklist when done

---

### Step 16: Engage with Audience

**What you do manually:**
1. **Within 15 minutes of posting**, reply to the first 5-10 comments
2. **Reply to DMs** if you receive any
3. **Spend 20 minutes engaging** with your audience
4. **Like and respond** to comments on your post

**Tool:** Instagram App  
**Time:** 20 minutes  
**Status:** 🔧 Manual task - mark as complete in checklist when done

---

### Step 17: Track Metrics

**What you do manually:**
1. **Wait 24-48 hours** after posting
2. **Go to Instagram Insights** (or use Metricool Free)
3. **Monitor metrics:**
   - Saves
   - Comments
   - Shares
   - Reach
4. **Note what worked** and what didn't
5. **Use insights** for future content

**Tool:** Instagram Insights / Metricool Free  
**Time:** 10 minutes  
**Status:** 🔧 Manual task - mark as complete in checklist when done

---

## 📅 Part 5: Weekly Tasks

These are ongoing tasks you should do weekly to improve your content:

### Weekly Checklist

**What you do manually:**

1. **Analyze Top-Performing Posts** 🔧
   - Review engagement metrics from the past week
   - Identify patterns in successful content
   - Note what topics/format worked best

2. **Research Trending Reels Audio** 🔧
   - Browse Instagram Reels
   - Note trending audio tracks
   - Save them for future use

3. **Collaborate with Creators** 🔧
   - Reach out to small creators in your niche
   - Plan collaborations
   - Cross-promote content

4. **Update Hashtags List** 🔧
   - Research new relevant hashtags
   - Update your hashtag strategy
   - Test new hashtag combinations

5. **Refresh Avatar/Voice** 🔧 (If using AI avatar)
   - Update avatar appearance if needed
   - Adjust voice settings if needed
   - Keep content fresh

**Time:** 1-2 hours per week  
**Status:** 🔧 Manual tasks

---

## ⏰ Best Posting Times (IST - Indian Standard Time)

Post during these times for best engagement:

| Day | Content Type | Time | Purpose |
|-----|-------------|------|---------|
| Monday | Carousel | 11 AM | Educational content |
| Tuesday | Reel | 7 PM | Boost reach |
| Wednesday | Story | 12 PM, 9 PM | Engage followers |
| Thursday | Reel | 6 PM | Build trust |
| Friday | Carousel | 11 AM | Save-worthy post |
| Saturday | Reel | 1 PM | Lighter tone |
| Sunday | Story | 10 AM, 8 PM | Strengthen community |

---

## 📊 Quick Reference: Complete Workflow

### For a Reel:
1. ✅ **App:** Generate idea, script, caption, hashtags, alt text, avatar dialogue
2. 🔧 **You:** Create voiceover (TTSMaker/ElevenLabs)
3. 🔧 **You:** Get stock footage (Pexels/Pixabay) - optional
4. 🔧 **You:** Get music (YouTube Audio Library) - optional
5. 🔧 **You:** Build avatar video (HeyGen/CapCut)
6. 🔧 **You:** Edit video (CapCut)
7. 🔧 **You:** Upload to Instagram
8. 🔧 **You:** Share to Story
9. 🔧 **You:** Engage with audience
10. 🔧 **You:** Track metrics

### For a Carousel:
1. ✅ **App:** Generate idea, carousel content, caption, hashtags, alt text
2. 🔧 **You:** Design slides (Canva)
3. 🔧 **You:** Upload to Instagram
4. 🔧 **You:** Share to Story
5. 🔧 **You:** Engage with audience
6. 🔧 **You:** Track metrics

---

## 💡 Tips for Best Results

### Writing Good Topics
- **Be specific:** "5 morning routines" is better than "routines"
- **Include your niche:** "Productivity tips for entrepreneurs"
- **Think about your audience:** What would they want to see?

### Choosing Content Types
- **Reels:** Best for reach and engagement
- **Carousels:** Great for educational content, saves
- **Stories:** Quick updates, behind-the-scenes
- **Posts:** Traditional content, longer captions

### Using Generated Content
- **Scripts:** Use as-is or edit to match your voice
- **Captions:** Add personal touches, your own emojis
- **Hashtags:** Mix with your own niche hashtags
- **Alt Text:** Always add for accessibility

---

## 🆘 Troubleshooting

### "Failed to load configuration"
- **Problem:** Backend server isn't running
- **Solution:** Go back to Step 3 and start the backend server

### "Content creation failed"
- **Problem:** API key might be invalid or expired
- **Solution:** Check your API key, ensure you have credits/quota

### "CORS error" in browser console
- **Problem:** Browser blocking requests
- **Solution:** Make sure backend is running on `http://localhost:8000`

### Generated content seems off
- **Problem:** Topic might be too vague
- **Solution:** Be more specific in your topic description

---

## ✅ Summary

**What the app does automatically:**
- ✅ Idea generation
- ✅ Script/content creation
- ✅ Caption generation
- ✅ Hashtag suggestions
- ✅ Alt text generation
- ✅ Avatar dialogue formatting

**What you do manually:**
- 🔧 Create voiceover (TTS)
- 🔧 Build avatar video
- 🔧 Edit video
- 🔧 Design carousel slides
- 🔧 Upload to Instagram
- 🔧 Engage with audience
- 🔧 Track metrics

---

## 🎯 Your First Content Creation Session

**Follow these steps in order:**

1. ✅ Start the app (Steps 3-4)
2. ✅ Generate content (Step 5)
3. ✅ Copy generated content (Step 6)
4. 🔧 Create visual/audio content (Steps 8-13)
5. 🔧 Post to Instagram (Steps 14-16)
6. 🔧 Track results (Step 17)

**Total time:** 1-2 hours for your first post (faster once you get the hang of it!)

---

**Happy creating! 🚀**

For more details, see:
- `USER_GUIDE.md` - Detailed usage instructions
- `manual_tasks.md` - Complete list of manual tasks
- `DEVELOPER_GUIDE.md` - Technical setup guide


